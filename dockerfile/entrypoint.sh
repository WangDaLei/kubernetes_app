#!/bin/bash

cd /kubernetes_app/k8s
export PATH=/root/anaconda3/bin:$PATH
python manage.py runserver 0.0.0.0:8000
