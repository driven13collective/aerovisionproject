import reflex as rx

config = rx.Config(
    app_name="aero_audit_pro",
    api_url="http://localhost:8000",
    disable_plugins=['reflex.plugins.sitemap.SitemapPlugin'],
)
