# Use uma imagem base com Python instalado
FROM python:3.9.16


# Copie seu arquivo .py para a imagem
COPY . /automacao-python

COPY . .

# Defina o diretório de trabalho
WORKDIR /automacao-python

RUN pip install xtelnet

# Execute seu script Python
ENTRYPOINT ["python", "onu.py", "/bin/bash"]
