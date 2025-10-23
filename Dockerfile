# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /code

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source code
COPY ./app ./app

# Set environment variable to ensure logs show immediately
ENV PYTHONUNBUFFERED=1

# Default command to run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
