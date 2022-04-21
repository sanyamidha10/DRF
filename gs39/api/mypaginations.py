from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit' #default is limit
    offset_query_param = 'myoffset' #default is offset
    max_limit = 7 # if max_limit is set to 7 then not more than 7 data can be seen on one page.
