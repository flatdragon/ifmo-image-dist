#!/bin/bash

nc -u -p "$APP_LOGGER_PORT" -s "$HOSTNAME" -l
