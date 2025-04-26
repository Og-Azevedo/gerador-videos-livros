FROM python:3.11-slim

# Atualiza o sistema e instala ffmpeg e imagemagick
RUN apt-get update && apt-get install -y ffmpeg imagemagick

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
