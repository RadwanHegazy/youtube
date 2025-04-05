from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Video
from django.contrib.auth import get_user_model

User = get_user_model()

@registry.register_document
class VideoDocument(Document):
    owner = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(),
        'full_name': fields.TextField(),
        'picture': fields.FileField(),
    })
    
    class Index:
        name = 'videos'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    
    class Django:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'created_at',
            'viewers_counter',
            'duration',
            'is_active',
        ]
        related_models = [User]
    
    def get_instances_from_related(self, related_instance):
        """If related user updates, update video documents"""
        if isinstance(related_instance, User):
            return related_instance.video_owner.all()
    
    def prepare_owner(self, instance):
        return {
            'id': instance.owner.id,
            'username': instance.owner.username,
            'full_name': instance.owner.full_name,
            'picture': instance.owner.picture.url if instance.owner.picture else None,
        }
    
    def prepare_thumbnail(self, instance):
        return instance.thumbnail.url if instance.thumbnail else None