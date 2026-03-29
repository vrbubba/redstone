"""
Giant Mountain with Ice Caps + Skyscraper City Generator
Generates .mcfunction files for Minecraft Bedrock Edition
"""
import os, math, random

OUT = r"c:\Users\abhbu\repos\redstone\BedrockPack\functions"

def write_func(name, lines):
    path = os.path.join(OUT, f"{name}.mcfunction")
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"  Wrote {name}.mcfunction ({len(lines)} commands)")

def fill(x1,y1,z1,x2,y2,z2,block):
    ax1,ax2 = min(x1,x2),max(x1,x2)
    ay1,ay2 = min(y1,y2),max(y1,y2)
    az1,az2 = min(z1,z2),max(z1,z2)
    cmds = []
    S = 31
    for cx in range(ax1, ax2+1, S):
        for cy in range(ay1, ay2+1, S):
            for cz in range(az1, az2+1, S):
                cmds.append(f"fill ~{cx} ~{cy} ~{cz} ~{min(cx+S-1,ax2)} ~{min(cy+S-1,ay2)} ~{min(cz+S-1,az2)} {block}")
    return "\n".join(cmds)

def sb(x,y,z,block):
    return f"setblock ~{x} ~{y} ~{z} {block}"

def comment(t):
    return f"# {t}"

# ── Mountain parameters ──
MTN_CX, MTN_CZ = 0, 0        # mountain center
MTN_RADIUS = 80               # base radius
MTN_HEIGHT = 120               # peak height
SNOW_LINE = 85                 # snow starts here
TREE_LINE = 60                 # trees stop here
ICE_CAP = 100                  # solid ice above this

# ── Skyscraper cluster ──
CITY_X = 120                   # city starts east of mountain
CITY_Z = -40
SKYSCRAPERS = [
    # (x_offset, z_offset, width, depth, height, name)
    (0,   0,  16, 16, 80, "Tower Alpha"),
    (22,  5,  12, 12, 60, "Tower Beta"),
    (38, -5,  14, 14, 100, "Tower Gamma"),
    (56,  8,  10, 10, 45, "Tower Delta"),
    (18, 22,  18, 14, 70, "Tower Epsilon"),
    (42, 20,  12, 12, 55, "Tower Zeta"),
]

def gen_master():
    lines = [
        comment("GIANT MOUNTAIN WITH ICE CAPS + SKYSCRAPER CITY"),
        comment("Run this to build everything. Find a VERY flat area!"),
        "function mountain_clear",
    ]
    write_func("build_mountain_city", lines)

def gen_clear():
    lines = [
        comment("Phase 1: Clear area and set ground"),
        fill(-100, -1, -100, 250, MTN_HEIGHT+10, 200, "air"),
        fill(-100, -1, -100, 250, 0, 200, "grass_block"),
        "function mountain_base",
    ]
    write_func("mountain_clear", lines)

def gen_mountain_base():
    """Phase 2: Lower mountain (Y=1 to Y=40) - wide base with dirt/stone"""
    lines = [comment("Phase 2: Mountain base (Y=1-40)")]
    
    for y in range(1, 41):
        # Radius shrinks as we go up using a smooth curve
        t = y / MTN_HEIGHT
        r = int(MTN_RADIUS * (1.0 - t**0.6))
        if r < 1:
            break
        
        # Determine block type by height
        if y <= 3:
            block = "dirt"
        elif y <= 15:
            block = "stone"
        else:
            block = "stone"
        
        # Build as concentric square rings (fill is rectangular)
        # Use multiple fills to approximate a circle
        for dx in range(-r, r+1, 30):
            ex = min(dx + 29, r)
            # Calculate z extent at this x position for circular shape
            for x in [dx]:
                half_z = int(math.sqrt(max(0, r*r - max(abs(dx),abs(ex))**2)))
                if half_z > 0:
                    lines.append(fill(
                        MTN_CX + dx, y, MTN_CZ - half_z,
                        MTN_CX + ex, y, MTN_CZ + half_z,
                        block
                    ))
        
        # Surface layer
        if y > 5:
            sr = r - 1
            if sr > 0:
                # Grass on top surface ring
                lines.append(fill(
                    MTN_CX - min(sr, 30), y, MTN_CZ - min(sr, 30),
                    MTN_CX + min(sr, 30), y, MTN_CZ + min(sr, 30),
                    "grass_block" if y < 30 else "stone"
                ))

    lines.append("function mountain_mid")
    write_func("mountain_base", lines)

