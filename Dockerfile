FROM ubuntu:24.04

LABEL author=tuanhy_le

SHELL ["/bin/bash", "-c"] 

# ENVIRONMENT VARIABLES
ENV PATH="/root/.local/bin/:$PATH"

# EXTERNAL SOURCES
# add uv sources
ADD https://astral.sh/uv/0.5.13/install.sh /uv-installer.sh

# EXECUTE
# install system dependencies
RUN apt-get update -y && \ 
    apt update -y && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    apt install -y unzip wget && \
    apt install -y git

# install uv dependencies
RUN sh /uv-installer.sh && rm /uv-installer.sh

# create python environment
RUN uv python install 3.10
RUN uv venv --python 3.10
RUN source /.venv/bin/activate

# install python dependencies
RUN uv pip install matplotlib
RUN uv pip install torch torchvision torchaudio
RUN uv pip install scikit-learn
RUN uv pip install tqdm

# create workspace
RUN mkdir /home/ubuntu/workspace
WORKDIR /home/ubuntu/workspace

CMD ["/bin/bash"]
