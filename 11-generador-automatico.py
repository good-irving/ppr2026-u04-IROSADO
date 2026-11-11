import ipaddress
from pathlib import Path

dispositivos = [
    {"nombre": "Router01", "interfaz": "G0/0", "ip": "192.168.1.1", "mascara": "255.255.255.0"},
    {"nombre": "Router02", "interfaz": "G0/0", "ip": "192.168.2.1", "mascara": "255.255.255.0"},
    {"nombre": "SwitchCore", "interfaz": "VLAN10", "ip": "192.168.10.2", "mascara": "255.255.255.0"},
    {"nombre": "FirewallEdge", "interfaz": "G0/1", "ip": "10.0.0.256", "mascara": "255.0.0.0"},
    {"nombre": "ServidorDNS", "interfaz": "Eth0", "ip": "192.168.2.1", "mascara": "255.255.255.0"},
    {"nombre": "AccessPoint01", "interfaz": "BVI1", "ip": "172.16.5.10", "mascara": "255.255.0.0"},
    {"nombre": "RouterBranch", "interfaz": "S0/0/0", "ip": "192.168.100.999", "mascara": "255.255.255.0"},
    {"nombre": "ServidorSQL", "interfaz": "Eth1", "ip": "192.168.20.15", "mascara": "255.255.255.0"},
    {"nombre": "SwitchAccess", "interfaz": "VLAN1", "ip": "192.168.1.254", "mascara": "255.255.255.0"},
    {"nombre": "GatewayVoz", "interfaz": "G0/2", "ip": "172.16.1.1", "mascara": "255.255.255.128"}
]

# CREAR LA CARPETA
carpeta = Path("configuraciones 4")
carpeta.mkdir(exist_ok=True)

ips_registradas = []

ips_validas = 0
ips_novalidas = 0
ips_duplicadas = 0

for dispositivo in dispositivos:
    ip = dispositivo["ip"]
    nombre = dispositivo["nombre"]

    # MANEJO DE EXCEPCIONES
    try: 
        ipaddress.ip_address(ip)

        if ip in ips_registradas:
            print(nombre, "-", ip, "DIRECCIÓN DUPLICADA")
            ips_duplicadas += 1
        else:
            print(nombre, "-", ip, "DIRECCIÓN IP VÁLIDA")
            ips_registradas.append(ip)
            ips_validas += 1
            
            
            configuracion = '''
hostname {dispositivo["nombre"]}

interface {dispositivo["interfaz"]}
 ip address {dispositivo["ip"]} {dispositivo["mascara"]}
 no shutdown

end
'''
            archivo = carpeta / f'{dispositivo["nombre"]}.txt'
            archivo.write_text(configuracion, encoding="utf-8")

    except ValueError:
        print(nombre, "-", ip, "DIRECCIÓN IP INVÁLIDA")
        ips_novalidas += 1

print("\n--- Resultados ---")
print("Válidas:", ips_validas)
print("No válidas:", ips_novalidas)
print("Duplicadas:", ips_duplicadas)