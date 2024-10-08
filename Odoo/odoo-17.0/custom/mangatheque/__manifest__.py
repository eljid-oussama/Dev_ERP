# -*- coding: utf-8 -*-
{
    'name': "mangatheque",

    'summary': """ 
    Application de gestion des mangas
    """,

    'description': """
Cette application vous permet de gérer tous vos managa
    """,

    'author': "JIITOX",
    'website': "https://www.jiitox.com",
    'license': 'LGPL-3',
    'application': True ,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/manga_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/note.xml',
        'views/manga.xml',

        'report/fiche_manga.xml',
        'report/mangatheque.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

