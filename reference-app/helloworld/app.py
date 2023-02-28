from flask import Flask

from jaeger_client import Config
from flask_opentracing import FlaskTracing

app = Flask(__name__)
config = Config(
    config={
        "sampler": {"type": "const", "param": 1},
        "logging": True,
        "reporter_batch_size": 1,
    },
    service_name="helloworld-service",
)
jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer, True, app)


@app.route("/")
def hello():
    return "Hello from Python!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
