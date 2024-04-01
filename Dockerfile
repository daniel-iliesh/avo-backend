# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /avo-backend

# Install system dependencies
RUN apt-get update && apt-get install -y netcat

# Install pipenv
RUN pip install pipenv

# Install Python dependencies
COPY Pipfile Pipfile.lock /avo-backend/
RUN pipenv install --system --deploy

# Copy the current directory contents into the container at /avo-backend
COPY . /avo-backend/

# Run the command to start uWSGI
CMD ["uwsgi", "--http", ":8000", "--module", "avo.wsgi", "--static-map", "/static=/avo-backend/static"]
