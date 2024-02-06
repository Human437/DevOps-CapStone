FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add non root user
RUN useradd -u 1001 nonroot

# Use non-root user
User nonroot

# Copy the rest of the application code
# Use --chown on COPY commands to set file permissions
COPY --chown=nonroot:nonroot . .

# Expose the ports needed to access the application
# Doesn't acutally do anything to the image, it is just documenation to the user
EXPOSE 8000

# Specify the command to run your Python application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]