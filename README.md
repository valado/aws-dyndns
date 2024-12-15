# DDNS

DynamicDNS for self-hosting using AWS.

## AWS policy needed

The AWS generated user credentials should be allowed to access the following functions of Route53. The access should also be limited to a resource (hosted zone).

```
ChangeResourceRecordSets
ListResourceRecordSets
```

## Following environment variables are necessary

`ACCESS_KEY`
`SECRET_KEY`
`ZONE_ID`
`DOMAIN`
`IP_TOKEN`
`CHECK_INTERVAL`

## Example docker compose file

```
version: "3"

services:
  ddns:
    container_name: ddns
    image: thevlad/ddns:latest
    restart: unless-stopped
    environment:
      - ACCESS_KEY=<ACCESS_KEY>
      - SECRET_KEY=<SECRET_KEY>
      - ZONE_ID=<ZONE_ID>
      - DOMAIN=ddns.example.com
      - IP_TOKEN=<TOKEN for https://ipinfo.io>
      - CHECK_INTERVAL=300
```
