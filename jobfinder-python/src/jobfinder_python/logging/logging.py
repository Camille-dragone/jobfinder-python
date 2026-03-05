import logging

# Inspired from : https://www.youtube.com/watch?v=9L77QExPmI0&ab_channel=mCoding

app_logger = logging.getLogger("jobfinder")
api_logger = app_logger.getChild("api")


logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s : %(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(message)s"
        },
        "detailed": {
            "format": "%(levelname)s : %(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(lineno)s : %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
        # "custom_json_formatter": {
        #     "()": "ergonova_ai.logging.custom_json_logger.CustomJSONFormatter",
        #     "fmt_keys": {
        #         "level": "levelname",
        #         "message": "message",
        #         "timestamp": "timestamp",
        #         "logger": "name",
        #         "module": "module",
        #         "function": "funcName",
        #         "line": "lineno",
        #         "thread_name": "threadName",
        #     },
        # },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            # "formatter": "simple",
            "formatter": "detailed",
            # "formatter": "custom_json_formatter",
            "stream": "ext://sys.stdout",
        },
        "stdout_json": {
            "class": "logging.StreamHandler",
            # "formatter": "custom_json_formatter",
            "stream": "ext://sys.stdout",
        },
        "queue_handler": {
            "class": "logging.handlers.QueueHandler",
            # "handlers": ["stdout", "stdout_json"],
            "handlers": ["stdout"],
            "respect_handler_level": True,
            # TODO : SET HANDLER(s) in function of ENV Variables
        },
    },
    "loggers": {
        # "root": {"handlers": ["stdout_json"]},
        # "root": {"handlers": ["stdout", ]},
        "root": {
            "handlers": [
                "queue_handler",
            ]
        },
    },
}
