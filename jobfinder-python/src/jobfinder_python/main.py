import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

# FOR LOGGING :
import logging
from logging.handlers import QueueHandler
import atexit
from jobfinder_python.logging.logging import api_logger, logging_config

load_dotenv()


@asynccontextmanager
async def fastapi_lifespan(app: FastAPI):
    # Setup before FastAPI starts

    ## Setup logging
    logging.config.dictConfig(logging_config)
    logging_queue_handler: QueueHandler = logging.getHandlerByName("queue_handler")
    if logging_queue_handler is not None:
        logging_queue_handler.listener.start()
        atexit.register(logging_queue_handler.listener.stop)
    logging.getLogger("root").setLevel(
        logging.INFO
    )  # Set log_level dynamically whenever u want !

    api_logger.info("Setup before FastAPI starts")

    yield

    # Cleanup before fastApi shuts down
    api_logger.info("Cleanup before FastAPI shuts down")


app = FastAPI(
    lifespan=fastapi_lifespan,
    title="JobFinder Python API",
    description="This API handles the job finder part of the project",
)


@app.get("/hello")
def hello():
    return "Hello from FastAPI !!!"


# app.include_router(router=ms_api.router, prefix="/api-python")
# app.include_router(router=ai_api.router, prefix="/api-python")
# app.include_router(router=ai_api.dev_router, prefix="/api-python/dev")


def launch_fastAPI_server():
    fastapi_port = int(os.environ["FASTAPI_PORT"])
    print("FASTAPI PORT : ", fastapi_port)
    fastapi_reload = os.environ["FASTAPI_RELOAD"] == "True"
    if fastapi_reload:
        print("FASTAPI RELOAD IS ENABLED")
    ## SETTING host important for docker !!! (see : https://github.com/tiangolo/fastapi/issues/655 and ESPECIALLY : https://pythonspeed.com/articles/docker-connection-refused/)
    ## USE FOLLOWING LINE WHEN BUILDING FOR DOCKER
    uvicorn.run(
        app="jobfinder_python.main:app",
        reload=fastapi_reload,  # this should be True only when developing locally !
        host="0.0.0.0",  # important for Docker !
        port=fastapi_port,
    )


if __name__ == "__main__":
    launch_fastAPI_server()
