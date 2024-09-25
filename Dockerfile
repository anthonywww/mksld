FROM python:3.9-alpine

# Install necessary packages
RUN apk add --no-cache python3 py3-pip

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements or the script if there are no dependencies to install separately
COPY requirements.txt ./

RUN if [ -e requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Run the script when the container launches
CMD ["python3", "src/mksld.py"]