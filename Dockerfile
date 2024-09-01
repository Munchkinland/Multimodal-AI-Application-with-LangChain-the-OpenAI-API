# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Instala herramientas necesarias para compilar paquetes
RUN apt-get update && \
    apt-get install -y \
    curl \
    build-essential

# Instala Rust para compilar paquetes necesarios
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    export PATH="/root/.cargo/bin:${PATH}"

# Copia el archivo de requirements.txt al contenedor
COPY requirements.txt .

# Actualiza pip, setuptools y wheel antes de instalar dependencias
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Define el comando para ejecutar la aplicación
CMD ["python", "app/main.py"]
