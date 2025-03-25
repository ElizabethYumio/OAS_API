from django.urls import path
from .views import UserListView, UserDetailView, UserLoginView
from .views import ItemListView, ItemDetailView
from .views import BidListView
from .views import TagListView
from .views import AdminLoginView

user_urlpatterns = [
    path(
        "user", 
        UserListView.as_view(), 
        name = UserListView.name
    ),
    path(
        "user/<uuid:id>", 
        UserDetailView.as_view(), 
        name = UserDetailView.name
    ),
    path(
        "user/login", 
        UserLoginView.as_view(), 
        name = UserLoginView.name
    ),
]

item_urlpatterns = [
    path(
        "item", 
        ItemListView.as_view(), 
        name = ItemListView.name
    ),
    path(
        "item/<uuid:id>",
        ItemDetailView.as_view(),
        name = ItemDetailView.name
    )
]

bid_urlpatterns = [
    path(
        BidListView.path,
        BidListView.as_view(),
        name = BidListView.name
    )
]

tag_urlpatterns = [
    path(
        TagListView.path,
        TagListView.as_view(),
        name = TagListView.name
    )
]

admin_urlpatterns = [
    path(
        "admins/login", 
        AdminLoginView.as_view(), 
        name = AdminLoginView.name
    ),
]

urlpatterns = [
    *user_urlpatterns,
    *item_urlpatterns,
    *bid_urlpatterns,
    *tag_urlpatterns,
    *admin_urlpatterns,
]
