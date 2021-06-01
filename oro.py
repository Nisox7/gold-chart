import shutil
import requests
from bs4 import BeautifulSoup

def oro():
    print('''\nGRAFICO DEL ORO
ORO en ONZA (oz) O KILO (kg):\n''')
    opcion=int(input("""Ingrese que tipo de gráfico desea descargar: 
1. Gráfico ORO por KILO
2. Gráfico ORO por ONZA\n"""))

    if opcion == 1:
        goldkg()
    elif opcion == 2:
        goldoz()
    else:
        print("Escriba 1 o 2")


def goldkg():

    try:

        image_url = "https://www.kitconet.com/charts/metals/gold/tny_au_en_uskg_2.gif"
        filename = image_url.split("/")[-1]


        r = requests.get(image_url, stream = True)


        if r.status_code == 200:
   
            r.raw.decode_content = True
    
   
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
        
        else:
            print('El gráfico del ORO no se pudo descargar')


        photo = open('tny_au_en_uskg_2.gif', 'rb')
        print(f"""Gráfico ORO por KILO en 24hs descargado como:
{filename}""")

    except:
        print("error al obtener el gráfico del oro")

def goldoz():

    try:

        image_url = "https://www.kitconet.com/charts/metals/gold/tny_au_en_usoz_2.gif"
        filename = image_url.split("/")[-1]


        r = requests.get(image_url, stream = True)


        if r.status_code == 200:
   
            r.raw.decode_content = True
    
   
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
        
        else:
            print('El gráfico del ORO no se pudo descargar')

        photo = open('tny_au_en_usoz_2.gif', 'rb')
        print(f"""Gráfico ORO por ONZA en 24hs descargado como:
{filename}""")

    except:
        print("error al obtener el gráfico del oro")

oro()