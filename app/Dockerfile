FROM python:3.9-alpine

ARG APP_SECRET_KEY
ARG APP_ENV
ARG APP_PORT
ARG APP_STATS_PORT
ARG APP_LOGGER_PORT
ARG APP_PATH

ENV APP_SECRET_KEY=$APP_SECRET_KEY
ENV APP_ENV=$APP_ENV
ENV APP_PORT=$APP_PORT
ENV APP_STATS_PORT=$APP_STATS_PORT
ENV APP_LOGGER_PORT=$APP_LOGGER_PORT
ENV APP_PATH=$APP_PATH

RUN addgroup -S uwsgi-group && adduser -S uwsgi-user -G uwsgi-group

RUN apk add --no-cache gcc libc-dev linux-headers dos2unix bash

WORKDIR $APP_PATH

COPY ./requirements.txt .

COPY ./serve.sh .

COPY ./logs.sh .

RUN dos2unix ./serve.sh

RUN dos2unix ./logs.sh

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE $APP_PORT $APP_STATS_PORT $APP_LOGGER_PORT

USER uwsgi-user

ENTRYPOINT ["./serve.sh"]