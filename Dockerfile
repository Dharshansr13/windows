# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY app.py /app

# Install dependencies
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# #Run the app
CMD ["python", "app.py"]
