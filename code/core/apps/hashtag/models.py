from globals.models import TimestampModel, models
from apps.videos.models import Video
from globals.validators import hastag_name_validator

class Hashtag (TimestampModel) : 
    name = models.CharField(max_length=30, validators=[hastag_name_validator])
    