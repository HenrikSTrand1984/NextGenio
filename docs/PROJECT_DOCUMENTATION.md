# NextGenio

NextGenio is a modern web application built with **FastAPI** that integrates various external services like **OpenAI**, **ClickUp**, and **Dropbox** for task management and AI-driven workflows. The project uses **Supabase** for database management and **Docker Build Cloud** for faster builds and deployment.

This repository contains the source code for the NextGenio platform, along with guides and documentation to help you set up, configure, and deploy the application.

## Project Structure

This project is organized into the following main components:

- **Backend**: [Backend Setup Guide](./backend/README.md)
- **Frontend**: [Frontend Setup Guide](./frontend/README.md)
- **Docker**: [Docker Setup Instructions](./docker/README.md)
- **API Documentation**: [API Endpoints and Usage](./docs/API_Documentation.md)
- **CI/CD**: [CI/CD Setup Guide](./docs/CI_CD_Guide.md)
- **Setup Guide**: [Instructions for Setting Up NextGenio](./docs/Setup_Guide.md)
- **Docker Setup**: [Docker Configuration Guide](./docs/Docker_Setup.md)
- **Documentation**: [General Documentation](./docs/README.md)

## Getting Started

Follow the instructions in the relevant sections to set up and configure **NextGenio** for local development or production environments.

### Prerequisites

Before you start, make sure you have the following installed:

- **Python 3.9** or later
- **Docker** (for containerized development, optional)
- **GitHub account** (for CI/CD integration with GitHub Actions)
- **Supabase account** (for PostgreSQL database setup)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/NextGenio.git
    cd NextGenio
    ```

2. If you're using **Docker** (recommended for containerized development):
    ```bash
    docker build -t nextgenio .
    docker run -p 8000:8000 nextgenio
    ```

3. Alternatively, for local setup:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables (e.g., **OPENAI_API_KEY**, **CLICKUP_API_KEY**, **DROPBOX_API_KEY**, **DATABASE_URL**) in a `.env` file.

5. To run the application locally:
    ```bash
    uvicorn src.main:app --reload
    ```

Your application will be available at **http://localhost:8000**.

## Deployment

Once you're ready to deploy your application to production, you can use Docker to push your Docker image to **Docker Hub** or deploy it on any cloud platform like **AWS**, **Google Cloud**, or **Azure**.

For more details, refer to the [Docker Setup](./docs/Docker_Setup.md) and [CI/CD Guide](./docs/CI_CD_Guide.md).

## Documentation

- **[API Documentation](./docs/API_Documentation.md)**: Overview of API endpoints and usage.
- **[Setup Guide](./docs/Setup_Guide.md)**: Detailed instructions on setting up NextGenio both locally and in the cloud.
- **[Docker Setup](./docs/Docker_Setup.md)**: Instructions for Docker configuration and usage.
- **[CI/CD Setup](./docs/CI_CD_Guide.md)**: Guide for setting up continuous integration and deployment with GitHub Actions.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

