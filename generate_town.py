"""
Modern Town Generator
Generates a small town with modern houses for Minecraft Bedrock Edition
"""
import os, random

OUT = r"c:\Users\abhbu\repos\redstone\BedrockPack\functions"

def write_func(name, lines):
    path = os.path.join(OUT, f"{name}.mcfunction")
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")
    actual = sum(line.count('\n') + 1 for line in lines if not line.startswith('#'))
    print(f"  Wrote {name}.mcfunction ({actual} cmds)")

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

# ── Town layout ──
# 10 house plots arranged along streets
# Main road runs East-West, side streets run North-South
ROAD_Y = 0
PLOT_W = 20   # each plot is 20x22
PLOT_D = 22

# House styles
STYLES = [
    {"name": "Contemporary",  "wall": "white_concrete",  "accent": "dark_oak_planks", "roof": "gray_concrete",   "floor": "birch_planks"},
    {"name": "Industrial",    "wall": "light_gray_concrete", "accent": "iron_block",   "roof": "black_concrete",  "floor": "polished_deepslate"},
    {"name": "Minimalist",    "wall": "white_concrete",  "accent": "quartz_block",    "roof": "white_concrete",  "floor": "quartz_block"},
    {"name": "Rustic Modern", "wall": "stone_bricks",    "accent": "spruce_planks",   "roof": "dark_oak_planks", "floor": "spruce_planks"},
    {"name": "Luxury",        "wall": "quartz_block",    "accent": "gold_block",      "roof": "gray_concrete",   "floor": "dark_oak_planks"},
]

