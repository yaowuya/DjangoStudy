from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPageNumberPagination(PageNumberPagination):
    # 1,默认的大小
    page_size = 10
    # 2,前端可以指定页面大小
    page_query_param = 'page_size'
    # 3,页面的最大大小
    max_page_size = 5

    def get_paginated_response(self, data):
        return Response(
            dict(
                page=self.page.number,
                total_page=self.page.paginator.num_pages,
                count=self.page.paginator.count,
                # next=self.get_next_link(),
                # pervious=self.get_previous_link(),
                data=data
            )
        )
