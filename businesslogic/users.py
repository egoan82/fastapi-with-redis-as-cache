import json
from typing import List, Union
from uuid import UUID
from sqlmodel import Session

from api.v100.schemas.users import UserRead, UserCreate, UserUpdate
from db.repositories.users import UsersRepository
from dependencies.redis.redis import RedisClient


class BusinessLogicUsers:

    def __init__(self):
        self.users = UsersRepository()
        self.redis = RedisClient()

        self.dynamodb = None

    def list(self, db: Session) -> List[UserRead]:
        return self.users.list(db=db)

    def get_one(self, db: Session, id: UUID) -> Union[UserRead, None]:
        user_cache = self.redis.get(key=str(id))
        if user_cache:
            user_json = json.loads(user_cache)
            return UserRead(**user_json)

        user_db = self.users.get_one(db=db, id=id)

        if not user_db:
            return None

        user_dict = user_db.model_dump()
        user_dict["id"] = str(user_db.id)
        self.redis.set(key=str(user_db.id), value=json.dumps(user_dict))

        return user_db

    def create(self, db: Session, user: UserCreate) -> UserRead:
        return self.users.create(db=db, user=user)

    def update(self, db: Session, id: UUID, user: UserUpdate) -> UserRead:
        user_db = self.users.update(db=db, id=id, user=user)

        user_cache = self.redis.get(key=str(id))
        if user_cache:
            user_dict = user_db.model_dump()
            user_dict["id"] = str(user_db.id)
            self.redis.set(key=str(user_db.id), value=json.dumps(user_dict))

        return user_db

    def delete(self, db: Session, id: UUID) -> None:
        user_cache = self.redis.get(key=str(id))
        if user_cache:
            self.redis.delete(key=str(id))

        self.users.delete(db=db, id=id)