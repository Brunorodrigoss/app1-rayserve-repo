import ray
from fastapi import FastAPI
from ray import serve

app = FastAPI()

@serve.deployment
@serve.ingress(app)
class App1Deployment:
    @app.get("/")
    def root(self):
        return "Hello, App1!"

app1_test = App1Deployment.bind()
