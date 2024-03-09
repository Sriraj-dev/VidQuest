import importlib
import os
from dotenv import load_dotenv
import subprocess

load_dotenv()


if __name__ == "__main__":
    print("Starting pathway_sample_app!!")
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8080))
    app_api = importlib.import_module("api.app")
    app_api.run(host=host, port=port)