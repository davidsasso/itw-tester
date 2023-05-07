@echo off
cmd /k "cd /d C:\DSV\test-engine\virtualenv\Scripts & activate & cd C:\DSV\test-engine\ui & pyuic5 gui.ui -o gui.py & exit"
