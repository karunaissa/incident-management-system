# Use slim Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn (production WSGI server)
RUN pip install gunicorn

# Copy all app code
COPY . .

# Install python-dotenv (if not in requirements.txt)
RUN pip install python-dotenv

# Expose Flask port
EXPOSE 5000

# Run Flask app with Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "run:app"]
