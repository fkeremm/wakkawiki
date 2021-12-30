import os
import time

os.system("apt install git")
os.system("apt install python python2 -y")
os.system("pkg install termux-api")
os.system("clear")
os.system("figlet WakkaWiki")
os.system("termux-tts-speak -l tr Merhaba ben furkanın tooluyum senin için wakka wiki açıklı siteler bulacağım")
os.system("termux-tts-speak -l tr siteler bulununca sana bildirim yollayacağım")
os.chdir("/data/data/com.termux/files/home/sqlmap/")
os.system("python2 sqlmap.py -g inurl:?PagePrincipale --batch")
time.sleep(40)
os.system("termux-notification -t Siteler bulundu")
