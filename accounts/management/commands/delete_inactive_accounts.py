from django.core.management import BaseCommand
from accounts.models import Account
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        accounts = Account.objects.filter(is_active=False)
        if accounts:
            accounts_to_be_deleted = []
            for i in accounts:
                accounts_to_be_deleted.append(i.email)
            f = open("delete_account_log.txt", "a")
            f.write("Accounts deleted: "+ str(accounts_to_be_deleted) +" at "+ str(datetime.now()) +"\n")
            f.close()
            accounts.delete()
        else:
            f = open("delete_account_log.txt", "a")
            f.write("Cron successfully ran at: "+ str(datetime.now()) + ". No invalid accounts found!\n")
            f.close()