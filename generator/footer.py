# generator/footer.py
from ui import SVG, Group, Rect, Text, Element
from theme import Theme

def endpoint_card(x: int, y: int, title: str, subtitle: str, status: str) -> Group:
    g = Group(transform=f"translate({x}, {y})")
    g.add(
        Rect(0, 0, 340, 75, Theme.colors.secondary_surface, rx=6, stroke=Theme.colors.border, stroke_width=1),
        # Blinking status indicator
        Element("circle", cx=20, cy=24, r=4, fill=Theme.colors.success, class_name="anim-blink"),
        Text(status, 32, 28, "10px", Theme.colors.success, is_mono=True, weight="600"),
        Text(title, 20, 50, Theme.fonts.size_md, Theme.colors.primary_text, weight="700", is_mono=True),
        Text(subtitle, 20, 65, "11px", Theme.colors.secondary_text)
    )
    return g

def generate_footer() -> str:
    svg = SVG(800, 320)
    
    # Section Header
    svg.add(Text("SYSTEM ENDPOINTS // COLLABORATION PROTOCOLS", 40, 30, Theme.fonts.size_xs, Theme.colors.secondary_text, is_mono=True, weight="600"))
    
    # 2x2 Grid of Communication Endpoints
    svg.add(
        endpoint_card(40, 60, "TCP/LINKEDIN_GATEWAY", "Establish connection &amp; follow network updates.", "PORT: OPEN"),
        endpoint_card(420, 60, "SMTP/COLLABORATION", "Ping for architectural discussions &amp; partnerships.", "AWAITING PAYLOAD"),
        endpoint_card(40, 155, "GIT/HUB_REPOSITORY", "Review source code &amp; execution engines.", "ACTIVE THREAD"),
        endpoint_card(420, 155, "HTTP/DOC_DECRYPTION", "Download encrypted resume &amp; career specs.", "READY")
    )
    
    # Bottom Footer Divider
    svg.add(Element("line", x1=40, y1=260, x2=760, y2=260, stroke=Theme.colors.border, stroke_width=1))
    
    # Copyright Statement
    svg.add(Text("© 2026 SAJAN D // VIRLITH SYSTEMS", 400, 290, "11px", Theme.colors.secondary_text, is_mono=True, text_anchor="middle"))
    
    return svg.render()