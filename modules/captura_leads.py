# modules/captura_leads.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import KEYWORDS, UBICACION, CHROME_DRIVER_PATH

def iniciar_selenium():
    options = webdriver.ChromeOptions()
        options.add_argument("--headless")
            options.add_argument("--disable-blink-features=AutomationControlled")
                driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
                    return driver

                    def buscar_leads(driver):
                        leads = []
                            url = f"https://www.google.com/search?q=site:linkedin.com/in+{'+'.join(KEYWORDS)}+{UBICACION}"
                                driver.get(url)
                                    time.sleep(3)
                                        
                                            perfiles = driver.find_elements(By.XPATH, '//div[@class="g"]')
                                                for perfil in perfiles:
                                                        try:
                                                                    nombre = perfil.find_element(By.TAG_NAME, 'h3').text
                                                                                enlace = perfil.find_element(By.TAG_NAME, 'a').get_attribute("href")
                                                                                            leads.append({'nombre': nombre, 'enlace': enlace, 'ubicacion': UBICACION, 'palabras_clave': KEYWORDS})
                                                                                                    except Exception as e:
                                                                                                                print(f"Error extrayendo perfil: {e}")
                                                                                                                    return leads