# main.py
import os
import pandas as pd
from modules.captura_leads import iniciar_selenium, buscar_leads
from modules.clasificacion import clasificar_leads
from modules.informe import crear_informe_pdf
from modules.envio_mensajes import enviar_informe
from config import DESTINATARIO_INFORME

def ejecutar_bot():
    driver = iniciar_selenium()
    informe_path = "data/informe_leads.pdf"

    try:
        print("Iniciando captura de leads...")
        leads = buscar_leads(driver)
        
        print("Clasificando leads...")
        leads_clasificados = clasificar_leads(leads)
        
        if not leads_clasificados:
            print("No se encontraron leads relevantes.")
            return

        df_leads = pd.DataFrame(leads_clasificados)
        
        print(f"Generando informe en {informe_path}...")
        crear_informe_pdf(df_leads, informe_path)
        
        print(f"Enviando informe por correo a {DESTINATARIO_INFORME}...")
        enviar_informe(DESTINATARIO_INFORME, informe_path)
        
        print("Proceso completado con éxito.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")
    
    ejecutar_bot()