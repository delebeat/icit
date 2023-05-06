# -*- coding: utf-8 -*-
{
    'name': "del_storable_consumable",

    'summary': """
        This module helps to change Consumable product type to Storable on product page""",

    'description': """
        This module helps to change Consumable product type to Storable on product page
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','product','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
