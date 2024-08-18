# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and model
COPY app.py .
COPY ./model/modelo_DecisionTree.pkl modelo_DecisionTree.pkl


EXPOSE 5000

# Run the command to start the Flask server
CMD ["python", "app.py"]