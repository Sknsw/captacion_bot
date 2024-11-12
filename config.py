# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Configuración de correo y API
EMAIL_REMITENTE = os.getenv("elboykillerdiamont@gmail.com")
EMAIL_PASSWORD = os.getenv("71897189aA@")
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
DESTINATARIO_INFORME = os.getenv("rodriguezgrxalbert@gmail.com")

# Configuración de búsqueda
KEYWORDS = ["finanzas", "tecnología"]
UBICACION = "Madrid"