from bot_backend.bot_db_models.models import Carousels


# GroupsListView
def has_group_id(data: dict) -> bool:
    """Response True if the dict has key `group_vk_id` else False
    `return data.get('group_vk_id', False)`
    """
    return data.get("group_vk_id", False)  # 39 71 320


def has_hours_in_dict(request: dict) -> bool:
    """Response True if the dict has key `hours` else False
    `return request.GET.get('hours', False)`
    """
    return request.get("hours", False)  # 226


def upd_request_data_dict(
    data: dict, field_name: str, field_value: int
) -> None:
    """Update a key in a dict
    `data.update({field_name: field_value})`
    """
    data.update({field_name: field_value})
    # 40 72 97 168 240


def upd_request_carousel(req_data: dict, instance: Carousels) -> None:
    """Update several keys in a dict"""
    key_words = {"url", "url1", "url2", "text", "content_id", "carousel_id"}
    data = instance.__dict__
    for key in data:
        if key in key_words:
            req_data[key] = data.get(key)  # 279
