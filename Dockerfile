# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask openai flask-cors

# Expose the application port
EXPOSE 5000

# Set environment variable for production
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Run Flask app
CMD ["python", "app.py"]
