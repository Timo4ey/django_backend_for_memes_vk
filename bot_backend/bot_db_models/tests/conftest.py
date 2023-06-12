import os
from json import loads
from pathlib import Path

import pytest

from bot_backend import settings
from bot_backend.bot_db_models.models import Carousels, Content, Groups, Posts

with open(
    os.path.join(Path(__file__).parent, "tests_cases_models.json"), "r"
) as f:
    data = loads(f.read())[0]


@pytest.fixture(scope="function")
def django_db_setup():
    settings.DATABASES["TEST"]


# Group
@pytest.fixture
def group_factory(db):
    def create_group(group_vk_id: int, group_name: str):
        group = Groups.objects.create(
            group_vk_id=group_vk_id, group_name=group_name
        )
        return group

    return create_group


@pytest.fixture
def group_a(db, group_factory):
    return group_factory(
        data["group"]["group_vk_id"], data["group"]["group_name"]
    )


# ---------------------------------------------------------
# Content


@pytest.fixture
def content_factory(db):
    def create_default_content(content_vk_id, group_id_fk, public_date):
        content = Content.objects.create(
            content_vk_id=content_vk_id,
            group_id_fk=group_id_fk,
            public_date=public_date,
        )
        return content

    return create_default_content


@pytest.fixture
def content_a(db, content_factory, group_a):
    group = group_a
    return content_factory(
        content_vk_id=data["content"]["content_vk_id"],
        group_id_fk=group,
        public_date=data["content"]["public_date"],
    )


# ---------------------------------------------------------
# Carousel


@pytest.fixture
def carousel_factory(db):
    def create_default_carousel(
        url,
        content_fk,
        url1,
        url2="",
        url3="",
        url4="",
        url5="",
        url6="",
        url7="",
        url8="",
        url9="",
        text="",
    ):
        carousel = Carousels.objects.create(
            url=url,
            url1=url1,
            url2=url2,
            url3=url3,
            url4=url4,
            url5=url5,
            url6=url6,
            url7=url7,
            url8=url8,
            url9=url9,
            text=text,
            content_fk=content_fk,
        )
        return carousel

    return create_default_carousel


@pytest.fixture
def carousel_a(db, carousel_factory, content_a):
    return carousel_factory(
        url=data["carousel"]["url"],
        url1=data["carousel"]["url1"],
        url2=data["carousel"]["url2"],
        text=data["carousel"]["text"],
        content_fk=content_a,
    )


# ---------------------------------------------------------
# Posts


@pytest.fixture
def posts_factory(db):
    def create_default_post(url, text, content_fk):
        post = Posts.objects.create(
            url=url,
            text=text,
            content_fk=content_fk,
        )
        return post

    return create_default_post


@pytest.fixture
def post_a(db, posts_factory, content_a):
    return posts_factory(
        url=data["post"]["url"],
        text=data["post"]["text"],
        content_fk=content_a,
    )
