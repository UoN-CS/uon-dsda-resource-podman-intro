# Use the official Python image from Docker Hub
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Make sure pip is up to date
RUN pip install --upgrade pip

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the Python script
CMD ["python", "process.py"] > output.txt
