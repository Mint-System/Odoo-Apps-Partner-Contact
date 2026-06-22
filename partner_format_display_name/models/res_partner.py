# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"


    def _get_complete_name(self):

        if self.name and self.parent_id and self.parent_id.name:
            new_name = f"{self.name} ({self.sudo().parent_id.name})" 
            return new_name.strip()

        name = super()._get_complete_name()
        return name

