from locust import HttpUser, between, task
import random

class CarparkUser(HttpUser):
    wait_time = between(1, 10)

    @task
    def index(self):
        self.client.get("/")

    @task
    def add_car(self):
        with self.client.post("/add", {"reg": str(random.randint(0,20)), "type": "Car"}, catch_response=True) as response:
            if response.status_code <= 400:
                response.success()

    @task
    def remove_car(self):
        self.client.post("/remove", {"reg": str(random.randint(0, 20))})