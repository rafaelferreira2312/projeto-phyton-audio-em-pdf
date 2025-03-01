# Conversor de Vídeo (.mkv) para Texto

Este projeto extrai o áudio de arquivos de vídeo no formato `.mkv` e o transcreve em um arquivo `.txt` utilizando Python.

## Tecnologias Utilizadas

- Python 3
- MoviePy
- SpeechRecognition
- Pydub
- FFMPEG

## Requisitos

Certifique-se de que seu sistema possui os seguintes pacotes instalados:

### Dependências Python

Instale as bibliotecas necessárias utilizando o `pip`:

```bash
pip install moviepy speechrecognition pydub
```

### FFMPEG

O `ffmpeg` é necessário para extrair o áudio dos vídeos. Instale-o conforme seu sistema operacional:

- **Ubuntu/Debian:**
  ```bash
  sudo apt-get install ffmpeg
  ```
- **MacOS (via Homebrew):**
  ```bash
  brew install ffmpeg
  ```
- **Windows:** Baixe e instale o `ffmpeg` a partir do site oficial: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

## Como Usar

1. **Coloque o vídeo na mesma pasta do script**

   - O vídeo deve estar no formato `.mkv`

2. **Execute o script**

   ```bash
   python3 converter.py
   ```

3. **Verifique o arquivo de texto gerado**

   - Após a execução, um arquivo `.txt` será criado com o mesmo nome do vídeo.

## Estrutura do Projeto

```
/
|-- converter.py  # Script principal
|-- video_exemplo.mkv  # Arquivo de vídeo para teste
|-- video_exemplo.txt  # Arquivo de saída com a transcrição
```

## Explicação do Script

O script segue os seguintes passos:

1. Carrega o vídeo usando `moviepy.editor`.
2. Extrai o áudio do vídeo e o salva temporariamente em `.wav`.
3. Divide o áudio em partes menores usando `pydub` para melhor reconhecimento.
4. Transcreve cada trecho utilizando a API do Google Speech Recognition.
5. Salva o texto resultante em um arquivo `.txt`.
6. Remove os arquivos temporários.

## Possíveis Erros e Soluções

### 1. "python: command not found"

Se você está no Linux e o comando `python` não é reconhecido, tente:

```bash
python3 converter.py
```

### 2. "ffmpeg not found"

Se o `ffmpeg` não estiver instalado corretamente, siga as instruções acima para instalá-lo.

### 3. "recognition connection failed: [Errno 32] Broken pipe"

Isso pode ocorrer se a conexão com a API do Google falhar. Soluções:

- Verifique sua conexão com a internet.
- Reinicie o script.
- Divida o áudio em segmentos menores.

## Autor

Projeto desenvolvido por [Seu Nome] como uma ferramenta simples para transcrição de vídeos em texto.

