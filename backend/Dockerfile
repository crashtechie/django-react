# Use the official uv image with Python 3.13 Alpine
FROM ghcr.io/astral-sh/uv:python3.13-alpine

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    curl \
    && rm -rf /var/cache/apk/*

# Copy uv configuration
COPY pyproject.toml uv.lock ./

# Install Python dependencies
RUN uv sync --frozen

# Copy project
COPY . .

# Create logs directory
RUN mkdir -p /app/logs

# Collect static files
RUN uv run python manage.py collectstatic --noinput

# Create a non-root user
RUN addgroup -g 1001 -S django && \
    adduser -S django -u 1001 -G django

# Change ownership of the app directory
RUN chown -R django:django /app

# Switch to non-root user
USER django

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -f http://localhost:8000/health/ || exit 1

# Start server
CMD ["uv", "run", "gunicorn", "customer_management.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--access-logfile", "/app/logs/access.log", "--error-logfile", "/app/logs/error.log"]