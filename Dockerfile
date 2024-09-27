# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1

# Expose the Flask port (default is 5000)
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]



