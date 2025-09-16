# Use lightweight Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy only requirements to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY app.py .

# Expose the Flask app’s port
EXPOSE 8080

# Run the Flask server
CMD ["python", "app.py"]
