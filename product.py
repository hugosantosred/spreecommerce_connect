# -*- encoding: utf-8 -*-
#########################################################################
#                                                                       #
# Copyright (C) 2011  Hugo Santos                                       #
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

class product_category(spree_osv.spree_osv):
    _inherit = "product.category"
    
    _columns = {
        'create_date': fields.datetime('Created date', readonly=True),
        'write_date': fields.datetime('Updated date', readonly=True),
        'spree_exportable': fields.boolean('Export To Spree'),
        
    }
    
    def record_category(self, cr, uid, data, external_referential_id):            
        self.ext_import(cr, uid, data, external_referential_id, defaults={})
        
product_category()