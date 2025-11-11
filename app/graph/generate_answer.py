def generate_answer_node(state: dict) -> dict:
    intent = state["intent"]
    docs = state["docs"]
    question = state["question"]

    if not docs:
        state["answer"] = f"No he encontrado información concreta para: {question}"
        return state

    # respuesta muy simple para empezar
    if intent == "aldea":
        doc = docs[0]
        answer = (
            f"Aldea recomendada: {doc['titulo']} ({doc['concejo']}). "
            f"{doc.get('descripcion', '')}"
        )
    elif intent == "ruta":
        doc = docs[0]
        answer = (
            f"Ruta sugerida: {doc['titulo']}. "
            f"Dificultad: {doc.get('dificultad', 'no indicada')}. "
            f"{doc.get('descripcion', '')}"
        )
    else:
        answer = f"He encontrado estos datos: {docs}"

    state["answer"] = answer
    return state
