# Sustituye esto por tu FAISS real cargado desde /data_text/aldeas_occidente
def retrieve_aldeas(query: str):
    # devolvería una lista de dicts con título, descripción, concejo, coords
    return [
        {
            "titulo": "Belén (Valdés)",
            "tipo": "aldea",
            "concejo": "Valdés",
            "descripcion": "Pequeña aldea de pizarra con vistas hacia el valle.",
            "coordenadas": "43.5, -6.6"
        }
    ]
