@echo off
cmd /k "cd /d C:\ITW\itw-tester\virtualenv\Scripts & activate & cd C:\ITW\itw-tester & pyinstaller --distpath "C:\ITW\itw-tester-release\deploy" --onedir --windowed --noconfirm --add-data "engine/settings;engine/settings" application.py --name Tester & pause & exit"
