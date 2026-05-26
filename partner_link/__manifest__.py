# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Link",
    "summary": """
        Link contacts with other contacts.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["contacts"],
    "data": ["views/res_partner_link_label_views.xml", "security/ir.model.access.csv", "views/res_partner_views.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
