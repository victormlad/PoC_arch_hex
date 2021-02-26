from flask import Flask

from app import api
from app.rest.device import device_blueprint

app = Flask('api')
app.register_blueprint(device_blueprint, url_prefix='/devices')


def run():
    app.run(host='0.0.0.0', port=8081)


def main():
    api.start()
    run()


if __name__ == '__main__':
    main()
