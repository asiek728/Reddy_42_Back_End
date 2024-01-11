from application import app, socketio, routes ## app from __init__.py

if __name__ == "__main__":
    app.run(port=4000, debug=True, host="0.0.0.0")
    socketio.run(app, debug=True)
