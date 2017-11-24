from django.conf.urls import url
# from django.contrib import admin
# from django.conf.urls import include
from views import verify_account
from views import get_borrow_status
from views import query_book
from views import query_all_tags
from controllers import create_book
from controllers import delete_book
from views import renew
urlpatterns = [
    url(r'^verify_account/', verify_account),
    url(r'^get_borrow_status/', get_borrow_status),
    url(r'^query_book/', query_book),
    url(r'^query_all_tags/', query_all_tags),
    url(r'^create_book/', create_book),
    url(r'^delete_book/', delete_book),
    url(r'^renew/', renew),
]