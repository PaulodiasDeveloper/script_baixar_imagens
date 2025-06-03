from duckduckgo_search import DDGS
import urllib.request
import os
import mimetypes
import time
import hashlib
# Descomente a linha abaixo se usar fake-useragent
# from fake_useragent import UserAgent

# Configurações
filtro = 'Mac'
destino = r'C:\Users\paulo\Downloads\lampadas\dataset'
max_resultados = 10  # Reduzido para evitar rate limiting
extensoes_permitidas = ['image/jpeg', 'image/png', 'image/webp']
delay_segundos = 5  # Aumentado para maior segurança
max_tentativas = 3
# ua = UserAgent()  # Descomente se instalar fake-useragent

print(f'Iniciando download de até {max_resultados} imagens com filtro: {filtro}')

# Garante que a pasta de destino existe
os.makedirs(destino, exist_ok=True)

contador = 0

# Função para gerar nome de arquivo único
def gerar_nome_unico(url, extensao):
    hash_url = hashlib.md5(url.encode()).hexdigest()[:8]
    return os.path.join(destino, f"{filtro}_{hash_url}{extensao}")

# Inicia busca com DDGS
for tentativa_busca in range(max_tentativas):
    try:
        with DDGS() as ddgs:
            resultados = list(ddgs.images(filtro, max_results=max_resultados))
            print(f"Busca bem-sucedida, {len(resultados)} imagens encontradas.")
            break
    except Exception as e:
        print(f"Tentativa {tentativa_busca + 1} de busca falhou: {e}")
        if tentativa_busca == max_tentativas - 1:
            print("Falha após todas as tentativas de busca.")
            resultados = []
            break
        time.sleep(delay_segundos * (tentativa_busca + 1))

# Processa os resultados
for i, r in enumerate(resultados):
    url = r["image"]
    for tentativa in range(max_tentativas):
        try:
            # req = urllib.request.Request(url, headers={'User-Agent': ua.random})  # Use com fake-useragent
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                tipo = response.headers.get_content_type()

                if tipo not in extensoes_permitidas:
                    print(f"[{i}] Ignorado (tipo {tipo} não permitido)")
                    break

                extensao = mimetypes.guess_extension(tipo) or '.jpg'
                nome_arquivo = gerar_nome_unico(url, extensao)

                if os.path.exists(nome_arquivo):
                    print(f"[{i}] Ignorado (arquivo {nome_arquivo} já existe)")
                    break

                with open(nome_arquivo, 'wb') as f:
                    f.write(response.read())

                print(f"[{i}] OK - {nome_arquivo}")
                contador += 1
                time.sleep(delay_segundos)
                break

        except Exception as erro_download:
            print(f"[{i}] Tentativa {tentativa + 1} falhou: {erro_download}")
            if tentativa == max_tentativas - 1:
                print(f"[{i}] Falha após {max_tentativas} tentativas")
            time.sleep(delay_segundos * (tentativa + 1))

print(f'Download concluído. {contador} imagens salvas.')