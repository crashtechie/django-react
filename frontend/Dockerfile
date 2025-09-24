# Multi-stage build for React app with Nginx
# Using Google Distroless Node.js image for enhanced security
FROM gcr.io/distroless/nodejs20-debian12 AS runtime-base

# Build stage with minimal Node.js
FROM node:20.18.0-bookworm-slim AS builder

# Install security updates (debian-based)
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends dumb-init && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies (including devDependencies needed for build)
RUN npm ci

# Copy source code
COPY . .

# Build the app
RUN npm run build

# Clean up build artifacts and dependencies to reduce attack surface
RUN rm -rf node_modules package*.json src public /root/.npm /tmp/*

# Production stage  
FROM nginx:1.25.4-alpine3.19-slim

# Install security updates and curl for health checks
RUN apk update && apk upgrade --no-cache && \
    apk add --no-cache curl && \
    rm -rf /var/cache/apk/*

# Copy built app to nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Set proper permissions for nginx user
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/log/nginx && \
    touch /var/run/nginx.pid && \
    chown -R nginx:nginx /var/run/nginx.pid && \
    # Remove unnecessary packages to reduce attack surface
    apk del --purge apk-tools && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Switch to non-root user
USER nginx

# Expose ports
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl -f http://localhost/health || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]