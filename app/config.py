# app/config.py

def load_settings():
    # Configuración mínima de prueba
    return {
        "APP_ENV": "dev",
        "ASTURIAS_DATA_DIR": "./data_text",
        "ASTURIAS_INDEX_DIR": "./faiss_index",
        "EMBEDDINGS_MODEL_NAME": "bge-small-es",
        "GOOGLE_API_KEY": "local_test_key",
        "_validation_errors": []
    }
