# Brasilidades
Biblioteca Python recheada de brasilidades! Além de ser brasilmente diferente - evento de bibliotecas inúteis do servidor do @lanc0de

## 📲 Instalação
```bash
pip install brasilidades
```

## 👍 Coisas aleatórias do código

```python
import os
import random


import shutil
from pathlib import Path

# Envia prints aleatórios pro seu terminal
def prints_aleatorios():
    frases = [
        "Ao invés de ser uma pessoa seja uma pessoa!",
        "Para de procrastinar e vai resolver os bugs da tua aplicação!",
        "Não tome café-",
        "Fazendo download do teu pc..." # concerteza faz o download do teu pc
    ]

    frase_escolhida = random.choice(frases) # escolhe em ordem aleatória uma frase
    print(frase_escolhida)

prints_aleatorios()

def enviar_bom_dia_do_zap():
    base_path = Path(__file__).parent
    imagem_path = base_path / "assets" / "image.png"
    
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    destino = os.path.join(desktop, "image.png") # Baixa a imagem de bom dia
    
    try:
        if imagem_path.exists():
            shutil.copy2(imagem_path, destino)
            print("📦 Imagem de bom dia enviada pra sua área de trabalho, aproveita e envia pra quem vc quiser!")
    except:
        pass

# Vende-se Celta
def olha_o_pix():
    print("Vende-se Celta")
    print("")
    print("Mande o pix para seuzedograu@bomdia.com")
```

## ❓ Como funciona
 - Manda prints aleatórios pro seu terminal;
 - Manda mais um print só que de um "Vende-se Celta";
 - Faz o download de um "bom dia" no seu pc.

 ## 🤝 Contribuindo

 Nós aceitamos contribuições mas com uma regra importante:
 
 - ❌ | Não otimize nada
 - ❌ | Não remova nada desnecessário
 - ❌ | Não melhore a performance
 - ❌ | Não mude nada, quanto mais pior melhor 👍

 ### O que nós queremos:
 - ✅ | Loops extras
 - ✅ | Verificações redundantes
 - ✅ | Performance pior
 - ✅ | Tempo de execução maior
 - ✅ | Mais downloads desnecessários

Feito com ❤️ por Aquele Astro Lá
