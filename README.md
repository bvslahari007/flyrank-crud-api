# Task API — CRUD Operations with FastAPI, PostgreSQL & Docker

A simple Task Management API built with **FastAPI** as part of the **FlyRank Backend AI Engineering Internship**.

This project demonstrates:

- REST API development with FastAPI
- Repository Pattern architecture
- PostgreSQL integration
- Docker and Docker Compose
- Environment variable configuration using `.env`
- Persistent data storage using Docker volumes

---

## Assignment Overview

### W2 · A1

Built a CRUD API using FastAPI with tasks stored in an in-memory Python list.

### W3 · A2

Replaced the in-memory storage with a PostgreSQL repository running inside Docker.

The API routes and service layer remained unchanged. Only the repository implementation changed, demonstrating the benefits of layered architecture and separation of concerns.

---

## Features

- Create tasks
- View all tasks
- View a task by ID
- Update task title and completion status
- Delete tasks
- Health check endpoint
- Interactive Swagger UI documentation
- PostgreSQL persistence
- Dockerized deployment

---

## Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL
- Psycopg2
- Docker
- Docker Compose
- Uvicorn
- Python-dotenv

---

## Project Structure

```text
.
├── main.py
├── model.py
├── repository.py
├── init.sql
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── NOTES.md
```

---

## API Endpoints

| Method | Endpoint           | Description     |
| ------ | ------------------ | --------------- |
| GET    | `/`                | API information |
| GET    | `/health`          | Health check    |
| GET    | `/tasks`           | Get all tasks   |
| GET    | `/tasks/{task_id}` | Get task by ID  |
| POST   | `/tasks`           | Create task     |
| PUT    | `/tasks/{task_id}` | Update task     |
| DELETE | `/tasks/{task_id}` | Delete task     |

---

## Environment Variables

Create a `.env` file in the project root:

```env
DB_NAME=tasksdb
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=postgres
DB_PORT=5432
```

The `.env` file is excluded from Git using `.gitignore`.

An example configuration is provided in `.env.example`.

---

## Running the Project

### Clone the Repository

```bash
git clone https://github.com/bvslahari007/flyrank-crud-api.git
cd flyrank-crud-api
```

### Start the Complete Stack

```bash
docker compose up --build
```

This command starts:

- PostgreSQL container
- FastAPI application container

---

## Access the Application

### API

```text
http://localhost:8000
```

### Swagger UI

```text
http://localhost:8000/docs
```

### OpenAPI Schema

```text
http://localhost:8000/openapi.json
```

---

## Example Request

### Create a Task

```bash
curl -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Submit Assignment 3"}'
```

Response:

```json
{
  "id": 1,
  "title": "Submit Assignment 3",
  "done": false
}
```

---

## Database

This project uses **PostgreSQL** running inside a Docker container.

The database is automatically initialized using `init.sql` during the first startup.

### Tasks Table

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
```

---

## Repository Pattern

The application follows the Repository Pattern.

The API routes and business logic do not directly interact with PostgreSQL.

Instead, they communicate with a repository layer.

### A1

```text
FastAPI
   ↓
In-Memory Repository
```

### A2

```text
FastAPI
   ↓
Postgres Repository
   ↓
PostgreSQL Database
```

Only the repository implementation changed.

The API routes, request models, response models, and endpoint behavior remained unchanged.

This demonstrates proper separation of concerns and storage independence.

---

## Docker Setup

### PostgreSQL Container

- Image: `postgres:17`
- Persistent Docker volume attached
- Environment variables configured through Docker Compose

### FastAPI Container

- Built from custom Dockerfile
- Installs dependencies from `requirements.txt`
- Runs using Uvicorn

### Start Everything

```bash
docker compose up
```

### Stop Everything

```bash
docker compose down
```

---

## Persistence Verification

To verify database persistence:

### Step 1

Create a task:

```bash
POST /tasks
```

Response:

```json
{
  "id": 1,
  "title": "Submit Assignment 3",
  "done": false
}
```

### Step 2

Confirm it exists:

```bash
GET /tasks
```

### Step 3

Stop containers:

```bash
docker compose down
```

### Step 4

Restart containers:

```bash
docker compose up
```

### Step 5

Query tasks again:

```bash
GET /tasks
```

The previously created task still exists.

This confirms that PostgreSQL data is stored in a Docker volume and survives application and container restarts.

---

## Validation & Error Handling

The API uses:

- FastAPI request validation
- Pydantic models
- HTTPException responses

Examples:

### Task Not Found

```json
{
  "detail": "Task not found"
}
```

### Invalid Request Body

```json
{
  "detail": [
    {
      "msg": "Field required"
    }
  ]
}
```

---

## Screenshots

### Swagger UI

Add screenshots of:

- GET /tasks
- POST /tasks
- PUT /tasks/{id}
- DELETE /tasks/{id}
- PostgreSQL container running
- Docker Compose services

---

## Learning Outcomes

Through this assignment I learned:

- Building REST APIs using FastAPI
- Using PostgreSQL from Python with psycopg2
- Repository Pattern architecture
- Managing configuration using environment variables
- Containerizing applications using Docker
- Running multi-container applications using Docker Compose
- Persisting database data using Docker volumes
- Connecting application and database containers through Docker networking

---

## Assignment Requirements Checklist

- [x] PostgreSQL running in Docker
- [x] Docker volume for persistent storage
- [x] Connection configuration through `.env`
- [x] `.env.example` committed
- [x] PostgreSQL repository implementation
- [x] Service and routes unchanged
- [x] Docker Compose setup
- [x] Entire stack starts with `docker compose up`
- [x] Data persistence verified after restart

---

## Author

**Vinaya Sangeeta Lahari Baswa**

B.Tech Computer Science & Engineering  
GITAM (Deemed to be University)

FlyRank Backend AI Engineering Internship
