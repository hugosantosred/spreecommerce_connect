from osv import osv, fields
import time
import datetime
import netsvc
import urllib
import pycurl
from StringIO import StringIO
import base64
try:
    import json
except:
    raise osv.except_osv(_('Error!'), _('The json module is not installed'))
from base_external_referentials import external_osv
from tools.translate import _

class Connection(object):
    def __init__(self, location, username, password, debug=False):
        #Append / if not there
        if not location[-1] == '/':
            location += '/' 
        self.corelocation = location
        self.location = location + "api/"        
        self.username = username
        self.password = password
        self.debug = debug
        self.result = {}
        self.logger = netsvc.Logger()
    
    def connect(self):
        curl = pycurl.Curl()        
        curl.setopt(curl.USERPWD, '%s:%s' % (str(self.username), str(self.password)))
        self.ser = curl
        return True
    
    def call(self, method, *arguments): 
        if arguments:
            arguments = list(arguments)[0]
        else:
            arguments = []
        response_buffer = StringIO()
        url = self.location + method
        self.ser.setopt(pycurl.URL, str(url))
        self.ser.setopt(pycurl.WRITEFUNCTION, response_buffer.write)
        self.ser.perform()        
        self.ser.close()        
        data = response_buffer.getvalue()
        data = json.loads(data)
        return data
   
    
class spree_osv(external_osv.external_osv):    
    DEBUG = False
    
    def external_connection(self, cr, uid, referential, DEBUG=False):
        attr_conn = Connection(referential.location, referential.apiusername, referential.apipass, DEBUG)
        return attr_conn.connect() and attr_conn or False
    