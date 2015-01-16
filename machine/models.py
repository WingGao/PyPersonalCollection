from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Machine(models.Model):
    name = models.CharField(max_length=250, unique=True)


class AliveInfo(models.Model):
    machine = models.ForeignKey(Machine)
    save_ip = models.IPAddressField()
    save_time = models.DateTimeField(auto_now_add=True)


def get_machine(name):
    try:
        m = Machine.objects.get(name=name.strip())
        return m, get_last_info(m)
    except ObjectDoesNotExist:
        return None, None


def get_last_info(machine):
    infoq = AliveInfo.objects.filter(machine=machine).order_by('-id')
    if infoq.count() > 0:
        return infoq[0]
    else:
        return None
