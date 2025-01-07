# AWS-DynDNS

AWS-DynDNS for self-hosting using AWS.

## AWS policy needed

The AWS generated user credentials should be allowed to access the following functions of Route53. The access should also be limited to a resource (hosted zone).

```
ChangeResourceRecordSets
ListResourceRecordSets
```

## Following environment variables are necessary

- `AWS_ACCESS_KEY_ID` - AWS access key id
- `AWS_SECRET_ACCESS_KEY` - AWS access secret key
- `ZONE_ID` - Which hosted zone should be updated
- `DOMAIN` - Which domain should be updated with an `A` record-set
- `IP_TOKEN` - Token for [ipinfo](https://ipinfo.io) fetching the current IPv4
- `CHECK_INTERVAL` - How often to check the IP and update if changed (in seconds)

## Example docker compose file

```
version: "3"

services:
  ddns:
    container_name: ddns
    image: thevlad/aws-dyndns:latest
    restart: unless-stopped
    environment:
      - AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
      - AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
      - ZONE_ID=<ZONE_ID>
      - DOMAIN=ddns.example.com
      - IP_TOKEN=<TOKEN for https://ipinfo.io>
      - CHECK_INTERVAL=300
```
