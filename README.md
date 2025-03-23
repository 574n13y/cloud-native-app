# Cloud Native Application

A modern cloud-native application built with FastAPI, ready for containerization and deployment.

## Features
- RESTful API endpoints
- Health check endpoint
- Docker support
- OpenAPI documentation

## Quick Start

### Running Locally
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

### Running with Docker
1. Build the Docker image:
```bash
docker build -t cloud-native-app .
```

2. Run the container:
```bash
docker run -p 8000:8000 cloud-native-app
```

## API Endpoints
- `/`: Welcome message
- `/health`: Health check endpoint
- `/docs`: OpenAPI documentation (Swagger UI)
- `/redoc`: Alternative API documentation

## Development
The application uses FastAPI with automatic reload enabled during development.
