# IT Data Management Best Practices and Operational Excellence

## Executive Summary

This document establishes comprehensive data management best practices covering data governance, quality assurance, backup and recovery, compliance, and lifecycle management. These practices ensure data integrity, availability, security, and regulatory compliance while supporting business operations and decision-making.

## 1. Data Governance Framework

### 1.1 Data Classification and Cataloging

**Data Classification System:**
```python
# Data classification framework
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional
import json

class DataClassification(Enum):
    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"

class DataSensitivity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class DataAsset:
    name: str
    description: str
    classification: DataClassification
    sensitivity: DataSensitivity
    owner: str
    steward: str
    retention_period: int  # days
    compliance_requirements: List[str]
    access_controls: Dict[str, List[str]]
    
    def to_catalog_entry(self) -> Dict:
        return {
            "asset_id": self.generate_asset_id(),
            "name": self.name,
            "description": self.description,
            "classification": self.classification.value,
            "sensitivity": self.sensitivity.value,
            "governance": {
                "owner": self.owner,
                "steward": self.steward,
                "retention_days": self.retention_period
            },
            "compliance": self.compliance_requirements,
            "access_matrix": self.access_controls,
            "metadata": self.extract_metadata()
        }

class DataCatalog:
    def __init__(self):
        self.assets = {}
        self.lineage_graph = {}
    
    def register_asset(self, asset: DataAsset):
        """Register a data asset in the catalog."""
        asset_id = asset.generate_asset_id()
        self.assets[asset_id] = asset
        
        # Auto-discover schema and metadata
        metadata = self.discover_metadata(asset)
        asset.metadata = metadata
        
        # Log registration
        self.audit_log("asset_registered", {
            "asset_id": asset_id,
            "classification": asset.classification.value,
            "owner": asset.owner
        })
    
    def discover_metadata(self, asset: DataAsset) -> Dict:
        """Auto-discover data asset metadata."""
        if asset.name.startswith("customers"):
            return self.discover_table_metadata("customers")
        elif asset.name.startswith("orders"):
            return self.discover_table_metadata("orders")
        
        return {}
    
    def discover_table_metadata(self, table_name: str) -> Dict:
        """Discover database table metadata."""
        from django.db import connection
        
        with connection.cursor() as cursor:
            # Get column information
            cursor.execute("""
                SELECT column_name, data_type, is_nullable, column_default
                FROM information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position
            """, [table_name])
            
            columns = []
            for row in cursor.fetchall():
                columns.append({
                    "name": row[0],
                    "type": row[1],
                    "nullable": row[2] == "YES",
                    "default": row[3]
                })
            
            # Get table statistics
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            row_count = cursor.fetchone()[0]
            
            return {
                "schema": {
                    "columns": columns,
                    "row_count": row_count
                },
                "discovered_at": datetime.now().isoformat()
            }

# Data asset registration
customer_data = DataAsset(
    name="customers_table",
    description="Customer personal and contact information",
    classification=DataClassification.CONFIDENTIAL,
    sensitivity=DataSensitivity.HIGH,
    owner="data_team@company.com",
    steward="customer_success@company.com",
    retention_period=2555,  # 7 years
    compliance_requirements=["GDPR", "CCPA", "SOX"],
    access_controls={
        "read": ["customer_service", "sales", "management"],
        "write": ["customer_service", "data_admin"],
        "delete": ["data_admin", "compliance_officer"]
    }
)
```

### 1.2 Data Quality Management

