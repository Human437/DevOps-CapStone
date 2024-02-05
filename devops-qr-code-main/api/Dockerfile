FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

#Expose the ports needed to access the application
EXPOSE 8000

# Specify the command to run your Python application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]