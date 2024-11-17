# Use slim version of python3.12
FROM python:3.12-slim

# Install basic dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    curl \
    libxrender1 \
    libxext6 \
    libgl1 \
    git \
    software-properties-common \
    libx11-6 \
    libxml2 \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Install Python dependencies
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    rdkit \
    snakemake \
    click 


# Install AutoDock Vina

RUN wget https://github.com/ccsb-scripps/AutoDock-Vina/releases/download/v1.2.5/vina_1.2.5_linux_x86_64 -O /usr/local/bin/vina
RUN chmod +x /usr/local/bin/vina

# Add working directory
WORKDIR /workspace

# Copy the source code
COPY . .

# Set the entrypoint
ENTRYPOINT ["/bin/bash"]