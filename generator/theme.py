# generator/theme.py
from dataclasses import dataclass

@dataclass
class ColorPalette:
    background: str = "#0D1117"
    primary_surface: str = "#161B22"
    secondary_surface: str = "#21262D"
    border: str = "#30363D"
    primary_text: str = "#F0F6FC"
    secondary_text: str = "#8B949E"
    accent: str = "#2F81F7"
    success: str = "#238636"
    warning: str = "#9E6A03"
    danger: str = "#DA3633"

@dataclass
class Typography:
    primary: str = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    secondary: str = "'IBM Plex Mono', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
    size_xs: str = "10px"
    size_sm: str = "12px"
    size_md: str = "14px"
    size_lg: str = "16px"
    size_xl: str = "20px"
    size_xxl: str = "24px"

@dataclass
class Spacing:
    xs: int = 4
    sm: int = 8
    md: int = 16
    lg: int = 24
    xl: int = 32
    xxl: int = 48
    grid: int = 8

class Theme:
    colors = ColorPalette()
    fonts = Typography()
    space = Spacing()