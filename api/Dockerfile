# syntax=docker/dockerfile:1
# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Run the FastAPI application using uvicorn server
CMD uvicorn main:app --port=8000 --host=0.0.0.0