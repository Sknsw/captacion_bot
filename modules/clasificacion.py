# modules/clasificacion.py
import spacy
from config import KEYWORDS

nlp = spacy.load("en_core_web_sm")

def clasificar_perfil(perfil):
    doc = nlp(perfil['nombre'])
        perfil['relevancia'] = 'Alta' if any(token.text.lower() in KEYWORDS for token in doc) else 'Baja'
            return perfil

            def clasificar_leads(leads):
                return [clasificar_perfil(lead) for lead in leads]