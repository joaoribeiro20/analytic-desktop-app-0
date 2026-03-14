# 1. Imagem base do Python (versão enxuta)
FROM python:3.10-slim

# 2. Instala as dependências que o Tkinter exige do Linux
# Sem isso, o Python não consegue desenhar janelas
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

# 3. Define a pasta de trabalho dentro do container
WORKDIR /app

# 4. Copia o seu código para dentro do container
COPY . .

# 5. Variável de ambiente para o Docker saber onde enviar o vídeo
# O valor padrão 'host.docker.internal:0.0' aponta para o seu Windows
ENV DISPLAY=host.docker.internal:0.0

# 6. Comando para rodar seu app
CMD ["python", "Frame.py"]