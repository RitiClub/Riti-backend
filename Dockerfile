# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install curl, unzip and Rust-based uv package manager
RUN apt-get update && apt-get install -y curl unzip && \
    curl -Ls https://astral.sh/uv/install.sh | bash && \
    rm -rf /var/lib/apt/lists/*

# Add uv to PATH (the installer adds it to ~/.cargo/bin)
ENV PATH="/root/.cargo/bin:$PATH"

# Copy and install dependencies
RUN pip install uv
COPY requirements.txt .
#RUN uv pip install --system -r requirements.txt
RUN uv pip sync --system requirements.txt

# Copy project files
COPY . .
RUN python manage.py collectstatic --noinput
# Expose port
EXPOSE 8069

# Run Gunicorn
CMD ["gunicorn", "mysite.asgi:application", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8069"]

