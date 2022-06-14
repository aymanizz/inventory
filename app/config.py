import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("INVENTORY_APP_SECRET_KEY") or "defalut-secret-key"

    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("INVENTORY_APP_DATABASE_URL")
        or f"sqlite:///{os.path.join(basedir, 'app.db')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
