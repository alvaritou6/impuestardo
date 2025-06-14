from time import sleep
import requests
import os
import json

# obtención de la cotización actual del dolar
response = requests.get('https://api.bluelytics.com.ar/v2/latest').text
json_dls = json.loads(response)
dls_oficial = json_dls["oficial"]
dolar = dls_oficial["value_sell"]

# creación de las variables para un control más efectivo de los impuestos
imp_iva = 21
imp_ganancias = 30

# bienvenida a la app al usuario
print("""
 ██▓ ███▄ ▄███▓ ██▓███   █    ██ ▓█████   ██████ ▄▄▄█████▓ ▄▄▄       ██▀███  ▓█████▄  ▒█████  
▓██▒▓██▒▀█▀ ██▒▓██░  ██▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▒██▒  ██▒
▒██▒▓██    ▓██░▓██░ ██▓▒▓██  ▒██░▒███   ░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌▒██░  ██▒
░██░▒██    ▒██ ▒██▄█▓▒ ▒▓▓█  ░██░▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌▒██   ██░
░██░▒██▒   ░██▒▒██▒ ░  ░▒▒█████▓ ░▒████▒▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ░ ████▓▒░
░▓  ░ ▒░   ░  ░▒▓▒░ ░  ░░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▒░▒░ 
 ▒ ░░  ░      ░░▒ ░     ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░    ░      ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░ 
 ▒ ░░      ░   ░░        ░░░ ░ ░    ░   ░  ░  ░    ░        ░   ▒     ░░   ░  ░ ░  ░ ░ ░ ░ ▒  
 ░         ░               ░        ░  ░      ░                 ░  ░   ░        ░        ░ ░  
                                                                              ░               
""")
print('\n\n\nCargando app...')
sleep(2)
os.system("cls")

# calculo en pesos
def pesos(val_pesos):
    if game == 'n':
        if val_pesos.isdigit() == True:
            val_pesos = float(val_pesos)
            iva = val_pesos*imp_iva/100
            print(f'IVA (21%): {iva}')
            ganancias = val_pesos*imp_ganancias/100
            print(f'Ganancias (30%): {ganancias}')
            print(f'\nSin impuestos: {val_pesos}')
            print(f'Total con impuestos: {val_pesos+iva+ganancias}')
        elif val_pesos == 'EXIT':
            sleep(1)
            exit()
        elif val_pesos == 'DLS':
            val_dls = input('\n\nIngrese el importe en dolares a cacular impuestos: ')
            dolares(val_dls)
        else:
            print('Error! Escribe un valor válido')
    elif game == 'y':
        if val_pesos.isdigit() == True:
            val_pesos = float(val_pesos)
            iva = val_pesos*imp_iva/100
            print(f'IVA (21%): {iva}')
            print(f'\nSin impuestos: {val_pesos}')
            print(f'Total con impuestos: {val_pesos+iva}')
        elif val_pesos == 'EXIT':
            sleep(1)
            exit()
        elif val_pesos == 'DLS':
            val_dls = input('\n\nIngrese el importe en dolares a cacular impuestos: ')
            dolares(val_dls)
        else:
            print('Error! Escribe un valor válido')
    else:
        print('No has seleccionado una opción válida.')
        exit()

# calculo en dolares
def dolares(val_dls):
    if game == 'n':
        if val_dls.isdigit() == True:
            val_dls = float(val_dls)
            val_simp = val_dls*dolar
            iva = val_simp*imp_iva/100
            print(f'IVA (21%): {iva}')
            ganancias = val_simp*imp_ganancias/100
            print(f'Ganancias (30%): {ganancias}')
            print(f'\nSin impuestos: {val_simp}')
            print(f'Total con impuestos: {val_simp+iva+ganancias}')
            print(f'\nCotización del dolar: {dolar}')
        elif val_dls == 'EXIT':
            sleep(1)
            exit()
        elif val_dls == 'ARS':
            val_pesos = input('\n\nIngrese el importe a calcular impuestos: ')
            pesos(val_pesos)
        else:
            print('Error! Escribe un valor válido')
    elif game == 'y':
        if val_dls.isdigit() == True:
            val_dls = float(val_dls)
            val_simp = val_dls*dolar
            iva = val_simp*imp_iva/100
            print(f'IVA (21%): {iva}')
            print(f'\nSin impuestos: {val_simp}')
            print(f'Total con impuestos: {val_simp+iva}')
            print(f'\nCotización del dolar: {dolar}')
        elif val_dls == 'EXIT':
            sleep(1)
            exit()
        elif val_dls == 'ARS':
            val_pesos = input('\n\nIngrese el importe a calcular impuestos: ')
            pesos(val_pesos)
        else:
            print('Error! Escribe un valor válido')
    else:
        print('No has escrito un valor valido.')
        exit()

# elección entre calcular en pesos o dolares
print('Porfavor elige si quieres calcular impuestos en pesos (ARS) o en dolares (DLS). \nEn el caso elegido escribe TAL CUAL la palabra que está entre parentesis para seguir.')
print('\nEscriba EXIT para salir del programa.')
moneda = input('\n--> ')

# elección entre juego o app comun
print('¿Quieres calcular los impuestos de un juego? (y/n): ')
game = input()

print('\nSi desea intercambiar entre monedas solamente vuelva a escribir el nombre de la otra moneda TAL CUAL se encuentre entre parentesis.')
while True:
    # confección del cálculo en pesos
    if moneda == 'ARS':
        val_pesos = input('\n\nIngrese el importe a calcular impuestos: ')
        pesos(val_pesos)
    # confección del cálculo en dolares
    if moneda == 'DLS':
        val_dls = input('\n\nIngrese el importe en dolares a cacular impuestos: ')
        dolares(val_dls)
    if moneda == 'EXIT':
        sleep(1)
        exit()
