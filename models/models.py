# -*- coding: utf-8 -*-
from twilio.rest import Client
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class Driver(models.Model):
    _name = 'saba_pickings.driver'
    name = fields.Char(string="Name",required=True)
class Stock(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def action_done(self):
        res = super(Stock, self).action_done()
        if self.location_dest_id.usage == 'customer' and self.partner_id.mobile:
            self.send_sms()
       # do the things here
        return res

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    @api.multi
    def send_sms(self):
        # Your Account SID from twilio.com/console
        account_sid = "AC920f1728d96a03183d0baecda0b48caa"
        # Your Auth Token from twilio.com/console
        auth_token  = "d2d783452c7104a0df80f1d5892a0c2b"

        client = Client(account_sid, auth_token)
        body=""
        for r in self:
            for stock_move in r.move_lines:
                body += " "+ str(stock_move.product_id.name)+"-"+str(stock_move.product_uom_qty)
        message = client.messages.create(
            to=str(self.partner_id.mobile),
            from_="+12056273782",
            body=body +" has been processed Ref("+self.name+") driver("+str(self.driver_id.name)+") Plate("+str(self.plate_no)+")")
        print(message.sid)



    driver_id = fields.Many2one('saba_pickings.driver',string="Driver",ondelete='restrict',track_visibility='onchange')
    plate_no = fields.Char(string="Plate no")
class Sale(models.Model):
    _inherit = 'sale.order'


    driver_id = fields.Many2one('saba_pickings.driver',string="Driver",ondelete='restrict')
    plate_no = fields.Char(string="Plate no")
    @api.multi
    def action_confirm(self):
        self._action_confirm()
        if self.env['ir.config_parameter'].sudo().get_param('sale.auto_done_setting'):
            self.action_done()
        for order in self:
            if order.picking_ids:
                picking_ids=order.picking_ids
                for picking_id in picking_ids:
                    self.env['stock.picking'].search([('id','=',picking_id.id)],limit=1).write({
                        'driver_id': order.driver_id.id,
                        'plate_no': order.plate_no,
                    })
        return True
class ConfirmWizard(models.TransientModel):
    _name = "saba_pickings.bulk_confirm_sale_wizard"
    _description = "Bulk Sale Confirmation"
    @api.model
    def _get_selected_requests(self):
        sale_values = []
        sales=self.env['sale.order'].search([('id','in',self.env.context.get('active_ids'))])
        for sale in sales:
            sale_values.append(str(sale.partner_id.name) + ' (' +str(sale.amount_total)+ ')')
        return ' - '.join(sale_values)
    name = fields.Text(default=_get_selected_requests)


    def confirm_sales(self):
        sales=self.env['sale.order'].search([('id','in',self.env.context.get('active_ids'))])
        for sale in sales:
            if sale.state in ['draft']:
                sale.action_confirm()
