from odoo import fields, models, api, _
class employee(models.Model):
    # _name = 'mylib.employee'
    _description = 'My Employee'
    _inherit = 'hr.employee'
    nameemp = fields.Char(string='Mã Nhân Viên', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    datepartin = fields.Date('Ngày Được Nhận', default = lambda self: fields.Date.today ())
    classeducate = fields.Many2many('schedule.edu', string="Lớp đào tạo", Select=True)
    extracurricular = fields.Many2many('mylib.extracurricular', string="Hoạt động tham gia", Select=True)

    # category_ids = fields.Many2many(
    #     'hr.employee.category', 'employee_category_rel',
    #     'emp_id', 'category_id',
    #     string='Tags')

    @api.model
    def create(self, vals):
        if vals.get('nameemp', ('New')) == ('New'):
            vals['nameemp'] = self.env['ir.sequence'].next_by_code('hr.employee')
        res = super(employee, self).create(vals)
        return res