**Data Quality Framework:**
```python
# Comprehensive data quality management
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Tuple
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DataQualityRule(ABC):
    def __init__(self, name: str, description: str, severity: str = "medium"):
        self.name = name
        self.description = description
        self.severity = severity
    
    @abstractmethod
    def validate(self, data: Any) -> Tuple[bool, str]:
        pass

class CompletenessRule(DataQualityRule):
    def __init__(self, required_fields: List[str]):
        super().__init__(
            "completeness_check",
            f"Required fields must not be null: {', '.join(required_fields)}",
            "high"
        )
        self.required_fields = required_fields
    
    def validate(self, data: pd.DataFrame) -> Tuple[bool, str]:
        missing_data = data[self.required_fields].isnull().sum()
        total_missing = missing_data.sum()
        
        if total_missing > 0:
            missing_details = missing_data[missing_data > 0].to_dict()
            return False, f"Missing data found: {missing_details}"
        
        return True, "All required fields are complete"

class UniquenessRule(DataQualityRule):
    def __init__(self, unique_fields: List[str]):
        super().__init__(
            "uniqueness_check",
            f"Fields must be unique: {', '.join(unique_fields)}",
            "high"
        )
        self.unique_fields = unique_fields
    
    def validate(self, data: pd.DataFrame) -> Tuple[bool, str]:
        for field in self.unique_fields:
            if field in data.columns:
                duplicates = data[field].duplicated().sum()
                if duplicates > 0:
                    return False, f"Found {duplicates} duplicate values in {field}"
        
        return True, "All specified fields are unique"

class ValidityRule(DataQualityRule):
    def __init__(self, field: str, validation_func, error_message: str):
        super().__init__(
            f"validity_check_{field}",
            f"Field {field} must pass validation: {error_message}",
            "medium"
        )
        self.field = field
        self.validation_func = validation_func
        self.error_message = error_message
    
    def validate(self, data: pd.DataFrame) -> Tuple[bool, str]:
        if self.field not in data.columns:
            return False, f"Field {self.field} not found in data"
        
        invalid_count = (~data[self.field].apply(self.validation_func)).sum()
        
        if invalid_count > 0:
            return False, f"Found {invalid_count} invalid values in {self.field}: {self.error_message}"
        
        return True, f"All values in {self.field} are valid"

class DataQualityEngine:
    def __init__(self):
        self.rules = []
        self.quality_history = []
    
    def add_rule(self, rule: DataQualityRule):
        """Add a data quality rule."""
        self.rules.append(rule)
    
    def validate_dataset(self, data: pd.DataFrame, dataset_name: str) -> Dict:
        """Run all quality rules against a dataset."""
        results = {
            "dataset": dataset_name,
            "timestamp": datetime.now().isoformat(),
            "total_rules": len(self.rules),
            "passed_rules": 0,
            "failed_rules": 0,
            "rule_results": [],
            "overall_score": 0.0
        }
        
        for rule in self.rules:
            try:
                is_valid, message = rule.validate(data)
                
                rule_result = {
                    "rule_name": rule.name,
                    "description": rule.description,
                    "severity": rule.severity,
                    "passed": is_valid,
                    "message": message,
                    "timestamp": datetime.now().isoformat()
                }
                
                results["rule_results"].append(rule_result)
                
                if is_valid:
                    results["passed_rules"] += 1
                else:
                    results["failed_rules"] += 1
                    
                    # Log quality issues
                    self.log_quality_issue(dataset_name, rule, message)
                
            except Exception as e:
                rule_result = {
                    "rule_name": rule.name,
                    "description": rule.description,
                    "severity": "error",
                    "passed": False,
                    "message": f"Rule execution failed: {str(e)}",
                    "timestamp": datetime.now().isoformat()
                }
                results["rule_results"].append(rule_result)
                results["failed_rules"] += 1
        
        # Calculate overall quality score
        if results["total_rules"] > 0:
            results["overall_score"] = results["passed_rules"] / results["total_rules"] * 100
        
        # Store results for trending
        self.quality_history.append(results)
        
        return results
    
    def log_quality_issue(self, dataset: str, rule: DataQualityRule, message: str):
        """Log data quality issues for monitoring."""
        issue = {
            "dataset": dataset,
            "rule": rule.name,
            "severity": rule.severity,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        
        # Send to monitoring system
        self.send_quality_alert(issue)
    
    def send_quality_alert(self, issue: Dict):
        """Send quality alert based on severity."""
        if issue["severity"] == "high":
            # Send immediate alert
            self.send_immediate_alert(issue)
        elif issue["severity"] == "medium":
            # Add to daily digest
            self.add_to_digest(issue)
    
    def generate_quality_report(self, days: int = 7) -> Dict:
        """Generate data quality trend report."""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        recent_results = [
            r for r in self.quality_history
            if datetime.fromisoformat(r["timestamp"]) > cutoff_date
        ]
        
        if not recent_results:
            return {"message": "No quality data available for the specified period"}
        
        # Calculate trends
        scores = [r["overall_score"] for r in recent_results]
        
        return {
            "period_days": days,
            "total_validations": len(recent_results),
            "average_quality_score": sum(scores) / len(scores),
            "quality_trend": self.calculate_trend(scores),
            "top_issues": self.get_top_issues(recent_results),
            "recommendations": self.generate_quality_recommendations(recent_results)
        }

# Customer data quality rules
quality_engine = DataQualityEngine()

# Add completeness rules
quality_engine.add_rule(CompletenessRule([
    "first_name", "last_name", "email"
]))

# Add uniqueness rules
quality_engine.add_rule(UniquenessRule(["email"]))

# Add validity rules
def is_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, str(email)))

def is_valid_phone(phone):
    import re
    # Simple phone validation
    pattern = r'^\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$'
    return bool(re.match(pattern, str(phone)))

quality_engine.add_rule(ValidityRule(
    "email", is_valid_email, "Must be valid email format"
))

quality_engine.add_rule(ValidityRule(
    "phone", is_valid_phone, "Must be valid phone number format"
))
```

