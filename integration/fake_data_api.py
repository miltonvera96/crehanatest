from integration.generic_client import ApiClient


class FakeData(ApiClient):

    def __init__(self):
        super().__init__(url="https://jsonplaceholder.typicode.com")

    def get_posts(self):
        return self._get("posts")

    def get_post_by_id(self, post_id):
        return self._get(f"posts/{post_id}")

    def get_post_comments_by_id(self, post_id):
        return self._get(f"posts/{post_id}/comments")

    def get_comments_by_post(self, post_id):
        return self._get("comments", params={
            "postId": post_id
        })

    def create_post(self, data):
        return self._post("posts", data=data)

    def update_post(self, post_id, data):
        return self._put(f"posts/{post_id}", data=data)

    def partial_update_post(self, post_id, data):
        return self._patch(f"posts/{post_id}", data=data)

    def delete_post(self, post_id):
        return self._delete(f"posts/{post_id}")


