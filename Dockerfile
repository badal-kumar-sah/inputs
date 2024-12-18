# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies (if any are required, add a requirements.txt file)
RUN pip install --no-cache-dir --upgrade pip

# Expose a port (if needed, though not directly applicable here)
EXPOSE 8080

# Run main.py when the container launches
CMD ["python", "main.py"]
