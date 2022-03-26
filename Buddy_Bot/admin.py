from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

from AI_Integrated_Buddy_Bot import settings
from .models import *
from django.contrib.auth.models import Group

# admin.site.unregister(Group)