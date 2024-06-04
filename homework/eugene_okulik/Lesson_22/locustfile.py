from locust import task, HttpUser
from random import randrange


class MemesUser(HttpUser):
    token = None
    meme_ids = []

    def on_start(self):
        response = self.client.post(
            '/authorize',
            json={'name': 'Eugene'}
        )
        self.token = response.json()['token']

    @task(2)
    def get_all_memes(self):
        self.client.get(
            '/meme',
            headers={'Authorization': self.token}
        )

    @task(3)
    def get_one_meme(self):
        self.client.get(
            # f'/meme/{randrange(1, 5)}',
            '/meme/1',
            headers={'Authorization': self.token}
        )

    @task
    def post_a_meme(self):
        data = {
            'text': 'kasjhfklajsdhflkajsdhf',
            'url': 'oiuswjehgsiudfyskjdfh',
            'tags': ['tag1'],
            'info': {'key1': 'val1'}
        }
        response = self.client.post(
            '/meme',
            json=data,
            headers={'Authorization': self.token}
        )
        self.meme_ids.append(response.json()['id'])

    def on_stop(self):
        for meme_id in self.meme_ids:
            self.client.delete(
                f'/meme/{meme_id}',
                headers={'Authorization': self.token}
            )