def gen_mountain_mid():
    """Phase 3: Mid mountain (Y=41 to Y=80) - rocky terrain"""
    lines = [comment("Phase 3: Mountain mid section (Y=41-80)")]
    
    for y in range(41, 81):
        t = y / MTN_HEIGHT
        r = int(MTN_RADIUS * (1.0 - t**0.6))
        if r < 1:
            break
        
        block = "stone"
        if y > 60:
            block = "stone"  # above tree line, bare rock
        
        for dx in range(-r, r+1, 30):
            ex = min(dx + 29, r)
            half_z = int(math.sqrt(max(0, r*r - max(abs(dx),abs(ex))**2)))
            if half_z > 0:
                lines.append(fill(
                    MTN_CX + dx, y, MTN_CZ - half_z,
                    MTN_CX + ex, y, MTN_CZ + half_z,
                    block
                ))

    # Add some trees on slopes between Y=20 and TREE_LINE
    random.seed(42)  # deterministic
    for _ in range(60):
        angle = random.uniform(0, 2*math.pi)
        dist = random.uniform(15, 50)
        tx = MTN_CX + int(dist * math.cos(angle))
        tz = MTN_CZ + int(dist * math.sin(angle))
        # Find approximate Y at this distance
        ty_approx = int(MTN_HEIGHT * (1.0 - (dist/MTN_RADIUS)**(1/0.6)))
        if 10 < ty_approx < TREE_LINE:
            # Trunk
            for dy in range(1, 6):
                lines.append(sb(tx, ty_approx + dy, tz, "oak_log"))
            # Canopy
            lines.append(fill(tx-2, ty_approx+5, tz-2, tx+2, ty_approx+7, tz+2, "oak_leaves"))
            lines.append(fill(tx-1, ty_approx+8, tz-1, tx+1, ty_approx+8, tz+1, "oak_leaves"))

    lines.append("function mountain_peak")
    write_func("mountain_mid", lines)

def gen_mountain_peak():
    """Phase 4: Peak (Y=81 to summit) - snow and ice"""
    lines = [comment("Phase 4: Mountain peak with ice cap")]
    
    for y in range(81, MTN_HEIGHT + 1):
        t = y / MTN_HEIGHT
        r = int(MTN_RADIUS * (1.0 - t**0.6))
        if r < 1:
            r = 1
        
        # Block selection by height
        if y >= ICE_CAP:
            block = "blue_ice"
        elif y >= SNOW_LINE:
            block = "snow"  # packed snow layer
        else:
            block = "stone"
        
        for dx in range(-r, r+1, 30):
            ex = min(dx + 29, r)
            half_z = int(math.sqrt(max(0, r*r - max(abs(dx),abs(ex))**2)))
            if half_z > 0:
                lines.append(fill(
                    MTN_CX + dx, y, MTN_CZ - half_z,
                    MTN_CX + ex, y, MTN_CZ + half_z,
                    block
                ))
    
    # Ice spikes at the very top
    for dx, dz in [(-2,0),(2,0),(0,-2),(0,2),(0,0)]:
        for dy in range(MTN_HEIGHT+1, MTN_HEIGHT+8):
            lines.append(sb(MTN_CX+dx, dy, MTN_CZ+dz, "packed_ice"))
    # Beacon at summit
    lines.append(sb(MTN_CX, MTN_HEIGHT+8, MTN_CZ, "sea_lantern"))
    lines.append(sb(MTN_CX, MTN_HEIGHT+9, MTN_CZ, "blue_ice"))

    # Snow patches on upper slopes (scattered snow layers)
    random.seed(99)
    for _ in range(100):
        angle = random.uniform(0, 2*math.pi)
        dist = random.uniform(5, 35)
        sx = MTN_CX + int(dist * math.cos(angle))
        sz = MTN_CZ + int(dist * math.sin(angle))
        sy = int(MTN_HEIGHT * (1.0 - (dist/MTN_RADIUS)**(1/0.6)))
        if SNOW_LINE - 10 < sy < SNOW_LINE:
            lines.append(sb(sx, sy+1, sz, "snow"))

    lines.append("function mountain_skyscrapers")
    write_func("mountain_peak", lines)

