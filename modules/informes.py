# modules/informe.py
import pdfkit
from jinja2 import Environment, FileSystemLoader
import pandas as pd

def crear_informe_pdf(df, nombre_archivo="data/informe_leads.pdf"):
    env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template("informe_template.html")
            html_out = template.render(leads=df.to_dict(orient="records"))
                pdfkit.from_string(html_out, nombre_archivo)