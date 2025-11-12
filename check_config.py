# app/check_config.py
from app.config import load_settings

def main():
    settings = load_settings()

    print("\n=== Comprobación de configuración (local) ===")
    print(f"Entorno: {settings.get('APP_ENV')}")
    print(f"Ruta datos: {settings.get('ASTURIAS_DATA_DIR')}")
    print(f"Ruta índice: {settings.get('ASTURIAS_INDEX_DIR')}")
    print(f"Modelo embeddings: {settings.get('EMBEDDINGS_MODEL_NAME')}")
    print(f"Tiene GOOGLE_API_KEY: {bool(settings.get('GOOGLE_API_KEY'))}")
    print("\nErrores detectados:")
    errors = settings.get('_validation_errors', [])
    if errors:
        for e in errors:
            print(f" - {e}")
    else:
        print(" Ninguno. Todo correcto.")
    print("=============================================\n")

if __name__ == "__main__":
    main()
