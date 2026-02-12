# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Download model weights
RUN python fetch_weights.py

# Expose port for Reflex
EXPOSE 8000
EXPOSE 3000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV REFLEX_ENV=prod

# Initialize and run Reflex app
CMD ["sh", "-c", "reflex init && reflex run --env prod --backend-only"]
