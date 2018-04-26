# -*- coding: utf-8 -*-
from datetime import  datetime, timedelta


def date(delta=-1):
    return datetime.today() + timedelta(delta)