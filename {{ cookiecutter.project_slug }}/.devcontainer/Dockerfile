FROM mcr.microsoft.com/devcontainers/python:{{ cookiecutter.python_version }}

# Install just command runner
RUN apt-get update && \
    apt-get install -y just curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER vscode

# Install uv package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh