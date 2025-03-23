#!/usr/bin/env python3
import requests
import sys
import psutil
import json
from datetime import datetime

def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "timestamp": datetime.now().isoformat(),
        "cpu_usage_percent": cpu_percent,
        "memory_usage_percent": memory.percent,
        "disk_usage_percent": disk.percent,
        "memory_available_mb": round(memory.available / (1024 * 1024), 2),
        "disk_free_gb": round(disk.free / (1024 * 1024 * 1024), 2)
    }

def check_service_status(url):
    try:
        # Check main endpoint
        root_response = requests.get(url)
        health_response = requests.get(f"{url}/health")
        
        metrics = get_system_metrics()
        
        status = {
            "service": {
                "root_endpoint": {
                    "status_code": root_response.status_code,
                    "healthy": root_response.status_code == 200
                },
                "health_endpoint": {
                    "status_code": health_response.status_code,
                    "response": health_response.json(),
                    "healthy": health_response.status_code == 200
                }
            },
            "system_metrics": metrics
        }
        
        print(json.dumps(status, indent=2))
        
        # Return 0 if both endpoints are healthy
        if status["service"]["root_endpoint"]["healthy"] and status["service"]["health_endpoint"]["healthy"]:
            print("✅ All service endpoints are responding")
            return 0
        else:
            print("❌ Some service endpoints are not responding correctly")
            return 1
            
    except Exception as e:
        print(f"❌ Error checking service status: {str(e)}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python status_check.py <service_url>")
        sys.exit(1)
    
    service_url = sys.argv[1]
    sys.exit(check_service_status(service_url))
