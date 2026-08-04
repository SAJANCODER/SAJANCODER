# generator/boot.py
from ui import SVG, Text, Group, Rect
from theme import Theme

def generate_boot() -> str:
    svg = SVG(800, 200)
    
    terminal = Group(transform="translate(40, 40)")
    lines = [
        "[ OK ] BOOTING VIRLITH OS KERNEL v2.0.26...",
        "[ OK ] MOUNTING RESEARCH VOLUMES...",
        "[ OK ] INITIALIZING AUTONOMOUS AI EXECUTION ENGINES...",
        "[ OK ] LOADING AZURE CLOUD ARCHITECTURE...",
        "[ OK ] VERIFYING SYSTEM INTEGRITY... 100%",
        "sysadmin@virlith:~$ whoami"
    ]
    
    for i, line in enumerate(lines):
        color = Theme.colors.success if "[ OK ]" in line else Theme.colors.primary_text
        terminal.add(Text(line, 0, i * 24, Theme.fonts.size_sm, color, is_mono=True))
    
    # Blinking cursor
    terminal.add(Rect(200, 5 * 24 - 10, 8, 14, Theme.colors.primary_text, rx=0, class_name="anim-blink"))
    
    svg.add(terminal)
    return svg.render()