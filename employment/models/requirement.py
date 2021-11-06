# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class requirement(models.Model):
    _name = 'requirement.educate'
    _description = 'Requirement Educate'

    division = fields.Many2one('hr.department','Bộ Phận Yêu Cầu', select=True)
    petitioner = fields.Many2one('hr.employee', 'Người Yêu Cầu', select=True)
    time = fields.Datetime('Ngày giờ yêu cầu')
    dept = fields.Many2one('hr.department', 'Bộ Phận Nhận Yêu Cầu', select=True)
    dept1 = fields.Many2one('hr.employee', 'Người Nhận Yêu Cầu', select=True)
    positions = fields.Many2one('position.educate', string='Vị Trí')
    number = fields.Integer('Số lượng')
    is_new = fields.Boolean("Là nhân viên mới", default=False)
    is_old = fields.Boolean("Là nhân viên cũ", default=False)
    time_educate = fields.Integer('Thời gian (tháng)')
    status = fields.Selection(
        [('received','Đã tiếp nhận'), ('waiting','Đang chờ'), ('close','Hủy')],"Trạng thái")
    content = fields.Text('Nội dung')
    note = fields.Text('Ghi chú')



    # _sql_constraints = [
    #     ('unique_room', 'unique(room)', u'Phòng đã tồn tại, hãy thử lại!'),
    #     ('unique_name', 'unique(name)', u'Tên môn học đã tồn tại, hãy thử lại!'),
    # ]

    # @api.constrains("room")
    # def _room_validate(self):
    #     for subjects in self:
    #         if len(subjects.room) < 4:
    #             raise exceptions.ValidationError(u"Tên phòng quá ngắn!")
    #
    # @api.constrains("amount")
    # def _amount_validate(self):
    #     for subjects in self:
    #         if subjects.amount < 0:
    #             raise exceptions.ValidationError(u"Số lượng không thể ít hơn được nữa!")
    #
    # @api.onchange("amount")
    # def _amount_onchange(self):
    #     if self.amount == 0:
    #         self.state = 'nghi'
    #     elif self.amount == 3:
    #         self.state = 'hocchinhthuc'
    #     else:
    #         self.state = 'hocbu'
