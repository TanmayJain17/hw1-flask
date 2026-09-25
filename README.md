# HW1 Flask app

One Flask application for comparing AWS Elastic Beanstalk, Google App Engine, and IBM Code Engine. `GET /` returns JSON containing the message, hostname, Python version, and `PORT`; `GET /health` returns a health status.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python application.py
curl http://localhost:8080/
```

## AWS Elastic Beanstalk

From the repository root, make an archive with files at its root:

```bash
zip beanstalk-deploy.zip application.py requirements.txt Procfile
```

Create a Python 3.12 web-server environment and upload `beanstalk-deploy.zip`. The Procfile listens on `PORT` when set, otherwise on 8000 for the Beanstalk Python proxy default. Verify the environment URL returns JSON. Terminate the environment after recording results.

## Google App Engine

In a Cloud Shell configured for the intended project, run:

```bash
gcloud app deploy
gcloud app browse
```

`app.yaml` supplies the Python 3.12 runtime and Gunicorn entrypoint. Confirm the JSON response and disable the application after the exercise if appropriate.

## IBM Code Engine

Create a Code Engine project and application from this public GitHub source repository using Dockerfile build strategy. Configure application port 8080; the container also honors a platform-provided `PORT`. Open its URL and confirm the JSON response. Delete the project after the exercise.

## Local container smoke test

```bash
docker build -t hw1-flask .
docker run --rm -p 8080:8080 -e PORT=8080 hw1-flask
curl http://localhost:8080/
```

Cloud account setup, deployments, timings, billing, and screenshots must be performed and recorded separately; this repository does not claim any service has been deployed.
