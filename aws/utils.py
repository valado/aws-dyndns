from logging import info, error
import boto3, time

from common.consts import AWS_CONFIG

def update_dns_records(public_ip):
    route53 = boto3.client(
        'route53',
        aws_access_key_id=AWS_CONFIG['aws_credentials']['access_key'],
        aws_secret_access_key=AWS_CONFIG['aws_credentials']['secret_key']
    )
    for record in AWS_CONFIG['records']:
        try:
            response = route53.change_resource_record_sets(
                HostedZoneId=AWS_CONFIG['zone_id'],
                ChangeBatch={
                    'Comment': 'Update via DDNS Script',
                    'Changes': [{
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': record['name'],
                            'Type': record['type'],
                            'TTL': record['ttl'],
                            'ResourceRecords': [{'Value': public_ip}]
                        }
                    }]
                }
            )
            info(f"Updated DNS record for {record['name']} to {public_ip}. Response: {response['ChangeInfo']['Status']}")
            # Check if DNS record is updated
            time.sleep(5)
            if not check_dns_record_update(route53, AWS_CONFIG['zone_id'], record['name'], public_ip):
                error(f"DNS record for {record['name']} not updated to {public_ip} yet.")
            else:
                info(f"DNS record for {record['name']} successfully updated to {public_ip}.")  

        except Exception as e:
            error(f"Failed to update DNS record for {record['name']}: {e}")

def check_dns_record_update(route53, hosted_zone_id, record_name, expected_ip):
    try:
        response = route53.list_resource_record_sets(HostedZoneId=hosted_zone_id)
        for record_set in response['ResourceRecordSets']:
            if record_set['Name'] == record_name + '.' and record_set['Type'] == 'A':
                current_ip = record_set['ResourceRecords'][0]['Value']
                return current_ip == expected_ip
    except Exception as e:
        error(f"Error checking DNS record update for {record_name}: {e}")
    return False