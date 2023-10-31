# Use the official Python image as the base image
FROM python:3.8-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Create a directory to mount the scores
RUN mkdir -p /app/scores

# Command to run the application
CMD ["python3", "Main_Game.py"]
