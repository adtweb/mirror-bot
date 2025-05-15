# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set UTF-8 locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run bot.py when the container launches
CMD ["python", "bot.py"]