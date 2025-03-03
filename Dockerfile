# Use a lightweight base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy script and data files
COPY script.py .
COPY home/data /home/data

# Set entry point to execute script
CMD ["sh", "-c", "python script.py && tail -f /dev/null"]