## 2. Data Backup and Recovery

### 2.1 Backup Strategy Implementation

**Comprehensive Backup System:**
```python
# Enterprise backup and recovery system
import subprocess
import boto3
import gzip
import shutil
from pathlib import Path
from datetime import datetime, timedelta
import logging
import hashlib
import json

class BackupStrategy:
    def __init__(self, config: Dict):
        self.config = config
        self.logger = logging.getLogger('backup')
        self.s3_client = boto3.client('s3') if config.get('use_s3') else None
    
    def create_database_backup(self, backup_type: str = "full") -> Dict:
        """Create database backup with specified type."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"db_backup_{backup_type}_{timestamp}.sql"
        backup_path = Path(self.config['backup_dir']) / backup_filename
        
        try:
            # Create backup directory if it doesn't exist
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Database backup command
            if backup_type == "full":
                cmd = [
                    'pg_dump',
                    '--host', self.config['db_host'],
                    '--port', str(self.config['db_port']),
                    '--username', self.config['db_user'],
                    '--dbname', self.config['db_name'],
                    '--verbose',
                    '--clean',
                    '--no-owner',
                    '--no-privileges',
                    '--file', str(backup_path)
                ]
            else:  # incremental
                # Use WAL archiving for incremental backups
                cmd = [
                    'pg_basebackup',
                    '--host', self.config['db_host'],
                    '--port', str(self.config['db_port']),
                    '--username', self.config['db_user'],
                    '--pgdata', str(backup_path.with_suffix('')),
                    '--format', 'tar',
                    '--gzip',
                    '--progress',
                    '--verbose'
                ]
            
            # Set environment for password
            env = {'PGPASSWORD': self.config['db_password']}
            
            # Execute backup
            result = subprocess.run(cmd, env=env, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Compress backup if it's a full backup
                if backup_type == "full":
                    compressed_path = self.compress_backup(backup_path)
                    backup_path.unlink()  # Remove uncompressed file
                    backup_path = compressed_path
                
                # Calculate checksum
                checksum = self.calculate_checksum(backup_path)
                
                # Create backup metadata
                metadata = {
                    "backup_id": f"{backup_type}_{timestamp}",
                    "type": backup_type,
                    "timestamp": datetime.now().isoformat(),
                    "filename": backup_path.name,
                    "size_bytes": backup_path.stat().st_size,
                    "checksum": checksum,
                    "database": self.config['db_name'],
                    "status": "completed"
                }
                
                # Save metadata
                self.save_backup_metadata(metadata)
                
                # Upload to cloud storage if configured
                if self.s3_client:
                    self.upload_to_s3(backup_path, metadata)
                
                # Clean up old backups
                self.cleanup_old_backups()
                
                self.logger.info(f"Backup completed successfully: {backup_path}")
                return metadata
                
            else:
                error_msg = f"Backup failed: {result.stderr}"
                self.logger.error(error_msg)
                raise Exception(error_msg)
                
        except Exception as e:
            self.logger.error(f"Backup creation failed: {str(e)}")
            raise
    
    def compress_backup(self, backup_path: Path) -> Path:
        """Compress backup file using gzip."""
        compressed_path = backup_path.with_suffix(backup_path.suffix + '.gz')
        
        with open(backup_path, 'rb') as f_in:
            with gzip.open(compressed_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        return compressed_path
    
    def calculate_checksum(self, file_path: Path) -> str:
        """Calculate SHA-256 checksum of backup file."""
        sha256_hash = hashlib.sha256()
        
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        
        return sha256_hash.hexdigest()
    
    def upload_to_s3(self, backup_path: Path, metadata: Dict):
        """Upload backup to S3 with metadata."""
        s3_key = f"backups/{metadata['database']}/{backup_path.name}"
        
        try:
            # Upload file
            self.s3_client.upload_file(
                str(backup_path),
                self.config['s3_bucket'],
                s3_key,
                ExtraArgs={
                    'Metadata': {
                        'backup-id': metadata['backup_id'],
                        'backup-type': metadata['type'],
                        'checksum': metadata['checksum'],
                        'database': metadata['database']
                    },
                    'StorageClass': 'STANDARD_IA'  # Infrequent Access for cost optimization
                }
            )
            
            metadata['s3_location'] = f"s3://{self.config['s3_bucket']}/{s3_key}"
            self.logger.info(f"Backup uploaded to S3: {metadata['s3_location']}")
            
        except Exception as e:
            self.logger.error(f"S3 upload failed: {str(e)}")
            # Don't fail the backup if S3 upload fails
    
    def restore_database(self, backup_id: str, target_db: str = None) -> bool:
        """Restore database from backup."""
        metadata = self.get_backup_metadata(backup_id)
        if not metadata:
            raise ValueError(f"Backup {backup_id} not found")
        
        target_db = target_db or self.config['db_name']
        
        try:
            # Download from S3 if needed
            backup_path = self.ensure_backup_local(metadata)
            
            # Verify checksum
            if not self.verify_backup_integrity(backup_path, metadata['checksum']):
                raise Exception("Backup integrity check failed")
            
            # Decompress if needed
            if backup_path.suffix == '.gz':
                backup_path = self.decompress_backup(backup_path)
            
            # Restore database
            cmd = [
                'psql',
                '--host', self.config['db_host'],
                '--port', str(self.config['db_port']),
                '--username', self.config['db_user'],
                '--dbname', target_db,
                '--file', str(backup_path)
            ]
            
            env = {'PGPASSWORD': self.config['db_password']}
            result = subprocess.run(cmd, env=env, capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info(f"Database restored successfully from {backup_id}")
                return True
            else:
                error_msg = f"Restore failed: {result.stderr}"
                self.logger.error(error_msg)
                raise Exception(error_msg)
                
        except Exception as e:
            self.logger.error(f"Database restore failed: {str(e)}")
            raise
    
    def verify_backup_integrity(self, backup_path: Path, expected_checksum: str) -> bool:
        """Verify backup file integrity using checksum."""
        actual_checksum = self.calculate_checksum(backup_path)
        return actual_checksum == expected_checksum
    
    def cleanup_old_backups(self):
        """Clean up old backups based on retention policy."""
        retention_days = self.config.get('retention_days', 30)
        cutoff_date = datetime.now() - timedelta(days=retention_days)
        
        backup_dir = Path(self.config['backup_dir'])
        
        for backup_file in backup_dir.glob("db_backup_*"):
            if backup_file.stat().st_mtime < cutoff_date.timestamp():
                backup_file.unlink()
                self.logger.info(f"Deleted old backup: {backup_file}")

class BackupScheduler:
    def __init__(self, backup_strategy: BackupStrategy):
        self.backup_strategy = backup_strategy
        self.schedule = {}
    
    def schedule_backup(self, backup_type: str, cron_expression: str):
        """Schedule backup with cron expression."""
        self.schedule[backup_type] = cron_expression
    
    def run_scheduled_backups(self):
        """Run backups based on schedule."""
        from crontab import CronTab
        
        for backup_type, cron_expr in self.schedule.items():
            cron = CronTab(cron_expr)
            
            if cron.next(default_utc=True) == 0:  # Time to run
                try:
                    self.backup_strategy.create_database_backup(backup_type)
                except Exception as e:
                    self.logger.error(f"Scheduled backup failed: {str(e)}")

# Backup configuration
backup_config = {
    'backup_dir': '/var/backups/database',
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'customer_db',
    'db_user': 'backup_user',
    'db_password': 'secure_backup_password',
    'use_s3': True,
    's3_bucket': 'company-database-backups',
    'retention_days': 30
}

# Initialize backup system
backup_strategy = BackupStrategy(backup_config)
scheduler = BackupScheduler(backup_strategy)

# Schedule backups
scheduler.schedule_backup('full', '0 2 * * 0')      # Weekly full backup at 2 AM Sunday
scheduler.schedule_backup('incremental', '0 2 * * 1-6')  # Daily incremental backups
```

