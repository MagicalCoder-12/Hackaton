# Base image with Python 3.10
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
