# main.py
from modules.captura_leads import iniciar_selenium, buscar_leads
from modules.clasificacion import clasificar_leads
from modules.informe import crear_informe_pdf
from modules.envio_mensajes import enviar_informe
import pandas as pd

def ejecutar_bot():
    driver = iniciar_selenium()
        try:
                # Captura y clasificación de leads
                        leads = buscar_leads(driver)
                                leads_clasificados = clasificar_leads(leads)
                                        
                                                # Generación del informe
                                                        df_leads = pd.DataFrame(leads_clasificados)
                                                                crear_informe_pdf(df_leads)
                                                                        
                                                                                # Enviar informe
                                                                                        enviar_informe("data/informe_leads.pdf")
                                                                                            finally:
                                                                                                    driver.quit()

                                                                                                    if __name__ == "__main__":
                                                                                                        ejecutar_bot()