# 🚀 FastAPI with Redis as Cache

This project demonstrates the integration of **FastAPI** with **Redis** as a caching layer to optimize database queries. The primary database in this example is **SQLite**, but the design is flexible enough to support more robust databases like **PostgreSQL** or **MySQL** in production environments.

## 📚 Description

The primary goal of this project is to showcase how Redis can be effectively used as a caching mechanism to reduce the load on the main database and improve the overall performance of API queries. By caching frequently accessed data, the system can deliver faster response times and handle higher loads with ease.

## 🛠️ Technologies Used

- **FastAPI**: A modern, fast web framework for building APIs with Python, known for its performance and ease of use.
- **Redis**: In-memory database used as a cache.
- **SQLite**: A lightweight relational database used as the primary storage for this demonstration. However, the system is designed to work with other databases like **PostgreSQL** or **MySQL** in a production setup.
- **SQLModel**: A powerful library that simplifies working with SQL databases in Python by combining the best features of SQLAlchemy and Pydantic.

## 📂 Project Structure

```plaintext
.
├── api
│   └── v100
│       └── users
│           └── users.py
├── businesslogic
│   └── users.py
├── db
│   ├── sqlite
│   │   └── database.db
│   ├── database.py
│   └── tables
│       └── users.py
├── schemas
│   └── users.py
├── main.py
└── README.md
```

## 📋 Endpoints

### 📝 List Users

- **URL**: `/users`
- **Method**: `GET`
- **Description**: Retrieves a list of all users.
- **Response**:
  ```json
  [
    {
      "name": "string",
      "first_last_name": "string",
      "second_last_name": "string",
      "email": "user@example.com",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ]
  ```

### 🔍 Get User by ID

- **URL**: `/users/{id}`
- **Method**: `GET`
- **Description**: Retrieves a user by their ID.
- **Parameters**:
  - `id` (UUID): User ID.
- **Response**:
  ```json
  {
    "name": "string",
    "first_last_name": "string",
    "second_last_name": "string",
    "email": "user@example.com",
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
  ```

### ➕ Create User

- **URL**: `/users`
- **Method**: `POST`
- **Description**: Creates a new user.
- **Request Body**:
  ```json
  {
    "name": "string",
    "first_last_name": "string",
    "second_last_name": "string",
    "email": "user@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "name": "string",
    "first_last_name": "string",
    "second_last_name": "string",
    "email": "user@example.com",
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
  ```

### ✏️ Update User

- **URL**: `/users/{id}`
- **Method**: `PUT`
- **Description**: Updates an existing user.
- **Parameters**:
  - `id` (UUID): User ID.
- **Request Body**:
  ```json
  {
    "name": "string",
    "first_last_name": "string",
    "second_last_name": "string",
    "email": "user@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "name": "string",
    "first_last_name": "string",
    "second_last_name": "string",
    "email": "user@example.com",
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
  ```

### ❌ Delete User

- **URL**: `/users/{id}`
- **Method**: `DELETE`
- **Description**: Deletes a user by their ID.
- **Parameters**:
  - `id` (UUID): User ID.
- **Response**: `204 No Content`

## 🛠️ Environment Variables

Before running the application, make sure to set the following environment variables:

```plaintext
ENVIRONMENT="local"
REDIS_HOST="localhost"
REDIS_PORT=6379
```

## 🚀 Getting Started

1. **Clone the repository.**
   ```sh
   git clone https://github.com/egoan82/fastapi-with-redis-as-cache.git
   cd fastapi-with-redis-as-cache
   ```

2. **Install Poetry if you don't have it installed.**
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install the project dependencies.**
   ```sh
   poetry install
   ```

4. **Activate the Poetry virtual environment.**
   ```sh
   poetry shell
   ```

5. **Run the application with `uvicorn`.**
   ```sh
   uvicorn main:app --reload
   ```

## 🧑‍💻 Contributions

Contributions are welcome! Whether it's reporting a bug, suggesting new features, or improving the documentation, feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License.

---

Thank you for exploring **FastAPI with Redis as Cache**! 🎉
