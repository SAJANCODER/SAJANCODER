# generator/build.py
import os
from boot import generate_boot
from dashboard import generate_dashboard
from products import generate_products
from architecture import generate_architecture
from timeline import generate_timeline
from activity import generate_activity
from footer import generate_footer

def main():
    assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    files = {
        "boot.svg": generate_boot(),
        "dashboard.svg": generate_dashboard(),
        "products.svg": generate_products(),
        "architecture.svg": generate_architecture(),
        "timeline.svg": generate_timeline(),
        "activity.svg": generate_activity(),
        "footer.svg": generate_footer()
    }
    
    for filename, content in files.items():
        filepath = os.path.join(assets_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()