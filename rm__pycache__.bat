




::@echo off
cd "C:\Users\Tyler\pythonstuff\tool"
FOR /d /r . %%G IN (__pycache__) DO @IF EXIST "%%G" rd /s /q "%%G"
pause