# Usa uma imagem oficial do Python como base
FROM python:3.11-slim

# Instala dependências de sistema necessárias
RUN apt-get update && apt-get install -y ffmpeg imagemagick

# Cria um diretório para o app
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Flask usará
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]
