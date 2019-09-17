# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.

#     def __call__(self, request):
#         if not request.user.is_authenticated():
#             # or http response
#             return HttpResponseRedirect(reverse('landing_page'))
#         return None
#         # print(type(request))
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.

#         response = self.get_response(request)

#         # Code to be executed for each request/response after
#         # the view is called.

#         return response

from django.http import HttpResponseRedirect
from django.shortcuts import reverse


class AuthRequiredMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated():
            # or http response
            return HttpResponseRedirect(reverse('landing_page'))

        return self.get_response(request)

    # def process_request(self, request):

    #     return None
