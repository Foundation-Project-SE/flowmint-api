# Foundation Project - Backend API

Welcome to the official Backend repository for the Foundation project. This service exposes a RESTful API built with **FastAPI**, designed to be scalable and modular following **Hexagonal Architecture**.

## Tech Stack

* **Language:** Python 3.12 or higher
* **Web Framework:** FastAPI
* **ASGI Server:** Uvicorn
* **Validation & Configuration:** Pydantic and Pydantic-Settings
* **Environment Variables:** python-dotenv

## Project Architecture

The project follows **Hexagonal Architecture** with the following structure:

```
src/
├── main.py                 # Application entry point
├── domain/                 # Domain layer
│   ├── models/             # Domain models
│   └── schemas/            # Domain schemas
├── application/            # Application layer
│   ├── ports/              # Interfaces (ports)
│   └── use_cases/          # Use cases
└── infrastructure/         # Infrastructure layer
    ├── api/                # HTTP routes and controllers
    │   └── v1/
    ├── config.py           # Configuration (Pydantic Settings)
    └── persistence/        # Persistence adapters
```

## Prerequisites

Make sure you have installed on your machine:

* [Python 3.12](https://www.python.org/downloads/) or higher
* [Poetry](https://python-poetry.org/) (dependency management)
* [Git](https://git-scm.com/)

## Installation and Configuration (Local)

### 1. Clone the repository

```bash
git clone https://github.com/Foundation-Project-SE/backend.git
cd backend
```

### 2. Install dependencies (Poetry)

```bash
poetry install
```

### 3. Configure environment variables

Create a `.env` file in the project root with the following variables:

```env
DATABASE_URL=your_database_url
```

Optional (with default values):

```env
PROJECT_NAME=FlowMint API
API_V1_STR=/api/v1
```

### 4. Activate the virtual environment (if using Poetry)

```bash
poetry shell
```

## Running the Application

### Development

```bash
uvicorn src.main:app --reload
```

### Production

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

The application will be available at `http://localhost:8000`.

## Available Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/` | Redirects to Swagger documentation (`/docs`) |
| **GET** | `/api/v1/health` | System health check. Verifies the service is operational. |
| **GET** | `/api/v1/ping` | Simple latency test. Returns `{"message": "pong"}` |
| **GET** | `/docs` | Interactive Swagger UI documentation |
| **GET** | `/api/v1/openapi.json` | OpenAPI schema in JSON format |

## API Documentation

Once the server is running, access the interactive documentation at:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
