from custom.selectors import BaseSelector

from .models import Video


class VideoSelector(BaseSelector):
    model = Video
