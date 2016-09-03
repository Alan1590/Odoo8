import openerp
from openerp.addons.crm import crm
from openerp.osv import fields, osv
from openerp import tools, api
from openerp.tools.translate import _
from openerp.tools import html2plaintext
import logging

class account_invoice_tax(osv.osv):
    """ Print tax from invoice
    """
    _name = "account.invoice.tax"
    _description = "Print tax report"
    _inherit = ['account.invoice']
    _columns = {
        'start_date_invoice_partner': fields.date('Date Partner Start',size=256),
        'journal_partner': fields.many2many('account.journal',size=256),
        'end_date_invoice_partner': fields.date('Date Partner End',size=256),
        'tax_partner': fields.many2many('account.tax',size=256),
        'start_date_invoice_supplier': fields.char('Date Supplier Start',size=256),
        'journal_supplier': fields.char('account.journal',size=256),
        'end_date_invoice_supplier': fields.char('Date Supplier End',size=256),
        'tax_supplier': fields.char('account.tax',size=256),
        }

