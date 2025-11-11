# Aquí iría tu llamada real a Gemini u otro LLM.
# De momento lo dejamos en reglas simples para no complicar.
def classify_intent_node(state: dict) -> dict:
    question = state["question"].lower()

    if any(x in question for x in ["aldea", "pueblo", "villayón", "valdés", "boal", "navia", "coaña", "tapia"]):
        intent = "aldea"
    elif any(x in question for x in ["ruta", "caminar", "sendero", "mirador", "penouta", "esva"]):
        intent = "ruta"
    elif any(x in question for x in ["playa", "costa", "mar", "frejulfe", "barayo", "serantes"]):
        intent = "playa"
    elif any(x in question for x in ["buitre", "fauna", "aves", "avistamiento"]):
        intent = "fauna"
    elif any(x in question for x in ["fiesta", "romería", "san timoteo", "evento", "festival"]):
        intent = "evento"
    else:
        intent = "general"

    state["intent"] = intent
    return state
