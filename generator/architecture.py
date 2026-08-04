# generator/architecture.py
from ui import SVG, Group, Rect, Text, Element
from theme import Theme

def v_edge(x1: int, y1: int, x2: int, y2: int) -> Element:
    """Creates a smooth vertical bezier curve between two points."""
    cy = y1 + (y2 - y1) // 2
    return Element("path", 
                   d=f"M {x1} {y1} C {x1} {cy}, {x2} {cy}, {x2} {y2}", 
                   stroke=Theme.colors.border, 
                   stroke_width=1.5, 
                   fill="none")

def mind_node(x: int, y: int, width: int, height: int, title: str, subtitle: str) -> Group:
    """Creates a reusable decision node representing the engineering mindset."""
    g = Group(transform=f"translate({x}, {y})")
    
    # Base container
    g.add(Rect(0, 0, width, height, Theme.colors.secondary_surface, rx=6, stroke=Theme.colors.border, stroke_width=1))
    
    # Mathematical center for text alignment
    cx = width // 2
    
    # Node content (Title and decision question)
    g.add(
        Text(title, cx, 26, Theme.fonts.size_sm, Theme.colors.primary_text, weight="600", is_mono=True, text_anchor="middle"),
        Text(subtitle, cx, 46, Theme.fonts.size_xs, Theme.colors.secondary_text, text_anchor="middle")
    )
    return g

def generate_architecture() -> str:
    """Generates the Thinking Architecture diagram algorithmically."""
    canvas_w = 1000
    canvas_h = 1000
    node_h = 60
    y_step = 100
    start_y = 80
    
    svg = SVG(canvas_w, canvas_h)
    
    # Document Header
    svg.add(Text("ENGINEERING MINDSET // SAJAN D", 40, 40, Theme.fonts.size_xs, Theme.colors.secondary_text, is_mono=True, weight="600"))
    
    # Definition of the thinking pipeline
    layers_data = [
        [{"title": "PROBLEM DISCOVERY", "sub": "What is the core human necessity?", "width": 360}],
        [{"title": "DOMAIN RESEARCH", "sub": "What are the structural constraints?", "width": 360}],
        [{"title": "DATA ENGINEERING", "sub": "How is reality modeled as state?", "width": 360}],
        [
            {"title": "COMPUTER VISION", "sub": "Extract visual reality.", "width": 210},
            {"title": "GRAPH LEARNING", "sub": "Map dependencies.", "width": 210},
            {"title": "LLM PROCESSING", "sub": "Synthesize intent.", "width": 210},
            {"title": "REASONING", "sub": "Evaluate context.", "width": 210}
        ],
        [
            {"title": "PROMPT ARCHITECTURE", "sub": "Constrain AI output.", "width": 280},
            {"title": "BUSINESS LOGIC", "sub": "Enforce deterministic rules.", "width": 280},
            {"title": "AUTONOMOUS AGENTS", "sub": "Orchestrate workflows.", "width": 280}
        ],
        [{"title": "EXECUTION LAYER", "sub": "How do we expose scalable capabilities?", "width": 360}],
        [{"title": "INFRASTRUCTURE", "sub": "How do we ensure deployment reliability?", "width": 360}],
        [{"title": "OBSERVABILITY", "sub": "Is reality matching system expectations?", "width": 360}],
        [{"title": "CONTINUOUS EVOLUTION", "sub": "How does the system iteratively improve?", "width": 360}]
    ]
    
    edges_group = Group()
    nodes_group = Group()
    
    previous_centers = []
    previous_bottom = 0
    current_y = start_y
    
    # Algorithmically map layers and construct nodes & edges
    for i, layer in enumerate(layers_data):
        count = len(layer)
        spacing = 24
        total_width = sum(d['width'] for d in layer) + spacing * (count - 1)
        start_x = (canvas_w - total_width) // 2
        
        current_x = start_x
        current_centers = []
        
        for d in layer:
            # Construct the Node
            nodes_group.add(mind_node(current_x, current_y, d['width'], node_h, d['title'], d['sub']))
            
            # Record center coordinate for edge routing
            cx = current_x + (d['width'] // 2)
            current_centers.append(cx)
            current_x += d['width'] + spacing
        
        # Route Edges from the previous layer
        if i > 0:
            y1 = previous_bottom
            y2 = current_y
            
            if len(previous_centers) == 1 and len(current_centers) == 1:
                # Direct 1-to-1 Connection
                edges_group.add(v_edge(previous_centers[0], y1, current_centers[0], y2))
            else:
                # N-to-M Routing via Central Hub
                hub_x = canvas_w // 2
                hub_y = y1 + (y2 - y1) // 2
                
                for pcx in previous_centers:
                    edges_group.add(v_edge(pcx, y1, hub_x, hub_y))
                    
                for ccx in current_centers:
                    edges_group.add(v_edge(hub_x, hub_y, ccx, y2))
        
        # Advance layout state
        previous_centers = current_centers
        previous_bottom = current_y + node_h
        current_y += y_step
        
    svg.add(edges_group)
    svg.add(nodes_group)
    
    return svg.render()