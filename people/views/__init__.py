# -*- coding: utf-8 -*-

from people.views.handle import register, login, logout, user, au_top , user_topics, user_comments
from people.views.settings import profile, password
from people.views.follow import follow, following, un_follow


class MyMiddleware(object):
    def process_request(self, request):
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META["REMOTE_ADDR"]

        if request.user.is_authenticated():
            request.user.last_ip = ip
            request.user.save()

        return None
