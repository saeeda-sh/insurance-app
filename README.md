# insurance-app
## Overview
Web application to display insurance policies. 

Built using:
- Backend: FastAPI, Pydantic, SQLAlchemy
- Frontend: React, Material UI
- Database: PostgreSQL



## Setup with Docker
1. Build and start Docker container. 
    ```shell
    docker-compose up --build
    ```

## Setup locally
1. Install backend dependencies
    ```shell
    cd backend
    pip install poetry
    poetry env use python3.11
    poetry install
    ```

2. Run the backend
    ```shell
    uvicorn backend.app.main:app --reload
    ```

3. Install frontend dependencies 
    ```shell
    cd frontend
    npm install
    ```

4. Run frontend
    ```shell
    npm start
    ```

5. Run tests (backend)
    ```shell
    pytest
    ```

