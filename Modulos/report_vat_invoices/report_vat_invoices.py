import openerp
from openerp.addons.crm import crm
from openerp.osv import fields, osv
from openerp import models, tools, api
from openerp.tools.translate import _
from openerp.tools import html2plaintext
import logging

class account_invoice_tax_wizard(models.Model):
    """ Print tax from invoice
    """
    _name = "account.invoice.tax.report"
    _description = "Print tax report"
    _inherit = ['account']

    def _get_vat_partner(self, cr, uid, ids, context=None):
        return 0


    def _get_vat_supplier(self, cr, uid, ids, context=None):
        return 0


    def _get_vat_total(self, cr, uid, ids, context=None):
        return 0
