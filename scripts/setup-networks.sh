#!/bin/bash
# Network setup script for Customer Management System

set -e

echo "Setting up Docker networks for Customer Management System..."

# Create external network if it doesn't exist
if ! docker network inspect customer_management_external >/dev/null 2>&1; then
    echo "Creating external network..."
    docker network create \
        --driver bridge \
        --subnet=172.20.0.0/16 \
        --ip-range=172.20.240.0/20 \
        --gateway=172.20.0.1 \
        customer_management_external
    echo "✓ External network created"
else
    echo "✓ External network already exists"
fi

# Create internal network if it doesn't exist
if ! docker network inspect customer_management_internal >/dev/null 2>&1; then
    echo "Creating internal network..."
    docker network create \
        --driver bridge \
        --internal \
        --subnet=172.21.0.0/16 \
        --ip-range=172.21.240.0/20 \
        --gateway=172.21.0.1 \
        customer_management_internal
    echo "✓ Internal network created"
else
    echo "✓ Internal network already exists"
fi

echo "Network setup complete!"
echo ""
echo "Networks:"
echo "- External (customer_management_external): Frontend container only"
echo "- Internal (customer_management_internal): Backend and database communication"
echo ""
echo "Security Features:"
echo "- Internal network blocks external access"
echo "- Frontend acts as reverse proxy to backend"
echo "- Database only accessible from backend"