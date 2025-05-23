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

## Possible improvements
- More unit tests for the endpoints on the backend with mock API calls, testing components on the front-end, and just more tests testing edge cases, invalid data inputs etc. 
-  Improved error handling -- instead of handling errors in each function, can centralize it by using custom exception handlers on FastAPI.
- The database is hosted on Render. I did include the external database URL in
.env and GitHub Secrets. But this would normally be omitted since it includes credentials. 
- Possibly using async and await with FastAPI in the routers to improve performance when making database calls.