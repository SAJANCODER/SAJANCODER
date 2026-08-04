# generator/products.py
from ui import SVG, Card, Text, Group, ProgressBar, Chip
from theme import Theme

def generate_products() -> str:
    svg = SVG(800, 320)
    
    products_data = [
        {
            "name": "QUBREA",
            "desc": "Git intelligence bot delivering code repository summaries autonomously to Telegram.",
            "tech": ["Python", "Telegram API", "Git", "LLMs"],
            "progress": 1.0,
            "status": "LIVE"
        },
        {
            "name": "CARBON-TWIN",
            "desc": "AI-driven manufacturing optimization platform modeling industrial processes.",
            "tech": ["System Design", "GenAI", "Azure"],
            "progress": 0.85,
            "status": "IN DEVELOPMENT"
        },
        {
            "name": "HEALTH-LOCATOR",
            "desc": "Scalable emergency healthcare resource locator utilizing Azure Cloud Services.",
            "tech": ["Azure", "Microservices", "API"],
            "progress": 0.95,
            "status": "DEPLOYED"
        }
    ]
    
    svg.add(Text("PRODUCTS &amp; RESEARCH", 40, 30, Theme.fonts.size_xs, Theme.colors.secondary_text, is_mono=True, weight="600"))
    
    for i, prod in enumerate(products_data):
        card = Card(40, 50 + (i * 85), 720, 75)
        
        card.add(
            Text(prod["name"], 24, 30, Theme.fonts.size_lg, Theme.colors.primary_text, weight="700"),
            Text(prod["desc"], 200, 30, Theme.fonts.size_sm, Theme.colors.secondary_text),
            ProgressBar(24, 50, 150, prod["progress"], Theme.colors.success if prod["progress"] == 1.0 else Theme.colors.accent),
            Text(prod["status"], 185, 54, "9px", Theme.colors.success if prod["progress"] == 1.0 else Theme.colors.accent, is_mono=True)
        )
        svg.add(card)

    return svg.render()