HOST = '127.0.0.1'
# PORT = '9090'
# LOG_LEVEL = 'info'
# UDS = None
# FD = None
# LOOP = "auto"
# HTTP = "auto"
# WS = "auto"
# # LIFESPAN = "auto"
# LOGGER = None
# ACCESS_LOG = True,
# INTERFACE = "auto"
# DEBUG = False
# RELOAD = True
# RELOAD_DIRS = None
# WORKERS = 1
# PROXY_HEADERS = False
# ROOT_PATH = ""
# LIMIT_CONCURRENCY = None
# LIMIT_MAX_REQUESTS = None
# TIMEOUT_KEEP_ALIVE = 5
# TIMEOUT_NOTIFY = 30
# CALLBACK_NOTIFY = None
# SSL_KEYFILE = None
# SSL_CERTFILE = None
# SSL_CA_CERTS = None
# SSL_CIPHERS = "TLSv1"
# HEADERS = None


# 是否使用线程方式运行
IS_THREAD_RUN_METHOD = True

# 底层通用接口配置文件
API_LIST = [
    # {
    #     "name": "stockapi",             # api 名称
    #     "host": HOST,                   # host
    #     "port": 38080,                  # port
    #     "wsgi": "uvicorn",              # wsgi
    #     "module": "run",                # 启动模块名（即应用实例所在的文件名，eg:run.py）
    #     "app": "app"                    # api 实例名（即应用实例所起的变量名）
    # },

    # =============================================================================
    # {
    #     "name": "stockapi",             # api 名称
    #     "host": HOST,                   # host
    #     "port": 38080,                  # port
    #     "wsgi": "gunicorn",             # wsgi
    #     "module": "run",                # 启动模块名（即应用实例所在的文件名，eg:run.py）
    #     "app": "app"                    # api 实例名（即应用实例所起的变量名）
    # },

    # =============================================================================
    {
        "name": "stockapi",             # api 名称
        "host": HOST,                   # host
        "port": 38080,                  # port
        "wsgi": "daphne",               # wsgi
        "module": "run",                # 启动模块名（即应用实例所在的文件名，eg:run.py）
        "app": "app"                    # api 实例名（即应用实例所起的变量名）
    },

]