### 2.2 Disaster Recovery Planning

**Disaster Recovery Framework:**
```python
# Comprehensive disaster recovery system
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Optional
import time
import requests

class DisasterType(Enum):
    HARDWARE_FAILURE = "hardware_failure"
    DATA_CORRUPTION = "data_corruption"
    CYBER_ATTACK = "cyber_attack"
    NATURAL_DISASTER = "natural_disaster"
    HUMAN_ERROR = "human_error"

class RecoveryPriority(Enum):
    CRITICAL = 1    # RTO: 1 hour, RPO: 15 minutes
    HIGH = 2        # RTO: 4 hours, RPO: 1 hour
    MEDIUM = 3      # RTO: 24 hours, RPO: 4 hours
    LOW = 4         # RTO: 72 hours, RPO: 24 hours

@dataclass
class RecoveryObjective:
    rto_minutes: int  # Recovery Time Objective
    rpo_minutes: int  # Recovery Point Objective
    availability_target: float  # e.g., 99.9%

class DisasterRecoveryPlan:
    def __init__(self):
        self.recovery_objectives = {
            RecoveryPriority.CRITICAL: RecoveryObjective(60, 15, 99.95),
            RecoveryPriority.HIGH: RecoveryObjective(240, 60, 99.9),
            RecoveryPriority.MEDIUM: RecoveryObjective(1440, 240, 99.5),
            RecoveryPriority.LOW: RecoveryObjective(4320, 1440, 99.0)
        }
        
        self.system_priorities = {
            'database': RecoveryPriority.CRITICAL,
            'api_server': RecoveryPriority.CRITICAL,
            'web_frontend': RecoveryPriority.HIGH,
            'background_jobs': RecoveryPriority.MEDIUM,
            'analytics': RecoveryPriority.LOW
        }
        
        self.recovery_procedures = {}
        self.notification_channels = []
    
    def register_recovery_procedure(self, system: str, procedure):
        """Register recovery procedure for a system."""
        self.recovery_procedures[system] = procedure
    
    def initiate_disaster_recovery(self, disaster_type: DisasterType, affected_systems: List[str]):
        """Initiate disaster recovery process."""
        recovery_plan = {
            'disaster_id': self.generate_disaster_id(),
            'disaster_type': disaster_type,
            'affected_systems': affected_systems,
            'start_time': datetime.now(),
            'status': 'initiated',
            'recovery_steps': []
        }
        
        # Notify stakeholders
        self.notify_disaster_declared(recovery_plan)
        
        # Sort systems by priority
        prioritized_systems = sorted(
            affected_systems,
            key=lambda s: self.system_priorities.get(s, RecoveryPriority.LOW).value
        )
        
        # Execute recovery procedures
        for system in prioritized_systems:
            if system in self.recovery_procedures:
                step_result = self.execute_recovery_step(system, recovery_plan)
                recovery_plan['recovery_steps'].append(step_result)
        
        # Validate recovery
        recovery_plan['validation_results'] = self.validate_recovery(affected_systems)
        recovery_plan['end_time'] = datetime.now()
        recovery_plan['status'] = 'completed' if recovery_plan['validation_results']['success'] else 'failed'
        
        # Final notification
        self.notify_recovery_completed(recovery_plan)
        
        return recovery_plan
    
    def execute_recovery_step(self, system: str, recovery_plan: Dict) -> Dict:
        """Execute recovery procedure for a specific system."""
        procedure = self.recovery_procedures[system]
        priority = self.system_priorities.get(system, RecoveryPriority.LOW)
        objectives = self.recovery_objectives[priority]
        
        step_start = datetime.now()
        
        try:
            # Execute recovery procedure
            result = procedure.execute()
            
            step_end = datetime.now()
            recovery_time = (step_end - step_start).total_seconds() / 60  # minutes
            
            # Check if RTO was met
            rto_met = recovery_time <= objectives.rto_minutes
            
            return {
                'system': system,
                'priority': priority.name,
                'start_time': step_start,
                'end_time': step_end,
                'recovery_time_minutes': recovery_time,
                'rto_target_minutes': objectives.rto_minutes,
                'rto_met': rto_met,
                'success': result.get('success', False),
                'details': result
            }
            
        except Exception as e:
            return {
                'system': system,
                'priority': priority.name,
                'start_time': step_start,
                'end_time': datetime.now(),
                'success': False,
                'error': str(e)
            }
    
    def validate_recovery(self, systems: List[str]) -> Dict:
        """Validate that recovered systems are functioning correctly."""
        validation_results = {
            'success': True,
            'system_status': {},
            'failed_validations': []
        }
        
        for system in systems:
            try:
                status = self.validate_system_health(system)
                validation_results['system_status'][system] = status
                
                if not status['healthy']:
                    validation_results['success'] = False
                    validation_results['failed_validations'].append(system)
                    
            except Exception as e:
                validation_results['success'] = False
                validation_results['system_status'][system] = {
                    'healthy': False,
                    'error': str(e)
                }
                validation_results['failed_validations'].append(system)
        
        return validation_results
    
    def validate_system_health(self, system: str) -> Dict:
        """Validate individual system health."""
        health_checks = {
            'database': self.check_database_health,
            'api_server': self.check_api_health,
            'web_frontend': self.check_frontend_health
        }
        
        if system in health_checks:
            return health_checks[system]()
        
        return {'healthy': True, 'message': 'No specific health check available'}
    
    def check_database_health(self) -> Dict:
        """Check database connectivity and basic operations."""
        try:
            from django.db import connection
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                
                if result and result[0] == 1:
                    # Test a basic query
                    cursor.execute("SELECT COUNT(*) FROM customers LIMIT 1")
                    cursor.fetchone()
                    
                    return {
                        'healthy': True,
                        'message': 'Database is responding and accessible'
                    }
                else:
                    return {
                        'healthy': False,
                        'message': 'Database query returned unexpected result'
                    }
                    
        except Exception as e:
            return {
                'healthy': False,
                'message': f'Database health check failed: {str(e)}'
            }
    
    def check_api_health(self) -> Dict:
        """Check API server health."""
        try:
            response = requests.get('http://localhost:8000/api/health/', timeout=10)
            
            if response.status_code == 200:
                return {
                    'healthy': True,
                    'message': 'API server is responding',
                    'response_time': response.elapsed.total_seconds()
                }
            else:
                return {
                    'healthy': False,
                    'message': f'API server returned status {response.status_code}'
                }
                
        except Exception as e:
            return {
                'healthy': False,
                'message': f'API health check failed: {str(e)}'
            }

class DatabaseRecoveryProcedure:
    def __init__(self, backup_strategy: BackupStrategy):
        self.backup_strategy = backup_strategy
    
    def execute(self) -> Dict:
        """Execute database recovery procedure."""
        try:
            # Find latest backup
            latest_backup = self.backup_strategy.get_latest_backup()
            
            if not latest_backup:
                return {
                    'success': False,
                    'message': 'No backup available for recovery'
                }
            
            # Restore from backup
            success = self.backup_strategy.restore_database(latest_backup['backup_id'])
            
            if success:
                return {
                    'success': True,
                    'message': f'Database restored from backup {latest_backup["backup_id"]}',
                    'backup_timestamp': latest_backup['timestamp']
                }
            else:
                return {
                    'success': False,
                    'message': 'Database restore failed'
                }
                
        except Exception as e:
            return {
                'success': False,
                'message': f'Database recovery failed: {str(e)}'
            }

# Initialize disaster recovery
dr_plan = DisasterRecoveryPlan()

# Register recovery procedures
dr_plan.register_recovery_procedure('database', DatabaseRecoveryProcedure(backup_strategy))
```

