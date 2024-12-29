FROM ubuntu:24.04

# EXTERNAL SOURCES

# add uv sources
ADD https://astral.sh/uv/0.5.13/install.sh /uv-installer.sh

# EXECUTE

# install system dependencies
RUN apt-get update -y && \ 
    apt update -y && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    apt install unzip wget -y &&

# install uv dependencies
RUN sh /uv-installer.sh && rm /uv-installer.sh &&

# create python environment
RUN uv venv ~/cv --python 3.10
RUN source ~/.cv/bin/activate

# ENVIRONMENT VARIABLES
ENV PATH="/root/.local/bin/:$PATH"
