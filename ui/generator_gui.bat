@echo off
cmd /k "cd /d C:\ITW\itw-tester\virtualenv\Scripts & activate & cd C:\ITW\itw-tester\ui & pyuic5 gui.ui -o gui.py & cd C:\ITW\itw-tester\resources & pyrcc5 resources.qrc -o resources.py & exit"