def build_modern_house(lines, px, pz, style_idx, facing="south"):
    """Build one modern house on a plot at (px, pz)"""
    s = STYLES[style_idx % len(STYLES)]
    wall, accent, roof_b, floor_b = s["wall"], s["accent"], s["roof"], s["floor"]
    lines.append(comment(f"--- {s['name']} House at ({px},{pz}) ---"))

    # Plot dimensions
    hw, hd = 14, 16  # house footprint
    hh = 5           # wall height
    hx, hz = px + 3, pz + 4  # house position on plot (with front yard)

    # ── Yard ──
    lines.append(fill(px, 0, pz, px+PLOT_W-1, 0, pz+PLOT_D-1, "grass_block"))
    # Driveway
    lines.append(fill(px+8, 0, pz, px+11, 0, pz+3, "gray_concrete"))
    # Front path
    lines.append(fill(px+9, 0, pz+1, px+10, 0, pz+3, "stone"))
    # Fence around yard (except front)
    lines.append(fill(px, 1, pz+PLOT_D-1, px+PLOT_W-1, 1, pz+PLOT_D-1, "dark_oak_fence"))
    lines.append(fill(px, 1, pz+1, px, 1, pz+PLOT_D-1, "dark_oak_fence"))
    lines.append(fill(px+PLOT_W-1, 1, pz+1, px+PLOT_W-1, 1, pz+PLOT_D-1, "dark_oak_fence"))

    # ── Foundation ──
    lines.append(fill(hx, 0, hz, hx+hw-1, 0, hz+hd-1, floor_b))

    # ── Walls (solid shell then hollow) ──
    # All 4 walls
    lines.append(fill(hx, 1, hz, hx+hw-1, hh, hz, wall))           # front
    lines.append(fill(hx, 1, hz+hd-1, hx+hw-1, hh, hz+hd-1, wall)) # back
    lines.append(fill(hx, 1, hz, hx, hh, hz+hd-1, wall))           # left
    lines.append(fill(hx+hw-1, 1, hz, hx+hw-1, hh, hz+hd-1, wall)) # right
    # Hollow interior
    lines.append(fill(hx+1, 1, hz+1, hx+hw-2, hh-1, hz+hd-2, "air"))

    # ── Roof (flat with slight overhang) ──
    lines.append(fill(hx-1, hh, hz-1, hx+hw, hh, hz+hd, roof_b))
    # Roof edge accent
    lines.append(fill(hx-1, hh, hz-1, hx+hw, hh, hz-1, accent))
    lines.append(fill(hx-1, hh, hz+hd, hx+hw, hh, hz+hd, accent))

    # ── Large front windows (modern style) ──
    lines.append(fill(hx+2, 2, hz, hx+5, hh-1, hz, "glass"))
    lines.append(fill(hx+8, 2, hz, hx+hw-3, hh-1, hz, "glass"))
    # Side windows
    lines.append(fill(hx, 2, hz+4, hx, hh-1, hz+7, "glass"))
    lines.append(fill(hx, 2, hz+10, hx, hh-1, hz+13, "glass"))
    lines.append(fill(hx+hw-1, 2, hz+4, hx+hw-1, hh-1, hz+7, "glass"))
    lines.append(fill(hx+hw-1, 2, hz+10, hx+hw-1, hh-1, hz+13, "glass"))
    # Back windows
    lines.append(fill(hx+3, 2, hz+hd-1, hx+hw-4, hh-1, hz+hd-1, "glass"))

    # ── Front door ──
    lines.append(fill(hx+6, 1, hz, hx+7, 3, hz, "air"))
    lines.append(fill(hx+6, 4, hz, hx+7, 4, hz, accent))  # door lintel

    # ── Interior ──
    # Living room (front left)
    lines.append(fill(hx+1, 1, hz+1, hx+5, 1, hz+5, floor_b))
    # Sofa
    lines.append(fill(hx+1, 1, hz+4, hx+4, 1, hz+4, accent))
    lines.append(fill(hx+1, 2, hz+5, hx+4, 2, hz+5, accent))  # back
    # Coffee table
    lines.append(fill(hx+2, 1, hz+2, hx+3, 1, hz+3, "dark_oak_planks"))
    # TV wall
    lines.append(sb(hx+1, 2, hz+1, "black_concrete"))
    lines.append(sb(hx+2, 2, hz+1, "black_concrete"))
    lines.append(sb(hx+3, 2, hz+1, "black_concrete"))

    # Kitchen (front right)
    lines.append(fill(hx+8, 1, hz+1, hx+hw-2, 1, hz+1, "polished_deepslate"))  # counter
    lines.append(fill(hx+8, 1, hz+2, hx+hw-2, 1, hz+2, "polished_deepslate"))
    lines.append(sb(hx+hw-2, 1, hz+1, "crafting_table"))  # stove stand-in
    lines.append(sb(hx+10, 2, hz+1, "glowstone"))  # under-cabinet light

    # Interior dividing wall (partial, open plan)
    lines.append(fill(hx+7, 1, hz+5, hx+7, 3, hz+hd-5, wall))
    # Doorway in divider
    lines.append(fill(hx+7, 1, hz+7, hx+7, 3, hz+9, "air"))

    # Bedroom (back left)
    lines.append(fill(hx+1, 1, hz+hd-5, hx+1, 1, hz+hd-2, floor_b))
    # Bed
    lines.append(fill(hx+2, 1, hz+hd-4, hx+4, 1, hz+hd-3, "white_wool"))
    lines.append(fill(hx+2, 1, hz+hd-2, hx+4, 2, hz+hd-2, accent))  # headboard
    # Nightstands
    lines.append(sb(hx+1, 1, hz+hd-3, "dark_oak_planks"))
    lines.append(sb(hx+5, 1, hz+hd-3, "dark_oak_planks"))
    # Lamps on nightstands
    lines.append(sb(hx+1, 2, hz+hd-3, "sea_lantern"))
    lines.append(sb(hx+5, 2, hz+hd-3, "sea_lantern"))

    # Bathroom (back right)
    lines.append(fill(hx+9, 0, hz+hd-5, hx+hw-2, 0, hz+hd-2, "quartz_block"))
    lines.append(fill(hx+10, 1, hz+hd-2, hx+12, 1, hz+hd-2, "quartz_block"))  # vanity
    lines.append(sb(hx+11, 2, hz+hd-2, "glass"))  # mirror
    lines.append(sb(hx+9, 1, hz+hd-4, "cauldron"))  # tub stand-in

    # Ceiling lights
    lines.append(sb(hx+4, hh-1, hz+3, "glowstone"))
    lines.append(sb(hx+10, hh-1, hz+3, "glowstone"))
    lines.append(sb(hx+4, hh-1, hz+hd-4, "glowstone"))
    lines.append(sb(hx+10, hh-1, hz+hd-4, "glowstone"))

    # ── Garage (attached, right side) ──
    gx = hx + hw
    lines.append(fill(gx, 0, hz, gx+5, 0, hz+7, "polished_deepslate"))
    lines.append(fill(gx, 1, hz+7, gx+5, 4, hz+7, wall))     # back
    lines.append(fill(gx+5, 1, hz, gx+5, 4, hz+7, wall))     # side
    lines.append(fill(gx, 1, hz, gx, 4, hz+7, wall))          # shared wall
    lines.append(fill(gx, 4, hz, gx+5, 4, hz+7, roof_b))     # roof
    lines.append(fill(gx+1, 1, hz+1, gx+4, 3, hz+6, "air"))  # interior
    # Garage door (front, open)
    lines.append(fill(gx+1, 1, hz, gx+4, 3, hz, "air"))

    # ── Landscaping ──
    # Bushes along front
    for bx_off in [1, 2, 13, 14]:
        lines.append(sb(px+bx_off, 1, pz+3, "oak_leaves"))
    # Tree in front yard (away from house)
    tx, tz = px + 2, pz + 1
    for dy in range(1, 5):
        lines.append(sb(tx, dy, tz, "birch_log"))
    lines.append(fill(tx-1, 5, tz-1, tx+1, 6, tz+1, "birch_leaves"))
    lines.append(sb(tx, 7, tz, "birch_leaves"))
    # Mailbox
    lines.append(sb(px+8, 1, pz, "cobblestone_wall"))
    lines.append(sb(px+8, 2, pz, "iron_block"))
    # Outdoor light
    lines.append(sb(hx+6, 3, hz-1, "sea_lantern"))

