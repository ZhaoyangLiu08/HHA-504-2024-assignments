# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install flask

# Expose the port on which the app will run
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
