# Image Downloader with DuckDuckGo

Este projeto contém um script Python que faz o download automático de imagens da internet utilizando a API de busca de imagens do DuckDuckGo. Ele é configurável para buscar imagens com base em um termo específico, salvar em um diretório local e filtrar por formatos de imagem (JPEG, PNG, WebP). O script inclui tratamento de erros, re-tentativas e atrasos para evitar bloqueios por rate limiting, tornando-o útil para coletar datasets de imagens.

## Funcionalidades

- **Busca de Imagens**: Usa o DuckDuckGo para buscar imagens com base em um termo definido (ex.: "cars").
- **Filtros de Formato**: Suporta imagens nos formatos JPEG, PNG e WebP.
- **Nomes Únicos**: Gera nomes de arquivos com hash MD5 para evitar sobrescrita.
- **Robustez**: Inclui re-tentativas para erros de busca ou download e atrasos configuráveis para evitar rate limiting.
- **Logs Detalhados**: Exibe o progresso e erros durante o processo.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `duckduckgo_search` (para busca de imagens)
  - `urllib` (incluído na biblioteca padrão do Python)
  - `mimetypes` (incluído na biblioteca padrão do Python)
  - `hashlib` (incluído na biblioteca padrão do Python)
  - Opcional: `fake-useragent` (para rotação de User-Agent)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Crie e ative um ambiente virtual** (recomendado):
   ```bash
   python -m venv meu_ambiente
   source meu_ambiente/bin/activate  # Linux/Mac
   meu_ambiente\Scripts\activate  # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install duckduckgo_search
   ```

   Opcional: Para rotação de User-Agent, instale:
   ```bash
   pip install fake-useragent
   ```

## Uso

1. **Configuração**:
   Edite o script `downloadImagensDuckDuckGO.py` para ajustar as configurações:
   - `filtro`: Termo de busca (ex.: "cars").
   - `destino`: Caminho do diretório onde as imagens serão salvas.
   - `max_resultados`: Número máximo de imagens a baixar.
   - `extensoes_permitidas`: Lista de formatos aceitos (ex.: `['image/jpeg', 'image/png', 'image/webp']`).
   - `delay_segundos`: Atraso entre requisições (ex.: 5 segundos).
   - `max_tentativas`: Número máximo de re-tentativas para erros.

   Exemplo de configuração no script:
   ```python
   filtro = 'cars'
   destino = r'C:\Users\seu-usuario\Downloads\dataset'
   max_resultados = 10
   extensoes_permitidas = ['image/jpeg', 'image/png', 'image/webp']
   delay_segundos = 5
   max_tentativas = 3
   ```

2. **Execute o script**:
   ```bash
   python downloadImagensDuckDuckGO.py
   ```

3. **Saída**:
   As imagens serão salvas no diretório especificado com nomes no formato `filtro_hash.ext` (ex.: `cars_1a2b3c4d.jpg`). Logs no console mostrarão o progresso e eventuais erros.

## Exemplo de Saída

```plaintext
Iniciando download de até 10 imagens com filtro: cars
Busca bem-sucedida, 10 imagens encontradas.
[0] OK - C:\Users\paulo\Downloads\lampadas\dataset\cars_1a2b3c4d.jpg
[1] Ignorado (tipo image/gif não permitido)
[2] OK - C:\Users\paulo\Downloads\lampadas\dataset\cars_5e6f7g8h.png
...
Download concluído. 8 imagens salvas.
```

## Notas

- **Rate Limiting**: O DuckDuckGo pode impor limites de requisições. Se ocorrer um erro `403 Ratelimit`, aumente o `delay_segundos` ou reduza `max_resultados`.
- **User-Agent**: Para evitar bloqueios, o script usa um User-Agent padrão (`Mozilla/5.0`). Para maior robustez, descomente as linhas do `fake-useragent` no script após instalá-lo.
- **Permissões**: Certifique-se de que o diretório de destino existe e que você tem permissões de escrita.
- **Validação de Imagens**: O script não valida se as imagens baixadas são válidas. Considere usar a biblioteca `Pillow` para verificação adicional, se necessário.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias, como:
- Suporte a outras APIs de busca de imagens.
- Download assíncrono para maior eficiência.
- Validação de imagens após o download.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).