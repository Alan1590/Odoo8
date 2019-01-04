import openerp
from openerp.osv import fields, osv
from openerp import tools, api
from openerp.tools.translate import _
from openerp.tools import html2plaintext
import logging

class res_partner_extension(osv.osv):
    _name='res.partner'
    _description = "Limit notifications to the client"
    _inherit = ['res.partner']
    _columns = {
        'notification_client': fields.boolean('Notify to client', default=False),
	}

        
class sale_notification(osv.osv):
    _name='sale.order'
    _inherit = ['sale.order','mail.thread']
    _track = {
        'state': {
            'sale.mt_order_confirmed': lambda self, cr, uid, obj, ctx=None: obj.state in ['manual', 'progress'] and self.send_notification(cr,uid,obj.partner_id,ctx),
            'sale.mt_order_sent': lambda self, cr, uid, obj, ctx=None: obj.state in ['sent']
        },
    }

    def send_notification(self, cr, uid, ids, context=None):
        sendnotification = self.pool.get('res.partner').browse(cr,uid,int(ids[0]),context).notification_client
        return sendnotification
