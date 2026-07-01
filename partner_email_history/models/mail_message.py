# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models
from odoo.tools import html2plaintext

_logger = logging.getLogger(__name__)


class MailMessage(models.Model):
    _inherit = "mail.message"

    body_short = fields.Char(string="Body Preview", compute="_compute_body_short")

    @api.depends("body")
    def _compute_body_short(self):
        for msg in self:
            if msg.body:
                txt = html2plaintext(msg.body)
                txt = " ".join(txt.split())  # collapse all whitespace
                msg.body_short = txt[:160] + "…" if len(txt) > 160 else txt
            else:
                msg.body_short = ""
