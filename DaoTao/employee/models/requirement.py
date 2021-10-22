# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class requirement(models.Model):
    _name = 'requirement.educate'
    _description = 'Requirement Educate'

    dept = fields.Text('Bộ phận yêu cầu')
    position = fields.Selection(
        [('webfrontend','Web Front End'), ('backend','Web Back End'), ('qa','QA'), ('bi','BI'), ('datascience','Data Science')],"Vị Trí")
    time_educate = fields.Integer('Thời gian đào tạo(tháng)')
    content = fields.Text('Nội dung')
    note= fields.Text('Ghi chú')





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
