import os
from json import loads
from pathlib import Path

import dotenv
import pytest

from bot_backend.bot_db_models.models import Carousels, Content, Groups, Posts

dotenv.load_dotenv()


data = None
with open(
    os.path.join(Path(__file__).parent.parent, "tests_cases_models.json"), "r"
) as f:
    data = loads(f.read())[0]


@pytest.mark.django_db()
class TestGroups:
    def test_create_group(self):
        Groups.objects.create(group_vk_id=221003459, group_name="Котики AI")
        assert (
            Groups.objects.get(group_name="Котики AI").group_name
            == "Котики AI"
        )


class TestsContent:
    def test_content_is_correct(self, group_a):
        self.content = Content.objects.create(
            content_vk_id=data["content"]["content_vk_id"],
            group_id_fk=group_a,
            public_date=data["content"]["public_date"],
        )
        assert data["content"]["content_vk_id"] == self.content.content_vk_id
        assert data["content"]["public_date"] == self.content.public_date


class TestPosts:
    def test_posts_is_correct(self, content_a):
        self.post = Posts.objects.create(
            url=data["post"]["url"],
            text=data["post"]["text"],
            content_fk=content_a,
        )
        assert data["post"]["url"] == self.post.url
        assert data["post"]["text"] == self.post.text


class TestCarousel:
    def test_carousel_is_correct(self, content_a):
        self.carousel = Carousels.objects.create(
            url=data["carousel"]["url"],
            url1=data["carousel"]["url1"],
            content_fk=content_a,
        )
        assert data["carousel"]["url"] == self.carousel.url
        assert data["carousel"]["url1"] == self.carousel.url1
