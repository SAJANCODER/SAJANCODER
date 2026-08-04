# generator/ui.py
from typing import List, Dict, Any, Optional
from theme import Theme

class Element:
    def __init__(self, tag_name: str, **attributes):
        self.tag_name = tag_name
        self.attributes = attributes
        self.children: List['Element'] = []
        self.text_content: str = ""

    def add(self, *elements: 'Element') -> 'Element':
        for el in elements:
            if el:
                self.children.append(el)
        return self

    def text(self, content: str) -> 'Element':
        self.text_content = content
        return self

    def _serialize_attrs(self) -> str:
        attrs = []
        for k, v in self.attributes.items():
            if v is not None:
                key = k.replace('_', '-')
                if key == "class-name":
                    key = "class"
                attrs.append(f'{key}="{v}"')
        return " ".join(attrs)

    def render(self, indent: int = 0) -> str:
        pad = " " * indent
        attrs = self._serialize_attrs()
        attr_str = f" {attrs}" if attrs else ""
        
        if not self.children and not self.text_content:
            return f"{pad}<{self.tag_name}{attr_str} />"
        
        result = [f"{pad}<{self.tag_name}{attr_str}>"]
        if self.text_content:
            result.append(f"{pad}  {self.text_content}")
        for child in self.children:
            result.append(child.render(indent + 2))
        result.append(f"{pad}</{self.tag_name}>")
        
        return "\n".join(result)

class SVG(Element):
    def __init__(self, width: int, height: int):
        super().__init__("svg", 
            xmlns="http://www.w3.org/2000/svg",
            viewBox=f"0 0 {width} {height}",
            width=width,
            height=height,
            fill="none"
        )
        self.add(Element("style").text(f"""
                @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&amp;family=Inter:wght@400;500;600;700&amp;display=swap');
                text {{ font-family: {Theme.fonts.primary}; }}
                .mono {{ font-family: {Theme.fonts.secondary}; }}
                .anim-blink {{ animation: blink 1s step-end infinite; }}
                @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
            """))
        self.add(Element("rect", width="100%", height="100%", fill=Theme.colors.background))

class Group(Element):
    def __init__(self, **attributes):
        super().__init__("g", **attributes)

class Text(Element):
    def __init__(self, content: str, x: int, y: int, font_size: str, color: str, weight: str = "400", is_mono: bool = False, **kwargs):
        super().__init__("text", x=x, y=y, font_size=font_size, fill=color, font_weight=weight, **kwargs)
        if is_mono:
            self.attributes["class-name"] = "mono"
        self.text(content)

class Rect(Element):
    def __init__(self, x: int, y: int, width: int, height: int, fill: str, rx: int = 4, **kwargs):
        super().__init__("rect", x=x, y=y, width=width, height=height, fill=fill, rx=rx, **kwargs)

class Card(Group):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(transform=f"translate({x}, {y})")
        self.add(
            Rect(0, 0, width, height, Theme.colors.primary_surface, rx=8, stroke=Theme.colors.border, stroke_width=1)
        )

class ProgressBar(Group):
    def __init__(self, x: int, y: int, width: int, progress: float, color: str):
        super().__init__(transform=f"translate({x}, {y})")
        self.add(
            Rect(0, 0, width, 4, Theme.colors.border, rx=2),
            Rect(0, 0, int(width * progress), 4, color, rx=2)
        )

class Chip(Group):
    def __init__(self, x: int, y: int, label: str, color: str = Theme.colors.accent, bg: str = Theme.colors.secondary_surface):
        super().__init__(transform=f"translate({x}, {y})")
        self.add(
            Rect(0, 0, len(label) * 7 + 16, 20, bg, rx=10, stroke=color, stroke_width=1),
            Text(label, 8, 14, Theme.fonts.size_xs, color, is_mono=True)
        )