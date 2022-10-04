# Root view import:
from messages.notifications.api.views.root import NotificationsRootView

# View import:
from .views.notification import NotificationView

# Base default route import:
from network.all.base_api.base_default_router import BaseDefaultRouter

# Register router:
router = BaseDefaultRouter()

# App name registration:
app_name = 'api-notifications'

# Root api view route registration:
router.APIRootView = NotificationsRootView

# Standard view route registration:
router.register(r'notifications', NotificationView, basename='notifications')

# Add urlpatterns:
urlpatterns = router.urls
