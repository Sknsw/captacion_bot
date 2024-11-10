# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de correo y API
EMAIL_REMITENTE = os.getenv("EMAIL_REMITENTE")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
DESTINATARIO_INFORME = os.getenv("DESTINATARIO_INFORME")

# Configuración de búsqueda
KEYWORDS = ["finanzas", "tecnología"]
UBICACION = "Madrid"