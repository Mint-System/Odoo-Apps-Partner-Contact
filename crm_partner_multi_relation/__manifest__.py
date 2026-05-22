# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Crm Partner Multi Relation",
    "summary": """
        Add relations to CRM leads and opportunities.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["crm", "partner_multi_relation"],
    "data": [
        "views/crm_lead_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
