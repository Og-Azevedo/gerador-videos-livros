
from flask import Flask, request, jsonify, send_from_directory
import requests
from moviepy.editor import *
import tempfile
import os

app = Flask(__name__)

@app.route('/gerar-video', methods=['POST'])
def gerar_video():
    data = request.json

    trecho = data['trecho']
    titulo = data['titulo']
    autora = data['autora']
    audio_url = data['audio_url']

    # Baixar o áudio
    audio_response = requests.get(audio_url)
    temp_audio_path = tempfile.mktemp(suffix=".mp3")
    with open(temp_audio_path, "wb") as f:
        f.write(audio_response.content)

    # Criar vídeo
    audio_clip = AudioFileClip(temp_audio_path)
    duration = audio_clip.duration

    # Fundo branco
    video = ColorClip(size=(1080, 1920), color=(255, 255, 255), duration=duration)

    # Textos
    title_clip = TextClip(titulo, fontsize=80, color="black", font="DejaVu-Serif", method="caption", size=(900, None)).set_position(("center", 400)).set_duration(duration)
    author_clip = TextClip(autora, fontsize=50, color="black", font="DejaVu-Serif", method="caption", size=(900, None)).set_position(("center", 500)).set_duration(duration)
    trecho_clip = TextClip(trecho, fontsize=50, color="black", font="DejaVu-Serif", method="caption", size=(900, None)).set_position(("center", 700)).set_duration(duration)

    # Compor
    final = CompositeVideoClip([video, title_clip, author_clip, trecho_clip]).set_audio(audio_clip)

    # Exportar vídeo
    output_path = "static/video_final.mp4"
    os.makedirs("static", exist_ok=True)
    final.write_videofile(output_path, fps=24)

    # Retornar o link do vídeo
    base_url = request.url_root
    return jsonify({"video_url": f"{base_url}static/video_final.mp4"})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
