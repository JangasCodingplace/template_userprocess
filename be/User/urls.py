from django.urls import path, include

urlpatterns = [
    path(
        '',
        include('User.User.urls')
    ),
    path(
        'access/',
        include('User.TemporaryAccess.urls')
    )
]
