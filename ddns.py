from common.log import info, error, trim_log_file
from aws.utils import update_dns_records
from common.consts import CHECK_INTERVAL
from ip.utils import get_public_ip, is_domain_ip_still_valid, is_valid_ip
import time

def update_dns_record_if_needed():
    public_ip = get_public_ip()
    info(f'Public IP: {public_ip}')
    valid_ip = is_valid_ip(public_ip)
    if not valid_ip:
        error('Failed to obtain a valid public IP.')
        return
    
    domain_ip_still_valid = is_domain_ip_still_valid(public_ip)
    if domain_ip_still_valid:
        info('Public IP has not changed. No update needed.')
    else:
        info(f'Updating domain IP to {public_ip}')
        update_dns_records(public_ip)

def main_loop():
    while True:
        update_dns_record_if_needed()
        trim_log_file()
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main_loop()