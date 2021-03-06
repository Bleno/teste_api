#!/usr/bin/python
# -*- encoding: utf-8 -*-

# http://api.brlight.net/api/base_ses/reg?$$={%22select%22:[%22json_reg%22],%22literal%22:%22nm_nome%20like%20%27%Lu%%27%22}

class Order_by():
        asc = []
        desc = []
        
        def __init__(self, asc = None, desc = None):
            self.asc = asc
            self.desc = desc
        
class Filters():
    field = None
    term = None
    operation = None

#   def __init__(self,field = None, term = None, operation = None ):
#    self.field = field
#    self.term = term
#    self.operation = operation

class Pesquisa():
    select = []
    filters = [ Filters ]
    literal = None
    limit = None
    offset = None
    order_by = Order_by
    distinct = None
    
    def __init__(self, filters = Filters(), order_by = Order_by()):
        self.filters = [filters]
        self.order_by = order_by