def gen_master():
    lines = [
        comment("MODERN TOWN - 10 houses with roads and park"),
        comment("Run: /function build_town"),
        "function town_clear",
    ]
    write_func("build_town", lines)

def gen_clear():
    lines = [comment("Phase 1: Clear and flatten")]
    lines.append(fill(-5, -1, -5, 95, 15, 105, "air"))
    lines.append(fill(-5, -1, -5, 95, 0, 105, "grass_block"))
    lines.append("function town_roads")
    write_func("town_clear", lines)

def gen_roads():
    lines = [comment("Phase 2: Roads, sidewalks, street lights")]
    # Main East-West road (z = 45 to 50)
    lines.append(fill(-5, 0, 45, 95, 0, 50, "black_concrete"))
    # Yellow center line
    for x in range(-5, 95, 4):
        lines.append(fill(x, 0, 47, x+1, 0, 48, "yellow_concrete"))
    # White edge lines
    lines.append(fill(-5, 0, 45, 95, 0, 45, "white_concrete"))
    lines.append(fill(-5, 0, 50, 95, 0, 50, "white_concrete"))

    # Side street (x = 42 to 47)
    lines.append(fill(42, 0, -5, 47, 0, 105, "black_concrete"))
    lines.append(fill(42, 0, -5, 42, 0, 105, "white_concrete"))
    lines.append(fill(47, 0, -5, 47, 0, 105, "white_concrete"))

    # Sidewalks (stone slabs along roads)
    lines.append(fill(-5, 0, 43, 95, 0, 44, "stone"))
    lines.append(fill(-5, 0, 51, 95, 0, 52, "stone"))
    lines.append(fill(40, 0, -5, 41, 0, 105, "stone"))
    lines.append(fill(48, 0, -5, 49, 0, 105, "stone"))

    # Street lights along main road
    for x in range(0, 90, 15):
        lines.append(fill(x, 1, 44, x, 5, 44, "iron_block"))
        lines.append(sb(x, 6, 44, "glowstone"))
        lines.append(sb(x+1, 6, 44, "iron_block"))
        lines.append(sb(x+1, 6, 43, "glowstone"))  # light arm
        lines.append(fill(x, 1, 51, x, 5, 51, "iron_block"))
        lines.append(sb(x, 6, 51, "glowstone"))

    # Street signs
    lines.append(sb(42, 4, 45, "white_concrete"))
    lines.append(sb(42, 5, 45, "white_concrete"))

    lines.append("function town_houses1")
    write_func("town_roads", lines)

def gen_houses1():
    """North side houses (5 houses, z=0 to 42)"""
    lines = [comment("Phase 3: North side houses")]
    random.seed(123)
    # 5 houses along north side of main road
    plots = [
        (0,  20, 0),   # house 1
        (22, 20, 1),   # house 2
        (50, 20, 2),   # house 3
        (72, 20, 3),   # house 4
        (0,  0,  4),   # house 5 (further north)
    ]
    for px, pz, si in plots:
        build_modern_house(lines, px, pz, si)

    lines.append("function town_houses2")
    write_func("town_houses1", lines)

def gen_houses2():
    """South side houses (5 houses, z=53+)"""
    lines = [comment("Phase 4: South side houses")]
    random.seed(456)
    plots = [
        (0,  53, 2),   # house 6
        (22, 53, 0),   # house 7
        (50, 53, 4),   # house 8
        (72, 53, 1),   # house 9
        (50, 78, 3),   # house 10
    ]
    for px, pz, si in plots:
        build_modern_house(lines, px, pz, si)

    lines.append("function town_park")
    write_func("town_houses2", lines)

