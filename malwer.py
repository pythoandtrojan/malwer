import os
import sys
import time
import random
import socket
import platform
import webbrowser
from datetime import datetime
from urllib.request import urlopen
import json
import ctypes
import threading


FAKE_ENCRYPTION_COUNT = 0
MAX_FAKE_FILES = 500  
DELAY_PER_FILE = 0.01  


if platform.system() == 'Windows':
    os.system("color 0A")  
else:
    print("\033[1;31;40m") 



def get_public_ip():
    """Pega o IP público (não armazena, apenas exibe)"""
    try:
        response = urlopen('https://httpbin.org/ip')
        data = json.load(response)
        return data.get('origin', 'IP não encontrado')
    except:
        return "Erro ao obter IP"

def get_approximate_location(ip):
    """Pega localização aproximada (baseada em IP público)"""
    try:
        response = urlopen(f'http://ip-api.com/json/{ip}')
        data = json.load(response)
        return {
            'city': data.get('city', 'Desconhecida'),
            'region': data.get('regionName', 'Desconhecida'),
            'country': data.get('country', 'Desconhecido'),
            'isp': data.get('isp', 'Provedor desconhecido')
        }
    except:
        return {'city': 'Erro ao obter localização'}

def get_system_info():
    """Coleta informações do sistema (sem dados sensíveis)"""
    return {
        'username': os.getlogin(),
        'os': platform.system(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }



def fake_encryption_animation():
    """Mostra uma animação falsa de 'criptografia'"""
    global FAKE_ENCRYPTION_COUNT
    
    print("\n[!] SEUS ARQUIVOS ESTÃO SENDO CRIPTOGRAFADOS!")
    print("[!] NÃO DESLIGUE O COMPUTADOR!\n")
    
    for i in range(1, MAX_FAKE_FILES + 1):
        fake_file = f"C:\\Users\\{os.getlogin()}\\Documents\\file_{i}.txt"
        print(f"[🔒] Criptografando: {fake_file}")
        time.sleep(DELAY_PER_FILE)
        FAKE_ENCRYPTION_COUNT += 1
    
    print("\n[⚠️] TODOS OS SEUS ARQUIVOS FORAM BLOQUEADOS!")

def show_fake_ransom_note():
    
    ip = get_public_ip()
    location = get_approximate_location(ip)
    system_info = get_system_info()
    
    ransom_note = f"""
    ⚠️⚠️⚠️ VOCÊ FOI HACKEADO! ⚠️⚠️⚠️

    SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!
    {FAKE_ENCRYPTION_COUNT} ARQUIVOS BLOQUEADOS!

    -------------------------------
    🔍 INFORMAÇÕES COLETADAS:
    - IP: {ip}
    - Cidade: {location.get('city')}
    - Estado: {location.get('region')}
    - País: {location.get('country')}
    - Provedor: {location.get('isp')}
    - Usuário: {system_info['username']}
    - Sistema: {system_info['os']}
    - Horário do Ataque: {system_info['time']}
    -------------------------------


    (Este é um script de conscientização sobre segurança)
    """
    
    print(ransom_note)
    time.sleep(5)
    
   
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  



def fake_virus_menu():
    """Menu fake que simula um vírus (sem danos reais)"""
    print("""
    ██████╗ ███████╗██╗  ██╗██████╗ ███████╗
    ██╔══██╗██╔════╝██║  ██║██╔══██╗██╔════╝
    ██████╔╝█████╗  ███████║██████╔╝███████╗
    ██╔══██╗██╔══╝  ██╔══██║██╔══██╗╚════██║
    ██║  ██║███████╗██║  ██║██║  ██║███████║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    [FAKE VIRUS SIMULATOR - APENAS PARA TESTES]
    """)
    
    input("Pressione ENTER para 'iniciar o ataque'...")
    

    fake_encryption_animation()
    
   
    show_fake_ransom_note()
    
   
    print("\n[✅] FIM DA SIMULAÇÃO. SEUS ARQUIVOS ESTÃO SEGUROS!")
    input("Pressione ENTER para sair...")



if __name__ == "__main__":
    fake_virus_menu()
