## Development

### Build & Up
```
sudo docker-compose --env-file .dev.env up --build
```

### Force Rebuild
```
sudo docker-compose --env-file .dev.env up --build --force-recreate
```

## Production

### Build & Up
```
sudo docker-compose up --build
```

### Force Rebuild

```
sudo docker-compose up --build --force-recreate
```

### Monitor uWSGI Resources
```
# For Default App Container Name
bash ./top.sh ifmo-image-dist_app_1

# For Custom App Container name
bash ./top.sh {continer_hash or container_name}
```

### Monitor uWSGI Logs
```
# For Default App Container Name
bash ./logs.sh ifmo-image-dist_app_1

# For Custom App Container name
bash ./logs.sh {continer_hash or container_name}
```