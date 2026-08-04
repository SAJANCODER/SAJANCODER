# generator/activity.py
from ui import SVG, Group, Rect, Text
from theme import Theme
import datetime

def generate_activity() -> str:
    svg = SVG(800, 200)
    svg.add(Text("SYSTEM ACTIVITY", 40, 30, Theme.fonts.size_xs, Theme.colors.secondary_text, is_mono=True, weight="600"))
    
    terminal = Group(transform="translate(40, 50)")
    terminal.add(Rect(0, 0, 720, 130, Theme.colors.primary_surface, rx=8, stroke=Theme.colors.border, stroke_width=1))
    
    logs = [
        "sysadmin@virlith:~$ tail -f /var/log/research.log",
        f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] INFO: QUBREA deployment synchronized successfully.",
        f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] INFO: CARBON-TWIN simulation engine updated.",
        f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] WARN: Azure ML pipeline optimizing...",
        f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] INFO: Independent research manuscript drafted."
    ]
    
    for i, log in enumerate(logs):
        color = Theme.colors.secondary_text
        if "INFO" in log: color = Theme.colors.success
        elif "WARN" in log: color = Theme.colors.warning
        elif "sysadmin" in log: color = Theme.colors.primary_text
            
        terminal.add(Text(log, 16, 24 + (i * 22), Theme.fonts.size_xs, color, is_mono=True))
        
    svg.add(terminal)
    return svg.render()