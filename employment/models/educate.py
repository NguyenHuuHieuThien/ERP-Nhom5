from odoo import fields, models,api,_


class educate(models.Model):
    _name = 'mylib.educate'
    _description = 'Educate'

    id = fields.Char(string='Mã Dao Tao', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    name = fields.Text("Tên Chương trình")
    start_time = fields.Date("Thoi Gian Bat Dau")
    end_time = fields.Date('Thoi Gian Ket Thuc')
    description = fields.Text("Mo ta khoa hoc")

    @api.model
    def create(self, vals):
        if vals.get('id', ('New')) == ('New'):
            vals['id'] = self.env['ir.sequence'].next_by_code('educate.id') or _('New')
        res = super(educate, self).create(vals)
        return res

