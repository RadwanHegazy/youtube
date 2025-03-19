from celery import shared_task
from globals.resolution_parser import ResolutionParser
from apps.video_media.models import Video, VideoMedia

@shared_task
def parse_resolutions(vid_id) :

    try :
        video_model = Video.objects.get(id=vid_id) 
    except Video.DoesNotExist:
        return 
    
    parser = ResolutionParser(video_model.original_video.path)
    parser.create_multiple_resolutions('media/video-media/')
    results = parser.get_results()

    video_model.duration = parser.get_duration()

    for res in results:
        path, quality = res['path'], res['quality']

        vid_med = VideoMedia.objects.create(
            video=video_model,
            path=path,
            quality=quality
        )

        vid_med.save()
    
    video_model.is_active = True
    video_model.save()
