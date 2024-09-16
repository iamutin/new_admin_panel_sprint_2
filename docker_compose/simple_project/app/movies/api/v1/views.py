from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from rest_framework.viewsets import ReadOnlyModelViewSet

from .pagination import MoviesPagination
from .serializers import FilmWorkSerializer
from ...models import FilmWork


class MoviesViewSet(ReadOnlyModelViewSet):
    serializer_class = FilmWorkSerializer
    pagination_class = MoviesPagination

    def get_queryset(self):
        queryset = (
            FilmWork.objects.prefetch_related('genres', 'persons').all()
            .annotate(
                actors=ArrayAgg(
                    'persons__full_name',
                    filter=Q(personfilmwork__role='actor'),
                    distinct=True
                )
            )
            .annotate(
                directors=ArrayAgg(
                    'persons__full_name',
                    filter=Q(personfilmwork__role='director'),
                )
            )
            .annotate(
                writers=ArrayAgg(
                    'persons__full_name',
                    filter=Q(personfilmwork__role='writer'),
                )
            )
        )
        return queryset
