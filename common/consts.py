import os
from pathlib import Path

DOMAIN = os.environ.get('DOMAIN')
IP_URL = 'https://ipinfo.io/ip'
IP_TOKEN = os.environ.get('IP_TOKEN')
TIMEOUT = 5
CHECK_INTERVAL = int(os.environ.get('CHECK_INTERVAL'))
LOG_FILE_PATH = Path.home() / './ddns.log'
AWS_CONFIG = {
    'aws_credentials': {
        'aws_access_key_id': os.environ.get('AWS_ACCESS_KEY_ID'),
        'aws_secret_access_key': os.environ.get('AWS_SECRET_ACCESS_KEY')
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
