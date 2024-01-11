from application import app ## app from __init__.py

from application import routes
from application.patients import routes
from application.conditions import routes
# from application.user import auth

if __name__ == "__main__":
    app.run(port=4000, debug=True, host="0.0.0.0")
