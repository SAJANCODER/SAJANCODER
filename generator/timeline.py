# generator/timeline.py
from ui import SVG, Group, Text, Element
from theme import Theme

def generate_timeline() -> str:
    svg = SVG(800, 240)
    svg.add(Text("ENGINEERING TIMELINE", 40, 30, Theme.fonts.size_xs, Theme.colors.secondary_text, is_mono=True, weight="600"))
    
    events = [
        ("2026", "Architecting Scalable Emergency Healthcare Locator on Azure."),
        ("2025", "Founded VIRLITH. Launched QUBREA Git Intelligence Bot."),
        ("2025", "Initiated active research in Local LLMs & Prompt Engineering."),
        ("2024", "Began Independent Research focusing on Autonomous AI systems.")
    ]
    
    tl_group = Group(transform="translate(40, 60)")
    
    for i, (year, desc) in enumerate(events):
        y = i * 40
        # Line connector
        if i < len(events) - 1:
            tl_group.add(Element("line", x1=8, y1=y+10, x2=8, y2=y+40, stroke=Theme.colors.border, stroke_width=2))
        
        # Node
        tl_group.add(
            Element("circle", cx=8, cy=y+6, r=4, fill=Theme.colors.accent),
            Text(year, 24, y+10, Theme.fonts.size_sm, Theme.colors.primary_text, weight="600", is_mono=True),
            Text(desc, 80, y+10, Theme.fonts.size_sm, Theme.colors.secondary_text)
        )
        
    svg.add(tl_group)
    return svg.render()