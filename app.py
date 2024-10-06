import logging
import threading

from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api

from src.container import Container
from src.shared.infrastructure.config.config import Config
from src.shared.infrastructure.rest.error_handler import handle_exception

load_dotenv()

logging.basicConfig(level=logging.INFO,
                    format='{"dateTime": "%(asctime)s", "level": "info", "message": "%(message)s"}',
                    datefmt='%Y-%m-%d %H:%M:%S')

def create_app():
    flask_app = Flask(__name__)
    # flask_app.register_blueprint(Container.team_controller().routes(), url_prefix='/teams')
    flask_app.register_error_handler(Exception, handle_exception)
    api = Api(flask_app, version='1.0', title='My API', description='A simple Flask-RESTX API')


    return flask_app


async def start_consumers():
    bus = Container.event_bus()
    await bus.listen()

if __name__ == '__main__':
    t1 = threading.Thread(target=start_consumers)
    t1.daemon = True
    t1.start()

    app = create_app()
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)