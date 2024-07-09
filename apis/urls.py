from django.urls import include, path
from rest_framework import routers
from apis import views
from .views import restaurantview
from .views import userview
from .views import adminview

router = routers.DefaultRouter()
router.register(r'restaurants', views.restaurantview.RestaurantViewSet, basename='restaurants')
router.register(r'foods', views.restaurantview.FoodViewSet, basename='foods')
router.register(r'meals', views.restaurantview.MealViewSet, basename='meals')
router.register(r'menus', views.restaurantview.MenuViewSet, basename='menus')
router.register(r'menu_items', views.restaurantview.MenuItemViewSet, basename='menu_items')

router.register(r'users', views.userview.UserViewSet, basename='users')
router.register(r'admin', views.adminview.AdminViewSet, basename='admin')
router.register(r'admin_logout', views.adminview.AdminLogoutViewSet, basename='admin_logout')
# router.register(r'login', views.userview.LoginViewSet, basename='login')
router.register(r'logout', views.userview.LogoutViewSet, basename="logout")
router.register(r'university', views.userview.UniversityViewSet, basename='university')
router.register(r'profiles', views.userview.ProfileViewSet, basename='profiles')
router.register(r'financials', views.userview.FinancialViewSet, basename='financials')
router.register(r'reservations', views.userview.ReservationViewSet, basename='reservations')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.userview.LoginViewSet.as_view(), name='login'),
]
