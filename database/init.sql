#!/bin/bash
set -e

# Create necessary extensions
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Enable encryption extensions
    CREATE EXTENSION IF NOT EXISTS pgcrypto;
    CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
    
    -- Create application user
    CREATE USER customer_app WITH PASSWORD 'app_password_123!';
    
    -- Grant necessary permissions
    GRANT CONNECT ON DATABASE customer_management TO customer_app;
    GRANT USAGE ON SCHEMA public TO customer_app;
    GRANT CREATE ON SCHEMA public TO customer_app;
    
    -- Set up logging
    ALTER SYSTEM SET log_statement = 'all';
    ALTER SYSTEM SET log_destination = 'stderr';
    ALTER SYSTEM SET logging_collector = on;
    ALTER SYSTEM SET log_directory = '/var/log/postgresql';
    ALTER SYSTEM SET log_filename = 'postgresql-%Y-%m-%d.log';
    
    SELECT pg_reload_conf();
EOSQL