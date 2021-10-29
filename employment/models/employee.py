from odoo import fields, models
class employee(models.Model):
    # _name = 'mylib.employee'
    _description = 'My Employee'
    _inherit = 'hr.employee'

    datepartin = fields.Date('Ngày Được Nhận', default = lambda self: fields.Date.today ())
    classeducate = fields.Many2many('classlist.educate', string="Lop dao tao", Select=True)
    extracurricular = fields.Many2many('mylib.extracurricular', string="hoat dong tham gia", Select=True)

    # category_ids = fields.Many2many(
    #     'hr.employee.category', 'employee_category_rel',
    #     'emp_id', 'category_id',
    #     string='Tags')

