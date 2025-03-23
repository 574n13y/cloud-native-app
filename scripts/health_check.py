#!/usr/bin/env python3
import requests
import sys
from datetime import datetime

def check_health(url):
    try:
        response = requests.get(f"{url}/health")
        health_data = response.json()
        
        print(f"[{datetime.now().isoformat()}] Health Check Results:")
        print(f"Status Code: {response.status_code}")
        print(f"Status: {health_data.get('status', 'unknown')}")
        print(f"Version: {health_data.get('version', 'unknown')}")
        
        if response.status_code == 200 and health_data.get('status') == 'healthy':
            print("✅ Service is healthy")
            return 0
        else:
            print("❌ Service is unhealthy")
            return 1
    except Exception as e:
        print(f"❌ Error checking health: {str(e)}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python health_check.py <service_url>")
        sys.exit(1)
    
    service_url = sys.argv[1]
    sys.exit(check_health(service_url))
