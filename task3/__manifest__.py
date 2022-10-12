{
    'name': "module-relational-field",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mountain",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'data': [
        'view/menu_item.xml',
        'view/project_study.xml',
        'view/product_view.xml',
        'view/list_users_view.xml',
        'view/tag_view.xml',
        'security/ir.model.access.csv'

    ],
    'depends': ['base'],
}