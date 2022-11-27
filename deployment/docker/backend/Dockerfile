FROM python:latest

WORKDIR /app

# Use a python image
FROM python:latest

# Install requirements
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY core /core

EXPOSE 80

# Start the server
CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "80"]
