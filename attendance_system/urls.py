"""attendance_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from rest_framework.routers import DefaultRouter
from django.views.static import serve
from attendance_system.settings import MEDIA_ROOT

from users.views import UserViewset, SecurityViewset, QQLoginViewset

from dormitories.views import DormitoryViewset, WaterFeesViewset, ElectricityFeesViewset
from user_operation.views import WaterFeesLogViewset, ElectricityFeesLogViewset, RepairViewset, RepairLogViewset, FeesRechargeOrderViewset
from access_control.views import AccessControlViewset
from system_setting.views import SystemSettingViewset, SystemLogViewset

router = DefaultRouter()
router.register(r'users', UserViewset, basename="users")
router.register(r'dormitories', DormitoryViewset, basename="dormitories")
router.register(r'water_fees', WaterFeesViewset, basename="water_fees")
router.register(r'water_fees_log', WaterFeesLogViewset, basename="water_fees_log")
router.register(r'electricity_fees', ElectricityFeesViewset, basename="electricity_fees")
router.register(r'electricity_fees_log', ElectricityFeesLogViewset, basename="electricity_fees_log")
router.register(r'repair', RepairViewset, basename="repair")
router.register(r'repair_log', RepairLogViewset, basename="repair_log")
router.register(r'access_control', AccessControlViewset, basename="access_control")
router.register(r'system_setting', SystemSettingViewset, basename="system_setting")
router.register(r'system_log', SystemLogViewset, basename="system_log")
router.register(r'fees_recharge_order', FeesRechargeOrderViewset, basename="fees_recharge_order")

router.register(r'member/security', SecurityViewset, basename="security")
router.register(r'user/login_qq', QQLoginViewset, basename="login_qq")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),
    url(r'^token-verify/', verify_jwt_token)
]
