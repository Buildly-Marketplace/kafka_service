#!/bin/bash

# It is responsability of the deployment orchestration to execute before
# migrations, create default admin user, populate minimal data, etc.

gunicorn kafka_config.wsgi --config kafka_config/gunicorn_conf.py
