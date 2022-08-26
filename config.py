class Config(object):
    # Конфигурация приложения
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    RESTX_JSON = {"ensure_ascii": False, "indent": 2}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = True
    JSON_AS_ASCII = False
