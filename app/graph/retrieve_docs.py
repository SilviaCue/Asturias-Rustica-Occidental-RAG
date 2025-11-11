from app.retrievers.aldeas_retriever import retrieve_aldeas
from app.retrievers.rutas_retriever import retrieve_rutas
# from app.retrievers.playas_retriever import retrieve_playas
# from app.retrievers.fauna_retriever import retrieve_fauna
# from app.retrievers.eventos_retriever import retrieve_eventos

def retrieve_docs_node(state: dict) -> dict:
    intent = state["intent"]
    query = state["rewritten_question"]

    if intent == "aldea":
        docs = retrieve_aldeas(query)
    elif intent == "ruta":
        docs = retrieve_rutas(query)
    elif intent == "playa":
        # docs = retrieve_playas(query)
        docs = []
    elif intent == "fauna":
        # docs = retrieve_fauna(query)
        docs = []
    elif intent == "evento":
        # docs = retrieve_eventos(query)
        docs = []
    else:
        # fallback general
        docs = []

    state["docs"] = docs
    return state
