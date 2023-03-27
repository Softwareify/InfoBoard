from copy import copy, deepcopy

from modules.video.models import Video


class VideoService:
    model = Video

    def save_video(self, *, filepath, name):
        new_video = self.model(filepath=filepath, name=name)
        new_video.save()

    @staticmethod
    def update_video(*, instance: Video, filepath=None, name=None):
        filepath_name = copy(instance.filepath.name)
        instance.filepath = filepath
        instance.filepath.name = filepath_name
        instance.name = name
        instance.save()

    @staticmethod
    def validate_filepath(*, filepath_cleaned):
        ext = filepath_cleaned.name.split(".")[-1]
        if ext not in ["mp4"]:
            return False
        return True
