from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from . import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('five-names', views.five_names, name='five_names'),
    # path('macro-nutrients/', views.macro_nutrients),
    path('test', views.test_pivot),
    path('macro-nutrients/', views.food_list),
    path('macro-nutrients/<int:pk>', views.food_detail),
    path('macro-nutrients/index/<int:index>', views.food_detail_index),
    path('macro-nutrients/name/<str:name>', views.food_detail_name),
    path('food-groups', views.food_groups),
    # path('docs/', include_docs_urls(title='Food API', public=False)),
    path('docs/', include_docs_urls(title='Food API')),
    # path('load_database', views.load_database),
]