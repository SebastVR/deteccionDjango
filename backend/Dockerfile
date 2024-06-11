#dockerfile

FROM python:3.12-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        binutils \
        gdal-bin \
        gcc \
        g++ \
        libssl-dev \
        libgdal-dev \
        libproj-dev \
        libkrb5-dev \
        jq \
        tk \
        libgl1-mesa-dev \ 
        libglib2.0-0 \
        postgresql-client && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app

# upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# install Python dependencies
COPY . .

# install requirements from pip
RUN pip install --no-cache-dir -r requirements.txt



EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]