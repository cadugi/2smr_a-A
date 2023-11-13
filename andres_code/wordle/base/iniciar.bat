@echo off
setlocal

:: Comprobar si Colorama está instalado
pip show colorama >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando Colorama...
    pip install colorama
) else (
    echo Colorama ya está instalado.
)

:: Comprobar si IPython está instalado
pip show ipython >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando IPython...
    pip install ipython
) else (
    echo IPython ya está instalado.
)

:: Comprobar si tqdm está instalado
pip show tqdm >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando tqdm...
    pip install tqdm
) else (
    echo tqdm ya está instalado.
)

:: Comprobar si pyautogui está instalado
pip show pyautogui >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando pyautogui...
    pip install pyautogui
) else (
    echo pyautogui ya está instalado.
)

:: Ejecutar el archivo Python wordlev7.py
python /wordlev7.py

endlocal
