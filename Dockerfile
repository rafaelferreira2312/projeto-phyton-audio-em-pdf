FROM python:3.8-slim

# Instalar dependências
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6

# Criar diretórios de trabalho
RUN mkdir -p /app/input_videos /app/input_audio /app/output_pdfs

# Copiar todos os arquivos do diretório local para dentro do contêiner
COPY . /app

# Definir o diretório de trabalho como /app
WORKDIR /app

# Instalar bibliotecas Python
RUN pip install -r requirements.txt

# Comando padrão para executar o script
CMD ["python", "script.py"]