def gen_park():
    """Community park at the corner"""
    lines = [comment("Phase 5: Community park")]
    pk_x, pk_z = 0, 78
    pw, pd = 40, 26

    # Grass base
    lines.append(fill(pk_x, 0, pk_z, pk_x+pw-1, 0, pk_z+pd-1, "grass_block"))

    # Paved paths (cross shape)
    lines.append(fill(pk_x+pw//2-1, 0, pk_z, pk_x+pw//2, 0, pk_z+pd-1, "stone"))
    lines.append(fill(pk_x, 0, pk_z+pd//2-1, pk_x+pw-1, 0, pk_z+pd//2, "stone"))

    # Central fountain - contained basin
    fx, fz = pk_x + pw//2 - 2, pk_z + pd//2 - 2
    # Outer base
    lines.append(fill(fx, 0, fz, fx+4, 0, fz+4, "stone_bricks"))
    # Raised basin walls (2 blocks tall to contain water)
    lines.append(fill(fx, 1, fz, fx+4, 2, fz, "stone_bricks"))     # south wall
    lines.append(fill(fx, 1, fz+4, fx+4, 2, fz+4, "stone_bricks")) # north wall
    lines.append(fill(fx, 1, fz, fx, 2, fz+4, "stone_bricks"))     # west wall
    lines.append(fill(fx+4, 1, fz, fx+4, 2, fz+4, "stone_bricks")) # east wall
    # Basin floor
    lines.append(fill(fx+1, 0, fz+1, fx+3, 0, fz+3, "prismarine"))
    # Center pillar
    lines.append(sb(fx+2, 1, fz+2, "stone_bricks"))
    lines.append(sb(fx+2, 2, fz+2, "stone_bricks"))
    lines.append(sb(fx+2, 3, fz+2, "sea_lantern"))
    # Water INSIDE the basin (Y=1, walls go to Y=2 so water is contained)
    lines.append(sb(fx+1, 1, fz+1, "water"))
    lines.append(sb(fx+1, 1, fz+2, "water"))
    lines.append(sb(fx+1, 1, fz+3, "water"))
    lines.append(sb(fx+3, 1, fz+1, "water"))
    lines.append(sb(fx+3, 1, fz+2, "water"))
    lines.append(sb(fx+3, 1, fz+3, "water"))
    lines.append(sb(fx+2, 1, fz+1, "water"))
    lines.append(sb(fx+2, 1, fz+3, "water"))

    # Trees (scattered)
    random.seed(789)
    tree_spots = [(5, 5), (30, 5), (8, 20), (32, 18), (15, 10), (25, 15)]
    for tx_off, tz_off in tree_spots:
        tx, tz = pk_x + tx_off, pk_z + tz_off
        for dy in range(1, 6):
            lines.append(sb(tx, dy, tz, "oak_log"))
        lines.append(fill(tx-2, 6, tz-2, tx+2, 7, tz+2, "oak_leaves"))
        lines.append(fill(tx-1, 8, tz-1, tx+1, 8, tz+1, "oak_leaves"))

    # Benches
    for bx_off in [8, 22, 15]:
        bx, bz = pk_x + bx_off, pk_z + pd//2 + 2
        lines.append(fill(bx, 1, bz, bx+2, 1, bz, "spruce_planks"))
        lines.append(sb(bx, 1, bz+1, "spruce_planks"))
        lines.append(sb(bx+2, 1, bz+1, "spruce_planks"))

    # Playground area
    # Swing frame
    lines.append(fill(pk_x+5, 1, pk_z+pd-5, pk_x+5, 4, pk_z+pd-5, "iron_block"))
    lines.append(fill(pk_x+9, 1, pk_z+pd-5, pk_x+9, 4, pk_z+pd-5, "iron_block"))
    lines.append(fill(pk_x+5, 4, pk_z+pd-5, pk_x+9, 4, pk_z+pd-5, "iron_block"))
    # Sand pit
    lines.append(fill(pk_x+12, 0, pk_z+pd-6, pk_x+16, 0, pk_z+pd-3, "sand"))

    # Park lights
    for lx in [3, pw-4]:
        for lz_off in [3, pd-4]:
            lx_abs, lz_abs = pk_x+lx, pk_z+lz_off
            lines.append(fill(lx_abs, 1, lz_abs, lx_abs, 4, lz_abs, "iron_block"))
            lines.append(sb(lx_abs, 5, lz_abs, "glowstone"))

    # Flower beds
    flowers = ["red_flower", "yellow_flower"]
    for fx_off in range(3, 18, 3):
        lines.append(sb(pk_x+fx_off, 1, pk_z+2, flowers[fx_off % 2]))
    for fx_off in range(22, 37, 3):
        lines.append(sb(pk_x+fx_off, 1, pk_z+pd-2, flowers[fx_off % 2]))

    write_func("town_park", lines)

# ── Generate all ──
if __name__ == "__main__":
    print("Generating Modern Town...")
    gen_master()
    gen_clear()
    gen_roads()
    gen_houses1()
    gen_houses2()
    gen_park()
    print("\nDone! Run /function build_town in-game.")
