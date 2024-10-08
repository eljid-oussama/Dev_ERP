# -*- coding: utf-8 -*-

#dictionnaire de description nom ...
{
    'name': "Carpooling application",
    'version' : '1.0',

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
      Module to help you organize the traject with your employees.
       Make your life easier !
    """,

    'author': "JIITOX",
    'website': "https://www.yourcompany.com",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Cutomizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','product', 'contacts', 'survey'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'security/ir_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/carpooling_views.xml',
        'views/res_partner.xml',
        'wizard/carpooling_wizard_view.xml',
        'views/carpooling_menus.xml',
        'views/sale_order_views.xml',
        'views/product_template_views.xml',
        'views/website_templates.xml',
        'views/survey_survey_views.xml',
        'data/ir_cron.xml',


        'reports/car_report.xml',
        'reports/zpl_report.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

