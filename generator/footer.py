# generator/footer.py
from ui import SVG, Text, Element
from theme import Theme

def generate_footer() -> str:
    svg = SVG(800, 80)
    
    svg.add(
        Element("line", x1=40, y1=10, x2=760, y2=10, stroke=Theme.colors.border, stroke_width=1),
        Text("VIRLITH OS // ENGINEERED BY SAJAN D", 400, 45, Theme.fonts.size_xs, Theme.colors.secondary_text, is_mono=True, text_anchor="middle")
    )
    
    return svg.render()