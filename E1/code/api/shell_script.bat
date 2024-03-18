@echo off

rem Activer venv api
call D:\vscode\files\Rendus_Ecole_Simplon\PCO\E1\code\api\venv_api\Scripts\activate.bat

rem Lancer api dans un terminal
start  cmd /k "python api.py"

sleep 4

rem Lancer tracker
start  cmd /k "python tracking.py"

rem Activer venv appli
call D:\vscode\files\Rendus_Ecole_Simplon\PCO\E1\code\app\venv_app\Scripts\activate.bat

rem lancer appli
cd ../app
start cmd /k "streamlit run app.py "
