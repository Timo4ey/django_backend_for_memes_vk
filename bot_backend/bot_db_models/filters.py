from datetime import datetime, timedelta

from .models import Carousels, Content, Posts


def get_ids_for_specific_period(hour: int):
    dt = datetime.strftime(
        (datetime.today() - timedelta(hours=int(hour))), "%Y-%m-%d %H:%M:%S"
    )
    content_qs = Content.objects.filter(save_date__gt=dt).values_list(
        "content_id", flat=True
    )
    return content_qs


def get_posts_for_specific_period(hour: int):
    """Getting a query set of posts"""
    content_qs = get_ids_for_specific_period(hour)
    posts_qs = Posts.objects.filter(content_fk__in=content_qs)
    return posts_qs


def get_carousels_for_specific_period(hour):
    """Getting a query set of carousels"""
    content_qs = get_ids_for_specific_period(hour)
    carousels_qs = Carousels.objects.filter(content_fk__in=content_qs)
    return carousels_qs
