# Premium Scientific Calculator App

A modern, responsive, and secure glassmorphic calculator web application built with a FastAPI (Python) backend and a vanilla HTML/JS/CSS frontend. The project includes automated CI/CD testing using GitHub Actions and is configured for seamless deployment to Render.

---

## Features
* **Modern Dark Glassmorphic Design**: An elegant dark theme with soft ambient shadows, frosted glass panels, and smooth button interactive states (hover and click animations).
* **Robust Mathematical Expression Parsing**: Evaluates arithmetic and trigonometric expressions safely using Python's `ast` module (guards against Remote Code Execution).
* **Static File Serving**: Serves the frontend web pages directly from the FastAPI backend to simplify hosting, reduce latency, and completely avoid Cross-Origin Resource Sharing (CORS) issues.
* **Continuous Integration**: Automatically runs the backend test suite via GitHub Actions on every commit and pull request.
* **Infrastructure as Code**: Features a Render Blueprint configuration (`render.yaml`) and custom `Dockerfile` for single-click deployment.

---

## Local Development Setup

### 1. Prerequisites
Ensure you have [Anaconda or Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed, and the `fastapi` environment initialized.

### 2. Install Dependencies
Activate your conda environment and install the required dependencies:
```bash
conda activate fastapi
pip install -r backend/requirements.txt
```

### 3. Running the Server Locally
To start the FastAPI backend and host the integrated frontend, run the following command from the project root:
```bash
uvicorn main:app --app-dir backend --reload --port 8000
```
Then, open your web browser and navigate to:
```
http://127.0.0.1:8000
```

### 4. Running Unit Tests
To execute backend logic tests:
```bash
cd backend
pytest
```

---

## CI/CD Pipeline Configuration
A automated GitHub Actions workflow is defined in `.github/workflows/ci.yml`. 
* On every **push** or **pull request** to the `main` or `master` branches, GitHub Actions spins up a test environment, installs all python dependencies, and runs `pytest`.
* If any tests fail, the build will break, notifying you immediately of code regressions.

---

## Deployment to Render

You can deploy this project to Render in two ways:

### Option A: Using the Render Blueprint (Recommended)
1. Push this project repository to your GitHub account.
2. Log in to [Render](https://render.com).
3. Go to **Blueprints** and click **New Blueprint Instance**.
4. Connect your GitHub repository containing this project.
5. Render will read the `render.yaml` configuration and automatically spin up the Dockerized web service.

### Option B: Deploying manually as a Docker Web Service
1. In the Render Dashboard, click **New +** and select **Web Service**.
2. Connect your GitHub repository.
3. Choose **Docker** as the runtime.
4. Set the build command and start command to defaults (they are handled automatically by the root `Dockerfile`).
5. Render will automatically map the dynamic port to run your application.
