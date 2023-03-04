from flask import Flask, render_template, request
from jaeger_client import Config
from flask_opentracing import FlaskTracing
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
config = Config(
    config={
        "sampler": {"type": "const", "param": 1},
        "logging": True,
        "reporter_batch_size": 1,
    },
    service_name="frontend-service",
)
jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer, True, app)

metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application info", version="1.0.3")


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


@app.route("/")
def homepage():
    return render_template("main.html")


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/403")
def status_code_403():
    status_code = 403
    raise InvalidUsage(
        "Raising status code: {}".format(status_code), status_code=status_code
    )


@app.route("/404")
def status_code_404():
    status_code = 404
    raise InvalidUsage(
        "Raising status code: {}".format(status_code), status_code=status_code
    )


@app.route("/500")
def status_code_500():
    status_code = 500
    raise InvalidUsage(
        "Raising status code: {}".format(status_code), status_code=status_code
    )


@app.route("/503")
def status_code_503():
    status_code = 503
    raise InvalidUsage(
        "Raising status code: {}".format(status_code), status_code=status_code
    )


if __name__ == "__main__":
    app.run()
