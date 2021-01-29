import requests
from dataclasses import dataclass
import os

def push_to_airtable(email=None, api_key=None, base_id=None, table_name=None):
    if email is None:
        return False
    
    else:
        # API endpoint
        endpoint = f'https://api.airtable.com/v0/{base_id}/{table_name}'

        # Headers
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Payload
        data = {
            "records": [
                {
                    "fields": {
                        "email": email
                    }
                },
            ],
        }

        r = requests.post(endpoint, headers=headers, json=data)
        
        print(endpoint, r.json())

        return r.status_code == 200