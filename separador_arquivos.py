import os
from pathlib import Path
import shutil

caminho = input("Digite o caminho do arquivo: ")

caminho = caminho.replace('"', '')
#substitui as aspas duplas por nada, caso o usuário tenha colocado aspas duplas no caminho

nome_pasta = input("Digite o nome da pasta: ")

caminho_copiado = Path(caminho)
#substitui a variável caminho por uma variável do tipo Path, que é mais fácil de trabalhar com arquivos e pastas

pasta_destino_principal = caminho_copiado / nome_pasta
#nome da pasta que será criada para organizar os arquivos

while pasta_destino_principal.exists():
 #verifica se a pasta já existe, caso exista, pede para o usuário digitar outro nome   
    nome_pasta = input("A pasta já existe. Digite outro nome: ")
    #substitui a variável nome_pasta por uma nova variável, que é o novo nome da pasta que o usuário digitou
    
    pasta_destino_principal = caminho_copiado / nome_pasta
    #substitui a variável pasta_destino_principal por uma nova variável, que é o novo caminho da
    # pasta que o usuário digitou
    
pasta_destino_principal.mkdir(parents=True)
 #cria a pasta que o usuário digitou, caso ela não exista
 
arquivos = {
    ".txt": "Textos",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".pdf": "PDFs",
    ".docx": "Documentos",
    ".xlsx": "Planilhas",
    ".pptx": "Apresentações",
    ".mp3": "Áudios",
    ".mp4": "Vídeos",
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".csv": "Planilhas",
}

for item in caminho_copiado.iterdir():
    if item.is_file():
        extensao = item.suffix.lower()
        
        if extensao in arquivos:
            nome_subpasta = arquivos[extensao]
            subpasta =  pasta_destino_principal / nome_subpasta
    
            subpasta.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(item), str(subpasta / item.name))
# aqui o código percorre todos os arquivos do caminho digitado pelo usuário, 
# verifica a extensão de cada arquivo e cria uma subpasta correspondente à extensão do arquivo dentro da pasta principal criada pelo usuário. 
# Em seguida, ele copia o arquivo para a subpasta correspondente.


    
    