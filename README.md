#  Asturias Rústica Occidental – Mar, piedra y naturaleza viva

##  Descripción general
**Asturias Rústica Occidental** es un sistema **RAG multimodal** (Retrieval-Augmented Generation) diseñado para ofrecer información contextual, visual y cultural sobre el occidente medio de Asturias —una región de aldeas auténticas, arquitectura de pizarra, paisajes costeros, rutas rurales, playas naturales y observación de fauna.

El sistema combina **FastAPI**, **LangGraph** y **Gemini 1.5 Pro Multimodal** para permitir consultas naturales como:

- “Qué pueblos con vistas hay cerca de Boal.”  
- “Dónde ver buitres en el occidente de Asturias.”  
- “Cuándo es la fiesta de San Timoteo en Valdés.”  
- “Qué rutas fáciles hay cerca de Navia.”

---

##  Objetivo
Crear una IA **contextual y visual** capaz de responder con precisión usando datos locales (aldeas, rutas, playas, fauna, eventos y cultura rural), combinando **texto e imágenes**.

---

## Arquitectura general

asturias-rustica-occidental/
├── app/
│ ├── main.py # API FastAPI
│ ├── rag_flow.py # Flujo LangGraph
│ ├── config.py # Configuración general
│ ├── graph/ # Nodos del grafo
│ │ ├── classify_intent.py
│ │ ├── rewrite_question.py
│ │ ├── retrieve_docs.py
│ │ └── generate_answer.py
│ ├── retrievers/ # Buscadores por tipo de dato
│ │ ├── aldeas_retriever.py
│ │ ├── rutas_retriever.py
│ │ ├── playas_retriever.py
│ │ ├── fauna_retriever.py
│ │ └── eventos_retriever.py
│ └── agents/ # Agentes ampliables
│ ├── travel_planner.py
│ ├── image_search.py
│ └── calendar_events.py
├── data_text/ # Fichas descriptivas en JSON o TXT
│ ├── aldeas_occidente/
│ ├── rutas_y_paisajes/
│ ├── playas_y_entornos/
│ ├── fauna_y_avistamientos/
│ └── eventos_locales/
├── data_img/ # Imágenes de soporte
│ ├── pueblos_pizarra_occidente/
│ ├── rutas_y_miradores/
│ ├── playas_occidentales/
│ └── fauna_penouta/
├── requirements.txt
└── README.md


---

##  Tecnologías principales

| Categoría | Tecnología | Uso |
|------------|-------------|-----|
| Framework API | **FastAPI** | API REST principal |
| Orquestación | **LangGraph** | Flujo de nodos RAG |
| Modelo de lenguaje | **Gemini 1.5 Pro Multimodal** | Reformulación y generación multimodal |
| Embeddings | **FAISS** | Búsqueda semántica local |
| Datos | **JSON / TXT locales** | Información rural y cultural |
| Procesamiento multimodal | **Gemini + PIL + PyMuPDF** | Análisis de texto e imagen |
| Backend opcional | **PostgreSQL / JSON local** | Persistencia de datos |
| Entorno | **Python 3.11 + Google Colab / Local** | Desarrollo y pruebas |

---

## Ejecución rápida

1. Clonar el proyecto:
   ```bash
   git clone https://github.com/SilviaCue/Asturias-Rustica-Occidental-RAG.git
   cd asturias_rustica
---
© 2025 **Silvia Cue** · *Asturias Rústica Occidental – Mar, piedra y naturaleza viva*  
Código bajo licencia [MIT](./LICENSE) · Contenido (textos e imágenes) bajo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
