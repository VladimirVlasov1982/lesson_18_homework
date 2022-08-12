class Config(object):
    # Конфигурация приложения
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    RESTX_JSON = {"ensure_ascii": False, "indent": 2}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = True
