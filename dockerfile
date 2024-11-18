# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the working directory
COPY . .

# Expose the port that Flask will run on
EXPOSE 5000

# Define environment variables (if needed, such as FLASK_APP)
ENV FLASK_APP=app.py

# Run the Flask app when the container starts
CMD ["flask", "run", "--host", "0.0.0.0"]
