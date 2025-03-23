# Cloud Native Application v2.0.0

A modern cloud-native application built with FastAPI, featuring an interactive UI and comprehensive CI/CD pipeline.

## Features
- Modern web interface with Tailwind CSS
- Task management system (create, list, delete tasks)
- Real-time health monitoring
- RESTful API endpoints
- Automated CI/CD with GitHub Actions
- Docker containerization
- Comprehensive test suite
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

![Screenshot 2025-03-23 195919](https://github.com/user-attachments/assets/620ff69e-c814-4042-803e-dc63db5a3e0c)

![Screenshot 2025-03-23 195944](https://github.com/user-attachments/assets/d7491b52-c5e5-4ceb-b947-e662770bbc0c)

![Screenshot 2025-03-23 195955](https://github.com/user-attachments/assets/ce2b8302-2774-4bb5-af9b-373aab3bb5a8)

## API Endpoints
- `/`: Interactive web interface
- `/tasks`: Task management endpoints (GET, POST, DELETE)
- `/health`: Health check endpoint with real-time monitoring
- `/docs`: OpenAPI documentation (Swagger UI)
- `/redoc`: Alternative API documentation

## Development
- FastAPI with automatic reload enabled
- Comprehensive test suite with pytest
- GitHub Actions for automated testing and deployment
- Container registry integration

## CI/CD Pipeline
The application includes a complete CI/CD pipeline that:
- Runs automated tests
- Generates test coverage reports
- Builds and pushes Docker images
- Deploys to container registry
- Ensures code quality
