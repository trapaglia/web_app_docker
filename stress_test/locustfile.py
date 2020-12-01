import time
from locust import HttpUser, task

class QuickstartUser(HttpUser):

    @task(1)
    def index(self):
        raise NotInplementedError

    @task(3)
    def predict(self):
        raise NotInplementedError

    def on_start(self):
        pass
