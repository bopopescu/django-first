from catalog.models import Members

class Backend:
    """
    Custom authentication
    """

    def authenticate(self, request, username=None, password=None):
        print(username, password)
        try:
            user = Member.objects.filter(
                username=username, password=password, is_active=True).first()
            user.no_visits += 1
            user.save()
            return user
        except Exception as ex:
            return None
        return None

    def get_user(self, user_id):
        try:
            return Members.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
