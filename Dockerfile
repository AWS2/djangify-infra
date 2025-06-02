FROM python:3.11-slim

# Evita archivos .pyc y mejora logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instala dependencias del sistema necesarias para compilar paquetes Python (como mysqlclient)
RUN apt-get update && \
    apt-get install -y build-essential default-libmysqlclient-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Crea la carpeta del projecte
WORKDIR /app

# Copia requirements e instala dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia tot el projecte
COPY . .

# Expón el puerto (opcional)
EXPOSE 8000

# Lanza Gunicorn al arrancar el contenedor
CMD ["gunicorn", "webapp.wsgi:application", "--bind", "0.0.0.0:8000"]

