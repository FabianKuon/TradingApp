# Use a python image
FROM python:latest

# Set working directory
WORKDIR /app

# Install requirements
COPY requiremtents.txt /app
RUN pip install --no-chache-dir --upgrade  -r requirements.txt

# Copy scripts to the app folder
COPY . /app/backend

# Start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
