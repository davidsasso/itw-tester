@echo off
cmd /k "cd /d C:\DSV\test-engine\virtualenv\Scripts & activate & cd C:\DSV\test-engine\ui & pyuic5 main_window.ui -o main_window.py & exit"
