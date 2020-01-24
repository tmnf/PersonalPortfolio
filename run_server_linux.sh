#!/bin/bash
#Iniciar o Servidor em HTTP

echo "A ligar servidor!"
python3 manage.py 0.0.0.0:80 >> log.txt