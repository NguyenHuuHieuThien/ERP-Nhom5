from odoo import fields, models,api,_


class educate(models.Model):
    _name = 'mylib.extracurricular'
    _description = 'Extracurricular'

    # id = fields.Char(string='Mã Dao Tao', required=True, copy=False, readonly=True,
    #                    default=lambda seft: _('New'))
    name = fields.Text("Tên Hoạt Động")
    time_happend = fields.Date("Thời Gian Diễn Ra")
    state = fields.Selection(
        [('sapdienra','Sắp diễn ra'), ('dangdienra','Đang diễn ra'), ('dadienra','Đã diễn ra')],"Trạng Thái")
    description = fields.Text()
    address = fields.Text("Địa điểm")
    person = fields.Many2many('hr.employee', string="Nhân viên tham gia")

    # @api.model
    # def create(self, vals):
    #     if vals.get('id', ('New')) == ('New'):
    #         vals['id'] = self.env['ir.sequence'].next_by_code('educate.id') or _('New')
    #     res = super(educate, self).create(vals)
    #     return res

