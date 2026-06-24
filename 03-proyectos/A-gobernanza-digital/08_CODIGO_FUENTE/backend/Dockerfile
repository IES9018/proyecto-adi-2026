FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY src/ src/

# Puerto expuesto
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "src.web.main:app", "--host", "0.0.0.0", "--port", "8000"]
