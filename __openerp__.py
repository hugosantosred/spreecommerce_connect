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
{
    "name" : "Spree Commerce",
    "version" : "0.1",
    "depends" : ["base",
                 "product",
                 "product_m2mcategories",
                 'delivery',
                 "base_sale_multichannels",                 
                ],
    "author" : "Hugo Santos",
    "description": """Spree Commerce connector for Openerp
""",
    "website" : "http://www.ting.es",
    "category" : "Generic Modules",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : ['spree_core_view.xml'],
    "active": False,
    "installable": True,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

