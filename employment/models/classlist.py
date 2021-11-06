# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class classlist(models.Model):
    _name = 'classlist.educate'
    _description = 'Classlist Educate'

    name = fields.Char(string='ID', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    nameeducate = fields.Char('Tên Khóa Học', required=True)
    department = fields.Many2one('hr.department', string='Bộ Phận', select=True)
    startday = fields.Date('Ngày Bắt Đầu', required=True)
    endday = fields.Date('Ngày Kết Thúc', required=True)
    content = fields.Text('Nội dung', required=True)
    mentor = fields.Many2one('hr.employee', string='Người phụ trách', select=True)
    educate_image = fields.Binary("Hình Ảnh", attachment=True, help="Hình Ảnh")
    capacity = fields.Integer('Số lớp')
    note = fields.Text(string='Ghi chú')
    telephone = fields.Integer('Số điện Thoại')
    email = fields.Text('Email')
    numberemp = fields.Integer('Số lượng nhân viên')
    target = fields.Text('Mục tiêu đào tạo')
    level = fields.Selection([('coban','Cơ bản'),('nangcao','Nâng cao')],"Mức độ đào tạo")
    anotherrqm = fields.Text("Yêu cầu khác")
    specialrqm = fields.Text("Yêu cầu đặc biệt")
    schedules = fields.One2many('schedule.edu','course' ,string='Lớp Đào Tạo')




    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('classlist.educate') or _('New')
        res = super(classlist, self).create(vals)
        return res

    @api.constrains("nbofweek")
    def _nbofweek_validate(self):
        for classlist in self:
            if classlist.nbofweek < 1:
                raise exceptions.ValidationError(u"Số buổi tối thiểu là 1!")

    @api.constrains('endday')
    def onchange_date(self):
        if (self.startday and self.endday) and (self.endday < self.startday):
            raise exceptions.ValidationError(u'Ngày bắt đầu phải nhỏ hơn ngày kết thúc.')

    @api.constrains("capacity")
    def _capacity_validate(self):
        for classlist in self:
            if classlist.capacity < 1:
                raise exceptions.ValidationError(u"Sĩ số tối thiểu là 1!")

    _sql_constraints = [
        ('unique_name', 'unique(nameeducate)', u'Tên khóa học đã tồn tại, hãy thử lại!'),

    ]