def gen_skyscrapers():
    """Phase 5: Build the skyscraper cluster"""
    lines = [comment("Phase 5: Skyscraper city cluster")]
    
    # City ground / plaza
    cx1 = CITY_X - 10
    cz1 = CITY_Z - 20
    cx2 = CITY_X + 80
    cz2 = CITY_Z + 50
    lines.append(fill(cx1, 0, cz1, cx2, 0, cz2, "gray_concrete"))
    # Roads
    lines.append(fill(cx1, 0, CITY_Z - 2, cx2, 0, CITY_Z + 2, "black_concrete"))
    lines.append(fill(CITY_X + 35, 0, cz1, CITY_X + 39, 0, cz2, "black_concrete"))
    # Road markings
    for x in range(cx1, cx2, 6):
        lines.append(fill(x, 0, CITY_Z, x+2, 0, CITY_Z, "yellow_concrete"))
    for z in range(cz1, cz2, 6):
        lines.append(fill(CITY_X+37, 0, z, CITY_X+37, 0, z+2, "yellow_concrete"))

    for i, (xo, zo, w, d, h, name) in enumerate(SKYSCRAPERS):
        bx = CITY_X + xo
        bz = CITY_Z + zo
        lines.append(comment(f"--- {name} ({w}x{d}, {h} tall) ---"))

        # Foundation
        lines.append(fill(bx, -1, bz, bx+w, -1, bz+d, "stone_bricks"))

        # Build floor by floor using solid-shell-then-hollow
        floor_h = 5
        for fy in range(0, h, floor_h):
            yb = fy
            yt = min(fy + floor_h, h)

            # Step 1: Solid floor slab
            lines.append(fill(bx, yb, bz, bx+w, yb, bz+d, "polished_deepslate"))

            # Step 2: Solid outer shell walls (all 4 sides, full thickness)
            lines.append(fill(bx, yb+1, bz, bx+w, yt-1, bz, "iron_block"))      # south wall
            lines.append(fill(bx, yb+1, bz+d, bx+w, yt-1, bz+d, "iron_block"))  # north wall
            lines.append(fill(bx, yb+1, bz, bx, yt-1, bz+d, "iron_block"))      # west wall
            lines.append(fill(bx+w, yb+1, bz, bx+w, yt-1, bz+d, "iron_block"))  # east wall

            # Step 3: Hollow interior
            lines.append(fill(bx+1, yb+1, bz+1, bx+w-1, yt-1, bz+d-1, "air"))

            # Step 4: Cut glass windows into the solid walls (between columns)
            # We leave iron columns every 4 blocks for the structural frame
            col_spacing = 4
            # South face (Z=bz)
            for wx in range(bx+2, bx+w-1, col_spacing):
                we = min(wx + col_spacing - 2, bx+w-2)
                if we > wx:
                    lines.append(fill(wx, yb+2, bz, we, yt-2, bz, "glass"))
            # North face (Z=bz+d)
            for wx in range(bx+2, bx+w-1, col_spacing):
                we = min(wx + col_spacing - 2, bx+w-2)
                if we > wx:
                    lines.append(fill(wx, yb+2, bz+d, we, yt-2, bz+d, "glass"))
            # West face (X=bx)
            for wz in range(bz+2, bz+d-1, col_spacing):
                we = min(wz + col_spacing - 2, bz+d-2)
                if we > wz:
                    lines.append(fill(bx, yb+2, wz, bx, yt-2, we, "glass"))
            # East face (X=bx+w)
            for wz in range(bz+2, bz+d-1, col_spacing):
                we = min(wz + col_spacing - 2, bz+d-2)
                if we > wz:
                    lines.append(fill(bx+w, yb+2, wz, bx+w, yt-2, we, "glass"))

            # Step 5: Horizontal beams on ALL 4 sides at ceiling level
            lines.append(fill(bx, yt, bz, bx+w, yt, bz, "iron_block"))
            lines.append(fill(bx, yt, bz+d, bx+w, yt, bz+d, "iron_block"))
            lines.append(fill(bx, yt, bz+1, bx, yt, bz+d-1, "iron_block"))
            lines.append(fill(bx+w, yt, bz+1, bx+w, yt, bz+d-1, "iron_block"))

            # Floor lighting (recessed in floor)
            lines.append(sb(bx + w//2, yb, bz + d//2, "glowstone"))
            if w > 12:
                lines.append(sb(bx + w//4, yb, bz + d//4, "glowstone"))
                lines.append(sb(bx + 3*w//4, yb, bz + 3*d//4, "glowstone"))

        # Roof
        lines.append(fill(bx, h, bz, bx+w, h, bz+d, "polished_deepslate"))

        # Rooftop features
        if i == 2:  # Tallest tower gets a spire
            for dy in range(1, 20):
                lines.append(sb(bx + w//2, h + dy, bz + d//2, "iron_block"))
            lines.append(sb(bx + w//2, h + 20, bz + d//2, "redstone_lamp"))
        elif i == 0:  # Tower Alpha gets a helipad
            lines.append(fill(bx+3, h+1, bz+3, bx+w-3, h+1, bz+d-3, "gray_concrete"))
            # H marking
            lines.append(fill(bx+5, h+1, bz+5, bx+6, h+1, bz+d-5, "yellow_concrete"))
            lines.append(fill(bx+w-6, h+1, bz+5, bx+w-5, h+1, bz+d-5, "yellow_concrete"))
            lines.append(fill(bx+7, h+1, bz+d//2-1, bx+w-7, h+1, bz+d//2+1, "yellow_concrete"))
        else:
            # AC units / mechanical room
            lines.append(fill(bx+2, h+1, bz+2, bx+4, h+2, bz+4, "iron_block"))
            lines.append(sb(bx+3, h+3, bz+3, "iron_block"))

        # Lobby entrance (front face, ground level - cut through solid wall)
        lines.append(fill(bx + w//2 - 2, 1, bz, bx + w//2 + 2, 4, bz, "air"))
        lines.append(fill(bx + w//2 - 2, 5, bz, bx + w//2 + 2, 5, bz, "iron_block"))

    # Street lights
    for x in range(cx1 + 5, cx2, 15):
        lines.append(fill(x, 1, CITY_Z - 4, x, 4, CITY_Z - 4, "iron_block"))
        lines.append(sb(x, 5, CITY_Z - 4, "glowstone"))
        lines.append(fill(x, 1, CITY_Z + 4, x, 4, CITY_Z + 4, "iron_block"))
        lines.append(sb(x, 5, CITY_Z + 4, "glowstone"))

    # Park between mountain and city
    lines.append(fill(CITY_X - 15, 0, CITY_Z - 15, CITY_X - 5, 0, CITY_Z + 30, "grass_block"))
    random.seed(77)
    for _ in range(12):
        px = CITY_X - 14 + random.randint(0, 8)
        pz = CITY_Z - 12 + random.randint(0, 38)
        for dy in range(1, 5):
            lines.append(sb(px, dy, pz, "oak_log"))
        lines.append(fill(px-1, 5, pz-1, px+1, 6, pz+1, "oak_leaves"))

    write_func("mountain_skyscrapers", lines)

# ── Generate all ──
if __name__ == "__main__":
    print("Generating Mountain + Skyscraper City...")
    gen_master()
    gen_clear()
    gen_mountain_base()
    gen_mountain_mid()
    gen_mountain_peak()
    gen_skyscrapers()
    print("\nDone! Run /function build_mountain_city in-game.")
