# Usa uma imagem base do Python com suporte a ffmpeg
FROM python:3.11-slim

# Instala dependências do sistema necessárias
RUN apt-get update && apt-get install -y ffmpeg imagemagick libsm6 libxext6

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponha a porta que seu app usa
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]
