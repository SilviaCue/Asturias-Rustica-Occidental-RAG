def rewrite_question_node(state: dict) -> dict:
    # Aquí puedes llamar a Gemini para reescritura.
    # Por ahora, pasamos la pregunta original como "reformulada".
    original = state["question"]
    state["rewritten_question"] = original
    return state
