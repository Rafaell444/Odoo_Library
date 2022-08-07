# -*- coding: utf-8 -*-
{
    'name': "Library Management",
    'summary': """ Manage library catalog and book lending. """,
    'author': "Rafael Mkhitaryan",
    'license': "AGPL-3",
    'website': "https://github.com/Rafaell444/Odoo-Books-Catalog",
    'version': '15.0.1.0.0',
    'depends': ['base'],
    'application': True,
    'category': "Services/Library",

    "data": [
        "security/library_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/library_menu.xml",
        "views/book_list_template.xml",
    ]
}
