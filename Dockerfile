# Use the official Ubuntu base image
FROM ubuntu:latest

# Set a working directory
WORKDIR /app

# Copy code to container
COPY main.py .

# Copy FILE NAME TO CONVERT
COPY sample.pdf .

# Update the package list
RUN apt-get update

# Install Python, pip and other required system dependencies
RUN apt-get install -y python3 python3-pip ffmpeg
RUN apt-get install -y ffmpeg

# Install Python packages using pip
RUN pip3 install --default-timeout=100 --retries=5 PyMuPDF
RUN pip3 install tqdm
RUN pip3 install requests
RUN pip3 install pydub

# Clear the apt cache to reduce image size
# If you remove this layer by combining commands, make sure to keep the cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Command to run when the container starts (modify as needed)
CMD ["python3", "main.py"]