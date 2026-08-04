# generator/architecture.py
from ui import SVG, Group, Rect, Text, Element
from theme import Theme

def node(x: int, y: int, label: str, icon: str) -> Group:
    g = Group(transform=f"translate({x}, {y})")
    g.add(
        Rect(0, 0, 140, 50, Theme.colors.secondary_surface, rx=6, stroke=Theme.colors.border, stroke_width=1),
        Text(icon, 16, 30, Theme.fonts.size_lg, Theme.colors.primary_text),
        Text(label, 40, 29, Theme.fonts.size_sm, Theme.colors.primary_text, weight="500", is_mono=True)
    )
    return g

def edge(x1: int, y1: int, x2: int, y2: int) -> Element:
    return Element("path", 
                   d=f"M {x1} {y1} C {x1 + 40} {y1}, {x2 - 40} {y2}, {x2} {y2}", 
                   stroke=Theme.colors.border, 
                   stroke_width=2, 
                   fill="none")

def generate_architecture() -> str:
    svg = SVG(800, 280)
    svg.add(Text("SYSTEM ARCHITECTURE", 40, 30, Theme.fonts.size_xs, Theme.colors.secondary_text, is_mono=True, weight="600"))
    
    arch = Card(40, 50, 720, 210)
    
    # Draw edges
    arch.add(
        edge(160, 65, 290, 65),
        edge(160, 65, 290, 145),
        edge(430, 65, 540, 105),
        edge(430, 145, 540, 105)
    )
    
    # Draw nodes
    arch.add(
        node(20, 40, "CLIENT", "🖥️"),
        node(290, 40, "AZURE CLOUD", "☁️"),
        node(290, 120, "AI ENGINE", "🧠"),
        node(540, 80, "DATA LAKE", "🗄️")
    )
    
    svg.add(arch)
    return svg.render()