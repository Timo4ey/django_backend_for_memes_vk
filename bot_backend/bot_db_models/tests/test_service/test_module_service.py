import os
from json import loads
from pathlib import Path

import pytest

from bot_backend.bot_db_models.service import (
    has_group_id,
    has_hours_in_dict,
    upd_request_carousel,
    upd_request_data_dict,
)

test_data = None
with open(
    os.path.join(Path(__file__).parent, "test_cases_service.json"), "r"
) as f:
    test_data = loads(f.read())[0]


@pytest.fixture
def carousel_a(db, carousel_factory, content_a):
    return carousel_factory(
        url=test_data["carousel"]["carousel2"]["url"],
        url1=test_data["carousel"]["carousel2"]["url1"],
        url2=test_data["carousel"]["carousel2"]["url2"],
        text=test_data["carousel"]["carousel2"]["text"],
        content_fk=content_a,
    )


def test_has_group_id():
    assert test_data["group"]["group_vk_id"] == has_group_id(
        test_data["group"]
    )


def test_has_hours_in_dict():
    assert test_data["hours"]["hours"] == has_hours_in_dict(test_data["hours"])


def test_upd_request_data_dict():
    ans = test_data["upd"]["upd_data"]
    upd_request_data_dict(ans, "public_date", test_data["upd"]["public_date"])
    assert test_data["upd"]["upd_data2"] == ans


def test_upd_request_carousel(carousel_a):
    upd_request_carousel(
        req_data=test_data["carousel"]["carousel1"], instance=carousel_a
    )

    assert test_data["carousel"]["carousel1"]["url2"] == carousel_a.url2
    assert test_data["carousel"]["carousel1"]["text"] == carousel_a.text
