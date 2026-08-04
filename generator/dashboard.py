# generator/dashboard.py
from ui import SVG, Card, Text, Group, Chip, Rect
from theme import Theme

def generate_dashboard() -> str:
    svg = SVG(800, 300)
    
    # Profile Card
    profile = Card(40, 20, 720, 260)
    
    profile.add(
        Text("SAJAN D", 32, 48, Theme.fonts.size_xxl, Theme.colors.primary_text, weight="700"),
        Text("Founder, VIRLITH &amp; Independent Researcher", 32, 72, Theme.fonts.size_md, Theme.colors.secondary_text),
        Text("SYSTEM DESIGN | AI ARCHITECTURE | CLOUD PLATFORMS", 32, 96, Theme.fonts.size_xs, Theme.colors.accent, is_mono=True)
    )
    
    # System Status Panel
    status_group = Group(transform="translate(32, 130)")
    metrics = [
        ("UPTIME", "99.99%", Theme.colors.success),
        ("CURRENT FOCUS", "Generative AI Systems", Theme.colors.primary_text),
        ("PRIMARY ENV", "Azure Cloud, Local LLMs", Theme.colors.primary_text),
        ("RESEARCH STATUS", "Active", Theme.colors.success)
    ]
    
    for i, (label, val, color) in enumerate(metrics):
        y_offset = i * 28
        status_group.add(
            Text(label, 0, y_offset, Theme.fonts.size_xs, Theme.colors.secondary_text, is_mono=True),
            Text(val, 120, y_offset, Theme.fonts.size_sm, color, weight="500")
        )
        
    profile.add(status_group)
    
    # Tech Stack Chips
    chips = Group(transform="translate(350, 130)")
    techs = ["Python", "Azure", "Machine Learning", "System Architecture", "Prompt Engineering", "React"]
    
    x_off, y_off = 0, 0
    for tech in techs:
        width = len(tech) * 7 + 24
        if x_off + width > 350:
            x_off = 0
            y_off += 32
        chips.add(Chip(x_off, y_off, tech))
        x_off += width + 8
        
    profile.add(chips)
    
    svg.add(profile)
    return svg.render()