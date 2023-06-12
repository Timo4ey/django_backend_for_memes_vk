import os
from json import loads
from pathlib import Path

import pytest
from django.urls import reverse

data = None
with open(
    os.path.join(Path(__file__).parent.parent, "tests_cases_models.json"), "r"
) as f:
    data = loads(f.read())[0]


@pytest.mark.django_db
class TestViewsGroups:
    def test_groups_status(self, client):
        self.url = reverse("groups")
        self.response = client.get(self.url)
        assert self.response.status_code == 200


@pytest.mark.django_db
class TestViewsPosts:
    def test_posts_status(self, client):
        self.url = reverse("posts")
        self.response = client.get(self.url)
        assert self.response.status_code == 200


@pytest.mark.django_db
class TestViewsContent:
    def test_content_status(self, client):
        self.url = reverse("content")
        self.response = client.get(self.url)
        assert self.response.status_code == 200


@pytest.mark.django_db
class TestViewsCarousels:
    def test_carouse_status(self, client):
        self.url = reverse("carousel")
        self.response = client.get(self.url)
        assert self.response.status_code == 200


@pytest.mark.django_db
class TestViewTelegramUsers:
    def test_telegram_users_status(self, client):
        self.url = reverse("telegram_users")
        self.response = client.get(self.url)
        assert self.response.status_code == 200


@pytest.mark.django_db
class TestSpecificViewsGroups:
    def test_groups_status(self, client, group_a):
        id = group_a.group_id
        self.url = reverse("specific_group", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert self.response.status_code == 200

    def test_group_name(self, client, group_a):
        id = group_a.group_id
        self.url = reverse("specific_group", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert f'"group_name":"{data["group"]["group_name"]}"' in str(
            self.response.content.decode("utf-8")
        )

    def test_group_vk_id(self, client, group_a):
        id = group_a.group_id
        self.url = reverse("specific_group", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert f'"group_vk_id":{data["group"]["group_vk_id"]}' in str(
            self.response.content.decode("utf-8")
        )


@pytest.mark.django_db
class TestViewsSpecificPosts:
    def test_posts_status(self, client, post_a):
        id = post_a.post_id
        self.url = reverse("specific_post", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert self.response.status_code == 200

    def test_posts_url(self, client, post_a):
        id = post_a.post_id
        self.url = reverse("specific_post", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert f'"url":"{data["post"]["url"]}"' in str(
            self.response.content.decode("utf-8")
        )

    def test_posts_text(self, client, post_a):
        id = post_a.post_id
        self.url = reverse("specific_post", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert f'"text":"{data["post"]["text"]}"' in str(
            self.response.content.decode("utf-8")
        )


@pytest.mark.django_db
class TestViewsSpecificContent:
    def test_content_status(self, client, content_a):
        id = content_a.content_id
        self.url = reverse("specific_content", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert self.response.status_code == 200


@pytest.mark.django_db
class TestViewsSpecificCarousels:
    def test_carousel_status(self, client, carousel_a):
        id = carousel_a.carousel_id
        self.url = reverse("specific_carousel", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert self.response.status_code == 200

    def test_carousel_url(self, client, carousel_a):
        print(carousel_a)
        id = carousel_a.carousel_id
        self.url = reverse("specific_carousel", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert f'"url":"{data["carousel"]["url"]}"' in str(
            self.response.content.decode("utf-8")
        )

    def test_carousel_url1(self, client, carousel_a):
        id = carousel_a.carousel_id
        self.url = reverse("specific_carousel", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert f'"url1":"{data["carousel"]["url1"]}"' in str(
            self.response.content.decode("utf-8")
        )

    def test_carousel_url2(self, client, carousel_a):
        id = carousel_a.carousel_id
        self.url = reverse("specific_carousel", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert f'"url2":"{data["carousel"]["url2"]}"' in str(
            self.response.content.decode("utf-8")
        )

    def test_carousel_text(self, client, carousel_a):
        id = carousel_a.carousel_id
        self.url = reverse("specific_carousel", kwargs={"pk": id})
        self.response = client.get(self.url)
        assert data["carousel"]["text"] in str(
            self.response.content.decode("utf-8")
        )
