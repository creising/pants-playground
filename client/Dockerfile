FROM python:3

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./client /app

COPY ./logger /internal/logger

# Install any needed packages specified in requirements.txt
# If you have any additional dependencies, add them to your requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install /internal/logger

# Expose the port that Uvicorn will listen on
EXPOSE 8000

# Run the main.py script using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
