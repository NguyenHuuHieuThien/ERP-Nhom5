# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class schedule(models.Model):
    _name = 'schedule.edu'
    _description = 'Class Educate'


    name = fields.Char(string='ID', required=True, copy=False, readonly=True,
                       default=lambda seft: _('New'))
    Classname = fields.Text('Tên khóa học', required=True)
    startday = fields.Date('Ngày Bắt Đầu', required=True)
    endday = fields.Date('Ngày Kết Thúc', required=True)
    mentor = fields.Many2one('hr.employee', string='Người phụ trách', select=True)
    Address = fields.Text('Địa điểm')
    capacity = fields.Integer('Sĩ số')
    nbofweek = fields.Integer('Số Buổi Trong Tuần')
    telephone = fields.Integer('Số điện Thoại')
    email = fields.Text('Email')
    seat = fields.Integer('Số chỗ ngồi')
    course = fields.Many2one('classlist.educate',string='Khóa đào tạo')
    WeekDays = fields.Selection([
        ('Thứ hai', 'Thứ hai'),
        ('Thứ ba', 'Thứ ba'),
        ('Thứ tư', 'Thứ tư'),
        ('Thứ năm', 'Thứ năm'),
        ('Thứ sáu', 'Thứ sáu'),
        ('Thứ bảy', 'Thứ bảy')
    ], string='Thứ', default='Thứ hai')
    request_hour_from = fields.Selection([
        ('0', '12:00 AM'), ('0.5', '12:30 AM'),
        ('1', '1:00 AM'), ('1.5', '1:30 AM'),
        ('2', '2:00 AM'), ('2.5', '2:30 AM'),
        ('3', '3:00 AM'), ('3.5', '3:30 AM'),
        ('4', '4:00 AM'), ('4.5', '4:30 AM'),
        ('5', '5:00 AM'), ('5.5', '5:30 AM'),
        ('6', '6:00 AM'), ('6.5', '6:30 AM'),
        ('7', '7:00 AM'), ('7.5', '7:30 AM'),
        ('8', '8:00 AM'), ('8.5', '8:30 AM'),
        ('9', '9:00 AM'), ('9.5', '9:30 AM'),
        ('10', '10:00 AM'), ('10.5', '10:30 AM'),
        ('11', '11:00 AM'), ('11.5', '11:30 AM'),
        ('12', '12:00 PM'), ('12.5', '12:30 PM'),
        ('13', '1:00 PM'), ('13.5', '1:30 PM'),
        ('14', '2:00 PM'), ('14.5', '2:30 PM'),
        ('15', '3:00 PM'), ('15.5', '3:30 PM'),
        ('16', '4:00 PM'), ('16.5', '4:30 PM'),
        ('17', '5:00 PM'), ('17.5', '5:30 PM'),
        ('18', '6:00 PM'), ('18.5', '6:30 PM'),
        ('19', '7:00 PM'), ('19.5', '7:30 PM'),
        ('20', '8:00 PM'), ('20.5', '8:30 PM'),
        ('21', '9:00 PM'), ('21.5', '9:30 PM'),
        ('22', '10:00 PM'), ('22.5', '10:30 PM'),
        ('23', '11:00 PM'), ('23.5', '11:30 PM')], string='Bắt đầu từ:')
    request_hour_to = fields.Selection([
        ('0', '12:00 AM'), ('0.5', '12:30 AM'),
        ('1', '1:00 AM'), ('1.5', '1:30 AM'),
        ('2', '2:00 AM'), ('2.5', '2:30 AM'),
        ('3', '3:00 AM'), ('3.5', '3:30 AM'),
        ('4', '4:00 AM'), ('4.5', '4:30 AM'),
        ('5', '5:00 AM'), ('5.5', '5:30 AM'),
        ('6', '6:00 AM'), ('6.5', '6:30 AM'),
        ('7', '7:00 AM'), ('7.5', '7:30 AM'),
        ('8', '8:00 AM'), ('8.5', '8:30 AM'),
        ('9', '9:00 AM'), ('9.5', '9:30 AM'),
        ('10', '10:00 AM'), ('10.5', '10:30 AM'),
        ('11', '11:00 AM'), ('11.5', '11:30 AM'),
        ('12', '12:00 PM'), ('12.5', '12:30 PM'),
        ('13', '1:00 PM'), ('13.5', '1:30 PM'),
        ('14', '2:00 PM'), ('14.5', '2:30 PM'),
        ('15', '3:00 PM'), ('15.5', '3:30 PM'),
        ('16', '4:00 PM'), ('16.5', '4:30 PM'),
        ('17', '5:00 PM'), ('17.5', '5:30 PM'),
        ('18', '6:00 PM'), ('18.5', '6:30 PM'),
        ('19', '7:00 PM'), ('19.5', '7:30 PM'),
        ('20', '8:00 PM'), ('20.5', '8:30 PM'),
        ('21', '9:00 PM'), ('21.5', '9:30 PM'),
        ('22', '10:00 PM'), ('22.5', '10:30 PM'),
        ('23', '11:00 PM'), ('23.5', '11:30 PM')], string='Đến: ')
    note = fields.Text(string='Ghi chú')



    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('schedule.edu') or _('New')
        res = super(schedule, self).create(vals)
        return res

    # @api.constrains("nbofweek")
    # def _nbofweek_validate(self):
    #     for classlist in self:
    #         if classlist.nbofweek < 1:
    #             raise exceptions.ValidationError(u"Số buổi tối thiểu là 1!")
    #
    # @api.constrains('endday')
    # def onchange_date(self):
    #     if (self.startday and self.endday) and (self.endday < self.startday):
    #         raise exceptions.ValidationError(u'Ngày bắt đầu phải nhỏ hơn ngày kết thúc.')
    #
    # @api.constrains("capacity")
    # def _capacity_validate(self):
    #     for classlist in self:
    #         if classlist.capacity < 1:
    #             raise exceptions.ValidationError(u"Sĩ số tối thiểu là 1!")
    #
    # _sql_constraints = [
    #     ('unique_name', 'unique(name)', u'Tên khóa học đã tồn tại, hãy thử lại!'),
    #     ('unique_Classname', 'unique(Classname)', u'Tên lớp đào tạo đã tồn tại, hãy thử lại!'),
    #
    # ]







