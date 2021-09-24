   
from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def test1(self):
        self.client.get("http://localhost:5000")

    @task(2)
    def test2(self):
        payload = {"CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}}

        headers = {'content-type': 'application/json'}

        self.client.post("http://localhost:5000/predict", json=payload, headers=headers)
