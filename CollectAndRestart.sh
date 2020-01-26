#!/bin/bash

echo "A colectar.."
	python3 manage.py collectstatic
echo "Colectado!"
echo "A reiniciar servidor..."
	service apache2 restart 
echo "Reiniciado!"
