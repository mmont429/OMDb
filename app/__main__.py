from app import app, frontend

FLASK_PORT = 5001

if __name__ == "__main__":
    app.run (debug=True, port=FLASK_PORT, host='127.0.0.1')