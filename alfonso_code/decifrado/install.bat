@echo off
REM Verificar si NLTK está instalado
python -c "import nltk" 2>nul
if %errorlevel% neq 0 (
    echo NLTK no está instalado. Instalando NLTK...
    pip install nltk
)

REM Ejecutar base.py
python base.py
