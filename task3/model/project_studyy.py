import odoo
from odoo import  fields, models, _
from odoo.exceptions import UserError
from random import randint


class project_study(models.Model):
    _name = 'project.study'


    name = fields.Char(string="Name", required = True)
    dateline = fields.Date(string="DateLine", required=True)
    status = fields.Selection([
        ('todo', 'TODO'),
        ('in-progress', 'In-Progress'),
        ('review', 'Review'),
        ('done', 'Done')
        ], default='todo', string="Status")
    note = fields.Text(string='Note')
    description = fields.Html(string="Description")
    tag_ids = fields.Many2many('project.tag', string='Tags')
    assign_to = fields.Many2one('res.users','Assign To', default=lambda self: self.env.user)
    customer = fields.Many2one('res.partner','Customer')
    project_manager= fields.Many2one('users',string='Project Managers')
    project_study = fields.Many2one('users',string ='Task Attendees')


    _sql_constraints = [
        ('customer_uniq', 'unique (customer)', "Already exists!"),]


class ProjectTags(models.Model):
    """ Tags of project's tasks """
    _name = "project.tag"
    _description = "Project Tags"

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char('Name', required=True)
    color = fields.Integer(string='Color', default=_get_default_color)
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]


class product(models.Model):
    _name = 'product'

    name = fields.Char(string='Product')


    product_id = fields.Many2one('users', string='Owner')

class project2(models.Model):
    _name = 'project2'


    name =fields.Char(string='Name')

    project_id= fields.Many2one('users',string='Owner')


class users(models.Model):
    _name = 'users'
    name = fields.Char(string='Name')

    list_product = fields.One2many('product','product_id',string='list_product')




