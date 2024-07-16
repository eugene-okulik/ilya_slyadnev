from locust import task, HttpUser, between


class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_single_post(self):
        self.client.get("/posts/1")

    @task
    def create_post(self):
        data = {"title": "foo", "body": "bar", "userId": 1}
        self.client.post("/posts", json=data)

    @task
    def update_post(self):
        data = {"id": 1, "title": "foo", "body": "bar", "userId": 1}
        self.client.put("/posts/1", json=data)

    @task
    def delete_post(self):
        self.client.delete("/posts/1")
