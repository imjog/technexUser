from django.core.management.base import BaseCommand, CommandError
from Auth.models import *
#from getpass import getpass
import sys


class Command(BaseCommand):
    args="arguments are not needed"
    help = "sends new openvpn password"

    def handle(self, *args,**options):
        ws=Way2smsAccount.objects.all()
        for w in ws:
            w.messages_left=100
            w.save()
        ws=Way2smsAccount_Premium.objects.all()
        for w in ws:
            w.messages_left=100
            w.save()