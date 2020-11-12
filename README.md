# Monster Avatar App Using Docker

## Author
Kochetygov Andrew

## Installation
```shell script
git clone https://github.com/flatdragon/ifmo-image-dist.git
```

## Development

### Build & Up
```shell script
sudo docker-compose --env-file .dev.env up --build
```

### Force Rebuild
```shell script
sudo docker-compose --env-file .dev.env up --build --force-recreate
```

## Production

### Build & Up
```shell script
sudo docker-compose up --build
```

### Force Rebuild

```shell script
sudo docker-compose up --build --force-recreate
```

### Monitor uWSGI Resources
```shell script
# For Default App Container Name
bash ./top.sh ifmo-image-dist_app_1

# For Custom App Container name
bash ./top.sh {continer_hash or container_name}
```

### Monitor uWSGI Logs
```shell script
# For Default App Container Name
bash ./logs.sh ifmo-image-dist_app_1

# For Custom App Container name
bash ./logs.sh {continer_hash or container_name}
```
