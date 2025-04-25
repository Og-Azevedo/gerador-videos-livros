FROM python:3.11-slim

# Instala dependências de sistema
RUN apt-get update && apt-get install -y ffmpeg imagemagick

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação
COPY . .

# Instala dependências Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Flask usará
EXPOSE 5000

# Define comando de start
CMD ["python", "app.py"]

