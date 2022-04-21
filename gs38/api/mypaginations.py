from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'records' #gives power to client how much data they want to see on one page.
    max_page_size = 7 # page_size_query_param is set to whatever value like 8, 9 10 anything but if max_page_size is set to 7 then not more than 7 data can be seen on one page.

    last_page_strings = 'end' # default is 'last'
