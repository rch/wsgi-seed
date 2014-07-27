import sys, json, flask, datetime, random, hashlib
from flask import request, session, current_app
from itertools import imap, count
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR
from uuid import uuid4
from container import db

class TreeProvider(object):
    
    key = 'ctx_data'
    
    def __init__(self, message=None, cdata=None):
        self.data = []
        self.cdata = cdata
        self.parms = message.data
    
    def __call__(self, params):
        method = getattr(self, params['method'])
        return method(params)
   
    def items(self, params=None):
        tree = [{
            'id': 'root',
            'displayName': 'root',
            'displayType': 'engine',
            'leaf': False,
            'children':[],
        }]
        return {"total": len(tree), "data":tree, "success":True}
