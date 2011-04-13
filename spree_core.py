#########################################################################
#                                                                       #
# Copyright (C) 2011 Hugo Santos                                        #
#                                                                       #
#This program is free software: you can redistribute it and/or modify   #
#it under the terms of the GNU General Public License as published by   #
#the Free Software Foundation, either version 3 of the License, or      #
#(at your option) any later version.                                    #
#                                                                       #
#This program is distributed in the hope that it will be useful,        #
#but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#GNU General Public License for more details.                           #
#                                                                       #
#You should have received a copy of the GNU General Public License      #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################

from osv import osv, fields
import spree_osv
import tools
from base_external_referentials import external_osv
DEBUG = False

class external_referential(spree_osv.spree_osv):    
    
    _inherit = "external.referential"
    
    _columns = {
            'active': fields.boolean('Active')
    }
    _defaults = {
            'active': lambda *a: 1,
    }
    
    def sync_categs(self, cr, uid, ids, context):
        instances = self.browse(cr, uid, ids, context)
        for inst in instances:
            pro_cat_conn = self.external_connection(cr, uid, inst, DEBUG)
            categ_data = pro_cat_conn.call('taxons/1.json', [0])   
            self.pool.get('product.category').record_category(cr, uid, categ_data, 1)
        return True
external_referential()