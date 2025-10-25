import os
from dotenv import load_dotenv

load_dotenv()

from src.app import create_app
from src.db.init import init_database

init_database()
app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)
