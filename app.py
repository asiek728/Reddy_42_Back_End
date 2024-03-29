from application import app, socketio, routes ## app from __init__.py

from application.patients import routes
from application.conditions import routes
from application.hereditary_conditions import routes
from application.messages import routes

if __name__ == "__main__":
    # app.run(port=4000, debug=True, host="0.0.0.0")
    socketio.run(app, port=5000, debug=True)
