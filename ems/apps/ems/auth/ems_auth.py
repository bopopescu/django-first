from apps.ems.models import User


class Backend:
    """
    Custom authentication
    """

    def authenticate(self, request, username=None, password=None):
        print(username, password)
        try:
            user = User.objects.filter(
                username=username, password=password, is_active=True).first()
            
            return user
        except Exception as ex:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
