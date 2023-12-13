#!/bin/bash
echo "-> Instalando entorno virtual"
python3 -m venv .venv
echo "->Activando entorno virtual"
source .venv/bin/activate
echo "-> Instalando dependencias"
pip3 install -r requirements.txt
echo "-> Deactivando entorno virtual"
deactivate
echo "Proceso terminado"

