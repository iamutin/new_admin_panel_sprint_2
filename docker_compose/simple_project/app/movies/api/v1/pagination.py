from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MoviesPagination(PageNumberPagination):
    page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'prev': self.previous_page_number(),
            'next': self.next_page_number(),
            'results': data
        })

    def next_page_number(self) -> int | None:
        if self.page.paginator.num_pages > self.page.number:
            return self.page.next_page_number()

    def previous_page_number(self) -> int | None:
        if self.page.number > 1:
            return self.page.previous_page_number()
