# modules/envio_mensajes.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config import EMAIL_REMITENTE, EMAIL_PASSWORD, DESTINATARIO_INFORME

def enviar_informe(archivo_pdf, asunto="Informe de Leads", mensaje="Adjunto el informe generado."):
    msg = MIMEMultipart()
        msg['From'] = EMAIL_REMITENTE
            msg['To'] = DESTINATARIO_INFORME
                msg['Subject'] = asunto
                    msg.attach(MIMEText(mensaje, 'plain'))
                        
                            with open(archivo_pdf, "rb") as adjunto:
                                    mime_base = MIMEBase('application', 'octet-stream')
                                            mime_base.set_payload(adjunto.read())
                                                    encoders.encode_base64(mime_base)
                                                            mime_base.add_header('Content-Disposition', f'attachment; filename={archivo_pdf}')
                                                                    msg.attach(mime_base)
                                                                        
                                                                            try:
                                                                                    server = smtplib.SMTP('smtp.gmail.com', 587)
                                                                                            server.starttls()
                                                                                                    server.login(EMAIL_REMITENTE, EMAIL_PASSWORD)
                                                                                                            server.sendmail(EMAIL_REMITENTE, DESTINATARIO_INFORME, msg.as_string())
                                                                                                                    server.quit()
                                                                                                                            print("Correo enviado a", DESTINATARIO_INFORME)
                                                                                                                                except Exception as e:
                                                                                                                                        print("Error al enviar el correo:", e)