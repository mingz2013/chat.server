# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from BaseModel import BaseModel
from app import db


class FriendShip(BaseModel):
    user = db.ObjectIdField()
    friend = db.ObjectIdField()
