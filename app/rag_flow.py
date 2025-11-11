from langgraph.graph import StateGraph, END
from typing import Dict, Any

from app.graph.classify_intent import classify_intent_node
from app.graph.rewrite_question import rewrite_question_node
from app.graph.retrieve_docs import retrieve_docs_node
from app.graph.generate_answer import generate_answer_node

# Estado que va pasando por el grafo
class RAGState(dict):
    question: str
    intent: str
    rewritten_question: str
    docs: list
    answer: str

def build_graph():
    graph = StateGraph(RAGState)

    graph.add_node("classify_intent", classify_intent_node)
    graph.add_node("rewrite_question", rewrite_question_node)
    graph.add_node("retrieve_docs", retrieve_docs_node)
    graph.add_node("generate_answer", generate_answer_node)

    graph.set_entry_point("classify_intent")

    # classify -> rewrite
    graph.add_edge("classify_intent", "rewrite_question")
    # rewrite -> retrieve
    graph.add_edge("rewrite_question", "retrieve_docs")
    # retrieve -> answer
    graph.add_edge("retrieve_docs", "generate_answer")
    # answer -> END
    graph.add_edge("generate_answer", END)

    return graph.compile()

rag_app = build_graph()

def run_rag_flow(question: str) -> str:
    initial_state: Dict[str, Any] = {
        "question": question,
        "intent": "",
        "rewritten_question": "",
        "docs": [],
        "answer": ""
    }
    final_state = rag_app.invoke(initial_state)
    return final_state["answer"]
