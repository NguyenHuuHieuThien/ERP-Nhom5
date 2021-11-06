# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import date


class position(models.Model):
    _name = 'position.educate'
    _description = 'Position Educate'

    name = fields.Text('Tên Vị Trí')
    date_position = fields.Date('Ngày tạo',default = lambda self: fields.Date.today ())
    description = fields.Text('Mô tả chi tiết')

    _sql_constraints = [
        ('unique_name', 'unique(name)', u'Tên vị trí đã tồn tại!'),
    ]

    # @api.constrains('date_position')
    # def onchange_date(self):
    #     if  self.date_position > date.today():
    #         raise exceptions.ValidationError(u'Ngày bắt đầu phải nhỏ hơn ngày kết thúc.')



