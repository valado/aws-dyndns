import os
from pathlib import Path

DOMAIN = os.environ.get('DOMAIN')
IP_URL = 'https://ipinfo.io/ip'
IP_TOKEN = os.environ.get('IP_TOKEN')
TIMEOUT = 5
CHECK_INTERVAL = os.environ.get('CHECK_INTERVAL')
LOG_FILE_PATH = Path.home() / './ddns.log'
AWS_CONFIG = {
    'aws_credentials': {
        'access_key': os.environ.get('ACCESS_KEY'),
        'secret_key': os.environ.get('SECRET_KEY')
    },
    'zone_id': os.environ.get('ZONE_ID'),
    'records': [
        {
            'name': DOMAIN,
            'type': 'A',
            'ttl': 300
        }
    ]
}
