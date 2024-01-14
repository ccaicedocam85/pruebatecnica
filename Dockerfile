FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container at /app
COPY . /app/

# Expose the port that the app will run on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]