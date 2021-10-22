from odoo import fields, models
class employee(models.Model):
    # _name = 'mylib.employee'
    _description = 'My Employee'
    _inherit = 'hr.employee'


    # category_ids = fields.Many2many(
    #     'hr.employee.category', 'employee_category_rel',
    #     'emp_id', 'category_id',
    #     string='Tags')

