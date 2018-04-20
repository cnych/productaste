# -*- coding: utf-8 -*-
__author__ = 'ych'
__date__ = '18/04/2018 13:06'
import hashids


def hashid(_id, length=6):
    KEY = 'haimaxy.com'
    hasher = hashids.Hashids(salt=KEY, min_length=length)
    return hasher.encode(_id)
