import os
import random
import asyncio

import shutil
from pathlib import Path

def prints_aleatorios():
    frases = [
        "Ao invés de ser uma pessoa seja uma pessoa!",
        "Para de procrastinar e vai resolver os bugs da tua aplicação!",
        "Não tome café-",
        "Fazendo download do teu pc..."
    ]

    frase_escolhida = random.choice(frases)
    print(frase_escolhida)

prints_aleatorios()

def enviar_bom_dia_do_zap():
    base_path = Path(__file__).parent
    imagem_path = base_path / "assets" / "image.png"
    
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    destino = os.path.join(desktop, "BOM_DIA_GRUPO.jpg")
    
    try:
        if imagem_path.exists():
            shutil.copy2(imagem_path, destino)
            print("📦 Imagem de bom dia enviada pra sua área de trabalho, aproveita e envia pra quem vc quiser!")
    except:
        pass

def olha_o_pix():
    print("Vende-se Celta")
    print("")
    print("Mande o pix para seuzedograu@bomdia.com")