## 3. Data Compliance and Privacy

### 3.1 GDPR Compliance Framework

**GDPR Data Management:**
```python
# GDPR compliance implementation
from enum import Enum
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import hashlib
import json

class LegalBasis(Enum):
    CONSENT = "consent"
    CONTRACT = "contract"
    LEGAL_OBLIGATION = "legal_obligation"
    VITAL_INTERESTS = "vital_interests"
    PUBLIC_TASK = "public_task"
    LEGITIMATE_INTERESTS = "legitimate_interests"

class DataSubjectRights(Enum):
    ACCESS = "access"
    RECTIFICATION = "rectification"
    ERASURE = "erasure"
    RESTRICT_PROCESSING = "restrict_processing"
    DATA_PORTABILITY = "data_portability"
    OBJECT = "object"

@dataclass
class ConsentRecord:
    subject_id: str
    purpose: str
    legal_basis: LegalBasis
    consent_given: bool
    consent_timestamp: datetime
    consent_method: str  # web_form, email, phone, etc.
    consent_version: str
    withdrawal_timestamp: Optional[datetime] = None

class GDPRComplianceManager:
    def __init__(self):
        self.consent_records = {}
        self.processing_activities = {}
        self.data_retention_policies = {}
        self.audit_log = []
    
    def record_consent(self, consent: ConsentRecord):
        """Record data subject consent."""
        key = f"{consent.subject_id}_{consent.purpose}"
        self.consent_records[key] = consent
        
        # Audit log entry
        self.audit_log.append({
            'action': 'consent_recorded',
            'subject_id': consent.subject_id,
            'purpose': consent.purpose,
            'consent_given': consent.consent_given,
            'timestamp': datetime.now().isoformat()
        })
    
    def withdraw_consent(self, subject_id: str, purpose: str):
        """Process consent withdrawal."""
        key = f"{subject_id}_{purpose}"
        
        if key in self.consent_records:
            self.consent_records[key].consent_given = False
            self.consent_records[key].withdrawal_timestamp = datetime.now()
            
            # Trigger data processing restriction
            self.restrict_data_processing(subject_id, purpose)
            
            # Audit log entry
            self.audit_log.append({
                'action': 'consent_withdrawn',
                'subject_id': subject_id,
                'purpose': purpose,
                'timestamp': datetime.now().isoformat()
            })
    
    def handle_data_subject_request(self, request_type: DataSubjectRights, subject_id: str, details: Dict = None) -> Dict:
        """Handle data subject rights requests."""
        request_id = self.generate_request_id()
        
        handlers = {
            DataSubjectRights.ACCESS: self.handle_access_request,
            DataSubjectRights.RECTIFICATION: self.handle_rectification_request,
            DataSubjectRights.ERASURE: self.handle_erasure_request,
            DataSubjectRights.RESTRICT_PROCESSING: self.handle_restriction_request,
            DataSubjectRights.DATA_PORTABILITY: self.handle_portability_request,
            DataSubjectRights.OBJECT: self.handle_objection_request
        }
        
        try:
            handler = handlers.get(request_type)
            if handler:
                result = handler(subject_id, details or {})
                
                # Log the request
                self.audit_log.append({
                    'action': f'dsr_{request_type.value}',
                    'request_id': request_id,
                    'subject_id': subject_id,
                    'status': 'completed' if result.get('success') else 'failed',
                    'timestamp': datetime.now().isoformat()
                })
                
                return {
                    'request_id': request_id,
                    'type': request_type.value,
                    'subject_id': subject_id,
                    'status': 'completed' if result.get('success') else 'failed',
                    'result': result
                }
            else:
                return {
                    'request_id': request_id,
                    'error': f'Unsupported request type: {request_type.value}'
                }
                
        except Exception as e:
            self.audit_log.append({
                'action': f'dsr_{request_type.value}',
                'request_id': request_id,
                'subject_id': subject_id,
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            })
            
            return {
                'request_id': request_id,
                'error': f'Request processing failed: {str(e)}'
            }
    
    def handle_access_request(self, subject_id: str, details: Dict) -> Dict:
        """Handle right of access request."""
        try:
            # Collect all personal data for the subject
            personal_data = self.collect_personal_data(subject_id)
            
            # Include consent records
            consent_data = self.get_consent_records(subject_id)
            
            # Include processing activities
            processing_data = self.get_processing_activities(subject_id)
            
            return {
                'success': True,
                'data': {
                    'personal_data': personal_data,
                    'consent_records': consent_data,
                    'processing_activities': processing_data,
                    'export_timestamp': datetime.now().isoformat()
                }
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Access request failed: {str(e)}'
            }
    
    def handle_erasure_request(self, subject_id: str, details: Dict) -> Dict:
        """Handle right to erasure (right to be forgotten) request."""
        try:
            # Check if erasure is legally permissible
            if not self.can_erase_data(subject_id):
                return {
                    'success': False,
                    'reason': 'Erasure not permitted due to legal obligations'
                }
            
            # Anonymize or delete personal data
            deletion_results = self.anonymize_personal_data(subject_id)
            
            # Update consent records
            self.mark_subject_erased(subject_id)
            
            return {
                'success': True,
                'deleted_records': deletion_results,
                'erasure_timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Erasure request failed: {str(e)}'
            }
    
    def collect_personal_data(self, subject_id: str) -> Dict:
        """Collect all personal data for a data subject."""
        from django.apps import apps
        
        personal_data = {}
        
        # Get customer data
        try:
            Customer = apps.get_model('customers', 'Customer')
            customer = Customer.objects.get(id=subject_id)
            
            personal_data['customer_profile'] = {
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'email': customer.email,
                'phone': customer.phone,
                'created_at': customer.created_at.isoformat(),
                'is_active': customer.is_active
            }
            
            # Get related data (orders, addresses, etc.)
            if hasattr(customer, 'orders'):
                personal_data['orders'] = [
                    {
                        'id': order.id,
                        'date': order.created_at.isoformat(),
                        'total': str(order.total)
                    }
                    for order in customer.orders.all()
                ]
            
        except Exception as e:
            personal_data['error'] = f'Failed to collect customer data: {str(e)}'
        
        return personal_data
    
    def anonymize_personal_data(self, subject_id: str) -> Dict:
        """Anonymize personal data for a subject."""
        from django.apps import apps
        
        anonymization_results = {}
        
        try:
            Customer = apps.get_model('customers', 'Customer')
            customer = Customer.objects.get(id=subject_id)
            
            # Generate anonymous identifier
            anonymous_id = hashlib.sha256(f"anonymous_{subject_id}_{datetime.now()}".encode()).hexdigest()[:16]
            
            # Anonymize customer data
            customer.first_name = f"Anonymous_{anonymous_id}"
            customer.last_name = "User"
            customer.email = f"anonymous_{anonymous_id}@deleted.local"
            customer.phone = "000-000-0000"
            customer.is_active = False
            customer.save()
            
            anonymization_results['customer'] = {
                'original_id': subject_id,
                'anonymized': True,
                'anonymous_id': anonymous_id
            }
            
        except Exception as e:
            anonymization_results['error'] = f'Anonymization failed: {str(e)}'
        
        return anonymization_results
    
    def generate_compliance_report(self) -> Dict:
        """Generate GDPR compliance report."""
        return {
            'report_date': datetime.now().isoformat(),
            'consent_summary': self.get_consent_summary(),
            'data_subject_requests': self.get_dsr_summary(),
            'data_retention_compliance': self.check_retention_compliance(),
            'processing_activities': len(self.processing_activities),
            'audit_events': len(self.audit_log)
        }
    
    def get_consent_summary(self) -> Dict:
        """Get summary of consent records."""
        total_consents = len(self.consent_records)
        active_consents = sum(1 for c in self.consent_records.values() if c.consent_given)
        withdrawn_consents = total_consents - active_consents
        
        return {
            'total_consent_records': total_consents,
            'active_consents': active_consents,
            'withdrawn_consents': withdrawn_consents,
            'consent_rate': active_consents / max(total_consents, 1) * 100
        }

# Initialize GDPR compliance
gdpr_manager = GDPRComplianceManager()
```

---

**Document Version**: 1.0  
**Last Updated**: Current Date  
**Review Cycle**: Quarterly  
**Owner**: Data Management Team  
**Approval**: CDO