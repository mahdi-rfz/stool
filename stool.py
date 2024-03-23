import time
import os
import socket
import sys
import datetime
import getpass
import json
import requests

def all():
    def clear_screen():  # for clear screen in terminal on linux and windows
        if os.name == "nt" :
            os.system("cls")
        else :
            os.system("clear")

    def check_internet_connection():
        log_action("Check-internet-connection" , "216.239.38.120" , "80" , "None")
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            return False
        
    def server_status(ip, port , userName):
        log_action("Check-server-staxtus" , ip , port , userName)
        try:
            sock = socket.create_connection((ip, port), timeout=1)
            sock.close()
            return ("Up")
        except (socket.timeout, ConnectionRefusedError):
            return ("Down")
    
    def server_location(ip):
        try :
            request_url = 'https://geolocation-db.com/jsonp/' + ip
            response = requests.get(request_url)
            result = response.content.decode()
            result = result.split("(")[1].strip(")")
            result  = json.loads(result)
            return result["country_name"]
        except OSError :
            return " Not found"
        
    def log_action(action , ip , port , username):
        if os.name == "nt":
            try :
                os.chdir("c:/stool")
            except OSError :
                os.chdir("c:/")
                os.mkdir("stool")
                os.chdir("c:/stool")
        else :
            linuxuser = getpass.getuser()
            try :
                os.chdir(f"/home/{linuxuser}/stool")
            except FileNotFoundError :
                os.chdir(f"/home/{linuxuser}")
                os.mkdir("stool")
                os.chdir(f"/home/{linuxuser}/stool")
        
        file = open("stool-log.txt" , "a")
        
        today = datetime.date.today()
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        
        file.write(f"{today} {current_time} {action} ip<{ip}> , port<{port}> , username<{username}>\n")
        file.close()
                
    def connect_server (ip , port , username):    #ssh connection (secure shell)
        log_action("SSH-Connection" , ip , port , userName)
        os.system(f"ssh {username}@{ip} -p{port}")

    def download_server () :
        serverFile = input("Enter server file address :")
        localFile = input("Enter local file to save :")
        log_action("SCP-Download" , ip , port , userName)
        os.system(f"scp -P{port} {userName}@{ip}:{serverFile} {localFile} ")
        log_action("Download-compelet" , ip , port , userName)

    def upload_server (ip , port , userName , localFile , serverFile) :
        localFile = input("Enter local file address :")
        serverFile = input("Enter server file to save :")
        log_action("SCP-Upload" , ip , port , userName)
        os.system(f"scp {localFile} {userName}@{ip}:{serverFile} -P{port}")
        log_action("Upload-compelet" , ip , port , userName)
        
    clear_screen()
    ip = input("Enter ip (V4) :")
    port = input("Enter port (press Enter for default(22)) :").strip() or "22"  #for custom port 
    userName = input("Enter username :")
    
    internet_status = check_internet_connection()
    if bool(ip) == True :
        server_s = server_status(ip , port , userName)
        server_loc = server_location(ip)
    elif bool(ip) == False :
        server_s = ("Information not entered")
        server_loc = ("Information not entered")
    while True :
        clear_screen()
        time.sleep(0.3)
        clear_screen()
        
        print("""
░██████╗████████╗░█████╗░░█████╗░██╗░░░░░
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
╚█████╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░
░╚═══██╗░░░██║░░░██║░░██║██║░░██║██║░░░░░
██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝""")
        print("=========================================")
        print(f"Server location :{server_loc}")
        print(f"Server status : {server_s}")
        print("=========================================")
        print(f"IP:{ip} ,Port:{port} ,Username:{userName}")
        print("=========================================")
        print("Menu:")
        print("[1] - Connect to server")
        print("[2] - Download from server")
        print("[3] - Upload file to server")
        print("[4] - Connect with new IP")
        print("[5] - Server tool Guid")
        print("[6] - Exit")
        
        choice = input("Enter your choice >>>")    
        if choice == "1"  or choice == "one"  and internet_status == True:
                connect_server(ip, port, userName)
                
        elif choice == "1" or choice == "one" and internet_status == False :
            print("Internet connection is not established")
            input("Press enter to continu")
            
        elif choice == "2" or choice == "two":
            download_server()
            
        elif choice == "2" or choice == "two" and internet_status == False :
            print("Internet connection is not established")
            input("Press enter to continu")
            
        elif choice == "3":
            upload_server(ip, port, userName)
            
        elif choice == "3" or choice == "three" and internet_status == False :
            print("Internet connection is not established")
            input("Press enter to continu")
            
        elif choice == "4" or choice == "four" or choice == "newip" :
            all()
        
        elif choice == "5" or choice == "guid" or choice == "five" :
            print()
            print("=========================================")
            print("Hello welcome to server tool") 
            print("Contact us:")
            print("Github :https://github.com/mahdi-fyz")
            print("=========================================")
            print("● server tool options :")
            print("-Save log file :")
            print(" |  linux :/home/yourusername/stool/stool-log.txt")
            print(" |  windows :c:/stool/stool-log.txt")
            print("-Show server location")
            print(" |  <https://geolocation-db.com/>")
            print("-Check server status")
            print("-Check internet connection")
            print(" |  <www.google.com> , port<80>")
            print("=========================================")
            print()
            input("Press enter to continu")
        elif choice == "6" or choice == "exit" or choice == "six":
            print("Exiting...")
            time.sleep(1)
            clear_screen()
            sys.exit()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(0.5)
            input("Press enter to continu")
all()