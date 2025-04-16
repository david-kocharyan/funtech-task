FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port for ASGI server
EXPOSE 8000

# Default command can be overridden in docker-compose
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "funtech.asgi:application"]
