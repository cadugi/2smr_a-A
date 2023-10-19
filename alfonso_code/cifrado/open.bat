@echo off
setlocal

REM Verificar si pip está instalado
python -m ensurepip --default-pip

REM Instalar pyperclip si no está instalado
python -c "import pyperclip" || (
    echo Instalando pyperclip...
    pip install pyperclip
)

REM Abrir cesar.py
if exist cesar.py (
    echo Abriendo cesar.py...
    start "" cesar.py
) else (
    echo El archivo cesar.py no se encuentra en el directorio actual.
)

pause
