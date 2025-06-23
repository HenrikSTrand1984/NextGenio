# Setup Guide for NextGenio

This guide will walk you through the steps of setting up **NextGenio** on your local machine for development.

## Prerequisites

Before setting up the environment, make sure you have the following installed:

- **Python 3.9** or later.
- **Docker** (Optional, for containerized development).
- **GitHub account** for CI/CD setup.
- **Supabase** account for PostgreSQL setup (required for database).

## Step 1: Clone the repository

Start by cloning the **NextGenio** repository:

```bash
git clone https://github.com/your-username/NextGenio.git
cd NextGenio
python3 -m venv venv
source venv/bin/activate
.\venv\Scripts\activate
pip install -r requirements.txt
OPENAI_API_KEY=your_openai_api_key
CLICKUP_API_KEY=your_clickup_api_key
DROPBOX_API_KEY=your_dropbox_api_key
DATABASE_URL=your_database_url  # Set up Supabase PostgreSQL
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
docker build -t nextgenio .
docker run -p 8000:8000 nextgenio
docker-compose up
uvicorn src.main:app --reload
pip install --upgrade pip
