# -*- coding: utf-8 -*-
{
    'name': "saba_pickings",

    'summary': """
    adds driver and plate number to the transers
        """,

    'description': """
        -Driver name and plate number for each picking
        -Add Bulk sale confirmation

    """,

    'author': "Vitek",
    'website': "http://www.vitek.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'pcikings',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','sale','branch', 'stock_account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/stock_move.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/sale.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
