# Use a lightweight Python image (CPU-only, offline-safe)
FROM --platform=linux/amd64 python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install only the required package
RUN pip install --no-cache-dir PyMuPDF

# Create input and output folders inside the container
RUN mkdir -p /app/input /app/output

# Command to run your app when the container is started
CMD ["python", "main.py"]
