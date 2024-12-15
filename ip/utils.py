import requests
import ipaddress
import subprocess

from common.consts import DOMAIN, IP_TOKEN, IP_URL, TIMEOUT

def get_public_ip():
    response = requests.get(IP_URL, timeout=TIMEOUT, headers={'Authorization': f'TOK:{IP_TOKEN}'})
    ip = response.text.strip()
    if is_valid_ip(ip):
        return ip
    return None
    
def is_valid_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def get_domain_ip():
    result = subprocess.run(['dig', DOMAIN, 'any'], stdout=subprocess.PIPE)
    return result.stdout

def is_domain_ip_still_valid(ip):
    return ip.encode() in get_domain_ip()
