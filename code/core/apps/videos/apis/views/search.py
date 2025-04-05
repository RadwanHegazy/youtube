from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from apps.videos.documents import VideoDocument
from apps.videos.apis.serializers import VideoDocumentSerializer
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

class VideoSearchView(DocumentViewSet):
    document = VideoDocument
    serializer_class = VideoDocumentSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    
    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
    ]
    
    search_fields = (
        'title',
        'description',
    )
    
    filter_fields = {
        'is_active': 'is_active',
        'owner.id': 'owner.id',
    }