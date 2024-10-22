# Codinsight Backend 🧠

A powerful backend service that powers the Codinsight VS Code extension, helping developers understand code through AI-powered explanations.

The extension is available to use from [this link.](https://marketplace.visualstudio.com/items?itemName=Cinex10.codinsight)

## Overview 🎯

Codinsight is a VS Code extension that provides intelligent code explanations. It leverages Large Language Models to analyze and explain code snippets, making code comprehension faster and easier.

This repo is the backend of the extension.

## Features ⭐

- Code explanation generation using LLMs
- Support for multiple programming languages
- Fast API responses for real-time code analysis
- Docker containerization for easy deployment
- Multi-architecture support (AMD64/ARM64)

## Tech Stack 🛠️

- **Framework**: FastAPI, Pydantic
- **Language**: Python
- **Database**: MongoDB
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Cloud**: AWS ECR for container registry, AWS ECS for container deployment
- **AI**: LLM Integration

## Getting Started 🚀

### Prerequisites

- Python 3.9 or higher
- Docker
- AWS CLI (for deployment)

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/codinsight.git
cd codinsight
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the development server:
```bash
fastapi dev src/main.py
```

### Using Docker

1. Build the Docker image:
```bash
docker build -t codinsight .
```

2. Run the container:
```bash
docker run -p 80:80 --env-file .env codinsight
```

## API Documentation 📚

### Base URL
```
http://localhost/
```


## Deployment 🌐

The project uses GitHub Actions for CI/CD, automatically building and pushing Docker images to Amazon ECR (and Docker hub).

The project provide Docker images  versionning using specific commit hash for better traceability and reproducibility.

### AWS Setup

1. Create an ECR repository
2. Configure AWS credentials in GitHub secrets
3. Set up necessary IAM roles and permissions

### Environment Variables

Required environment variables:
```
DATABASE_URL=
API_V1_STR=
PROJECT_NAME=
DESCRIPTION=
VERSION=
SECRET_KEY=
ACCESS_TOKEN_EXPIRE_MINUTES=
ALLOWED_ORIGINS=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
LLM_API_KEY=
MODEL=
```

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License 📄

[Your chosen license]

## Contact 📧

yassine.driss@etu.umontpellier.fr