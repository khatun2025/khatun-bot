# Python image
FROM python:3.10-slim

# Working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the bot code
COPY . .

# Run the bot
CMD ["python", "main.py"]