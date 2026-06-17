# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Calendar CRM Link",
    "summary": """
        Add opportunity links to events.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Repository",
    "development_status": "Production/Stable",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["calendar", "crm_link"],
    "data": [
        "views/crm_lead_views.xml",
        "views/calendar_event_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
