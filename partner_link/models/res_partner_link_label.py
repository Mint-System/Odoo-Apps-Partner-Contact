# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartnerLinkLabel(models.Model):
    _name = "res.partner.link.label"
    _description = "Partner Link Label"

    name = fields.Char(string="Label")
