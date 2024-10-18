# syntax=docker/dockerfile:1
# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /python-docker

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget apt-transport-https software-properties-common && \
    apt-get install -y \
        ca-certificates \
        fonts-liberation \
        libappindicator3-1 \
        libasound2 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdbus-1-3 \
        libexpat1 \
        libgbm1 \
        libgtk-3-0 \
        libnspr4 \
        libnss3 \
        libx11-xcb1 \
        libxcomposite1 \
        libxcursor1 \
        libxdamage1 \
        libxrandr2 \
        xdg-utils \
        libu2f-udev \
        libvulkan1 \
        libxshmfence-dev \
        libegl1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app will run on
EXPOSE 8181

# Run the application
CMD [ "python3","app.py", "--host=0.0.0.0"]
