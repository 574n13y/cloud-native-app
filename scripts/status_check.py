#!/usr/bin/env python3
import requests
import sys
import psutil
import json
from datetime import datetime
from urllib.parse import urlparse

def validate_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def get_system_metrics():
    try:
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
    except Exception as e:
        return {
            "timestamp": datetime.now().isoformat(),
            "error": f"Failed to get system metrics: {str(e)}"
        }

def check_endpoint(url, endpoint=""):
    try:
        full_url = f"{url.rstrip('/')}/{endpoint.lstrip('/')}"
        response = requests.get(full_url, timeout=10)
        return {
            "url": full_url,
            "status_code": response.status_code,
            "healthy": response.status_code == 200,
            "response_time_ms": round(response.elapsed.total_seconds() * 1000, 2)
        }
    except requests.RequestException as e:
        return {
            "url": full_url,
            "status_code": None,
            "healthy": False,
            "error": str(e)
        }

def check_service_status(url):
    if not validate_url(url):
        status = {
            "error": f"Invalid URL provided: {url}",
            "timestamp": datetime.now().isoformat()
        }
        print(json.dumps(status, indent=2))
        return 1

    metrics = get_system_metrics()
    
    root_status = check_endpoint(url)
    health_status = check_endpoint(url, "health")
    
    status = {
        "timestamp": datetime.now().isoformat(),
        "service": {
            "root_endpoint": root_status,
            "health_endpoint": health_status
        },
        "system_metrics": metrics
    }
    
    print(json.dumps(status, indent=2))
    
    # Return success only if both endpoints are healthy
    if root_status["healthy"] and health_status["healthy"]:
        print("\n✅ All service endpoints are responding")
        return 0
    else:
        print("\n❌ Some service endpoints are not responding correctly")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python status_check.py <service_url>")
        sys.exit(1)
    
    service_url = sys.argv[1]
    sys.exit(check_service_status(service_url))
