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

# ── Mountain parameters ──
MTN_CX, MTN_CZ = 0, 0
MTN_RADIUS = 60               # slightly smaller base for performance
MTN_HEIGHT = 100               # 100 blocks tall
SNOW_LINE = 70
TREE_LINE = 50
ICE_CAP = 85

# ── Skyscraper cluster ──
CITY_X = 100
CITY_Z = -30
SKYSCRAPERS = [
    # (x_offset, z_offset, width, depth, height, name)
    (0,   0,  14, 14, 70, "Tower Alpha"),
    (20,  5,  10, 10, 50, "Tower Beta"),
    (34, -5,  12, 12, 90, "Tower Gamma"),
    (50,  8,  10, 10, 40, "Tower Delta"),
    (16, 20,  16, 12, 60, "Tower Epsilon"),
    (38, 18,  10, 10, 48, "Tower Zeta"),
]

# ─────────────────────────────────────────
def gen_master():
    lines = [
        comment("GIANT MOUNTAIN WITH ICE CAPS + SKYSCRAPER CITY"),
        comment("Run: /function build_mountain_city"),
        "function mtn_clear1",
    ]
    write_func("build_mountain_city", lines)

def gen_clear():
    """Split clearing into 2 phases to avoid command overload"""
    # Phase 1: clear air in vertical slices
    lines1 = [comment("Phase 1a: Clear upper air")]
    # Only clear 200x110x180 (much smaller)
    for x_start in range(-80, 220, 60):
        x_end = min(x_start + 59, 220)
        lines1.append(fill(x_start, 1, -80, x_end, MTN_HEIGHT+10, 100, "air"))
    lines1.append("function mtn_clear2")
    write_func("mtn_clear1", lines1)

    lines2 = [comment("Phase 1b: Set ground")]
    lines2.append(fill(-80, -1, -80, 220, 0, 100, "grass_block"))
    lines2.append("function mtn_base1")
    write_func("mtn_clear2", lines2)

def gen_mountain():
    """Split mountain into 3 files by Y range"""
    # ── Base: Y=1 to 35 ──
    lines = [comment("Phase 2: Mountain base (Y=1-35)")]
    for y in range(1, 36):
        t = y / MTN_HEIGHT
        r = int(MTN_RADIUS * (1.0 - t**0.6))
        if r < 1: break
        block = "dirt" if y <= 3 else "stone"
        # Fill row-by-row to keep command count low
        for dx in range(-r, r+1, 30):
            ex = min(dx + 29, r)
            half_z = int(math.sqrt(max(0, r*r - max(abs(dx),abs(ex))**2)))
            if half_z > 0:
                lines.append(fill(MTN_CX+dx, y, MTN_CZ-half_z,
                                  MTN_CX+ex, y, MTN_CZ+half_z, block))
        # Grass cap on surface
        if y > 5 and y < 25:
            sr = min(r-1, 30)
            if sr > 0:
                lines.append(fill(MTN_CX-sr, y, MTN_CZ-sr,
                                  MTN_CX+sr, y, MTN_CZ+sr, "grass_block"))
    lines.append("function mtn_base2")
    write_func("mtn_base1", lines)

    # ── Mid: Y=36 to 65 ──
    lines = [comment("Phase 3: Mountain mid (Y=36-65)")]
    for y in range(36, 66):
        t = y / MTN_HEIGHT
        r = int(MTN_RADIUS * (1.0 - t**0.6))
        if r < 1: break
        for dx in range(-r, r+1, 30):
            ex = min(dx + 29, r)
            half_z = int(math.sqrt(max(0, r*r - max(abs(dx),abs(ex))**2)))
            if half_z > 0:
                lines.append(fill(MTN_CX+dx, y, MTN_CZ-half_z,
                                  MTN_CX+ex, y, MTN_CZ+half_z, "stone"))
    # Trees on lower slopes
    random.seed(42)
    for _ in range(40):
        angle = random.uniform(0, 2*math.pi)
        dist = random.uniform(15, 40)
        tx = MTN_CX + int(dist * math.cos(angle))
        tz = MTN_CZ + int(dist * math.sin(angle))
        ty = int(MTN_HEIGHT * (1.0 - (dist/MTN_RADIUS)**(1/0.6)))
        if 10 < ty < TREE_LINE:
            for dy in range(1, 5):
                lines.append(sb(tx, ty+dy, tz, "oak_log"))
            lines.append(fill(tx-2, ty+5, tz-2, tx+2, ty+6, tz+2, "oak_leaves"))
            lines.append(fill(tx-1, ty+7, tz-1, tx+1, ty+7, tz+1, "oak_leaves"))
    lines.append("function mtn_peak")
    write_func("mtn_base2", lines)

    # ── Peak: Y=66 to summit + ice cap ──
    lines = [comment("Phase 4: Mountain peak with ice cap")]
    for y in range(66, MTN_HEIGHT + 1):
        t = y / MTN_HEIGHT
        r = int(MTN_RADIUS * (1.0 - t**0.6))
        if r < 1: r = 1
        if y >= ICE_CAP:
            block = "blue_ice"
        elif y >= SNOW_LINE:
            block = "snow"
        else:
            block = "stone"
        for dx in range(-r, r+1, 30):
            ex = min(dx + 29, r)
            half_z = int(math.sqrt(max(0, r*r - max(abs(dx),abs(ex))**2)))
            if half_z > 0:
                lines.append(fill(MTN_CX+dx, y, MTN_CZ-half_z,
                                  MTN_CX+ex, y, MTN_CZ+half_z, block))
    # Ice spikes at summit
    for dx, dz in [(-2,0),(2,0),(0,-2),(0,2),(0,0)]:
        for dy in range(MTN_HEIGHT+1, MTN_HEIGHT+6):
            lines.append(sb(MTN_CX+dx, dy, MTN_CZ+dz, "packed_ice"))
    lines.append(sb(MTN_CX, MTN_HEIGHT+6, MTN_CZ, "sea_lantern"))
    lines.append(sb(MTN_CX, MTN_HEIGHT+7, MTN_CZ, "blue_ice"))

    # Snow patches
    random.seed(99)
    for _ in range(50):
        angle = random.uniform(0, 2*math.pi)
        dist = random.uniform(5, 25)
        sx = MTN_CX + int(dist * math.cos(angle))
        sz = MTN_CZ + int(dist * math.sin(angle))
        sy = int(MTN_HEIGHT * (1.0 - (dist/MTN_RADIUS)**(1/0.6)))
        if SNOW_LINE - 8 < sy < SNOW_LINE:
            lines.append(sb(sx, sy+1, sz, "snow"))

    lines.append("function mtn_city1")
    write_func("mtn_peak", lines)

def build_tower(lines, bx, bz, w, d, h, idx, name):
    """Build one skyscraper at (bx, bz) with given dimensions"""
    lines.append(comment(f"--- {name} ({w}x{d}, {h} tall) ---"))
    lines.append(fill(bx, -1, bz, bx+w, -1, bz+d, "stone_bricks"))

    floor_h = 5
    for fy in range(0, h, floor_h):
        yb = fy
        yt = min(fy + floor_h, h)
        # Floor slab
        lines.append(fill(bx, yb, bz, bx+w, yb, bz+d, "polished_deepslate"))
        # Solid walls on all 4 sides
        lines.append(fill(bx, yb+1, bz, bx+w, yt-1, bz, "iron_block"))
        lines.append(fill(bx, yb+1, bz+d, bx+w, yt-1, bz+d, "iron_block"))
        lines.append(fill(bx, yb+1, bz, bx, yt-1, bz+d, "iron_block"))
        lines.append(fill(bx+w, yb+1, bz, bx+w, yt-1, bz+d, "iron_block"))
        # Hollow interior
        lines.append(fill(bx+1, yb+1, bz+1, bx+w-1, yt-1, bz+d-1, "air"))
        # Glass windows between iron columns (every 4 blocks)
        sp = 4
        for wx in range(bx+2, bx+w-1, sp):
            we = min(wx+sp-2, bx+w-2)
            if we > wx:
                lines.append(fill(wx, yb+2, bz, we, yt-2, bz, "glass"))
                lines.append(fill(wx, yb+2, bz+d, we, yt-2, bz+d, "glass"))
        for wz in range(bz+2, bz+d-1, sp):
            we = min(wz+sp-2, bz+d-2)
            if we > wz:
                lines.append(fill(bx, yb+2, wz, bx, yt-2, we, "glass"))
                lines.append(fill(bx+w, yb+2, wz, bx+w, yt-2, we, "glass"))
        # Beams all 4 sides
        lines.append(fill(bx, yt, bz, bx+w, yt, bz, "iron_block"))
        lines.append(fill(bx, yt, bz+d, bx+w, yt, bz+d, "iron_block"))
        lines.append(fill(bx, yt, bz+1, bx, yt, bz+d-1, "iron_block"))
        lines.append(fill(bx+w, yt, bz+1, bx+w, yt, bz+d-1, "iron_block"))
        # Floor light
        lines.append(sb(bx+w//2, yb, bz+d//2, "glowstone"))

    # Roof
    lines.append(fill(bx, h, bz, bx+w, h, bz+d, "polished_deepslate"))
    # Rooftop features
    if idx == 2:  # Tallest - spire
        for dy in range(1, 15):
            lines.append(sb(bx+w//2, h+dy, bz+d//2, "iron_block"))
        lines.append(sb(bx+w//2, h+15, bz+d//2, "redstone_lamp"))
    elif idx == 0:  # Helipad
        lines.append(fill(bx+3, h+1, bz+3, bx+w-3, h+1, bz+d-3, "gray_concrete"))
        lines.append(fill(bx+5, h+1, bz+5, bx+6, h+1, bz+d-5, "yellow_concrete"))
        lines.append(fill(bx+w-6, h+1, bz+5, bx+w-5, h+1, bz+d-5, "yellow_concrete"))
    else:
        lines.append(fill(bx+2, h+1, bz+2, bx+4, h+2, bz+4, "iron_block"))

    # Lobby
    lines.append(fill(bx+w//2-2, 1, bz, bx+w//2+2, 4, bz, "air"))
    lines.append(fill(bx+w//2-2, 5, bz, bx+w//2+2, 5, bz, "iron_block"))

def gen_city():
    """Split city into 2 function files (3 towers each)"""
    # ── City part 1: ground + towers 0-2 ──
    lines = [comment("Phase 5a: City ground + Towers 1-3")]
    cx1, cz1 = CITY_X - 10, CITY_Z - 20
    cx2, cz2 = CITY_X + 70, CITY_Z + 45
    lines.append(fill(cx1, 0, cz1, cx2, 0, cz2, "gray_concrete"))
    lines.append(fill(cx1, 0, CITY_Z-2, cx2, 0, CITY_Z+2, "black_concrete"))
    lines.append(fill(CITY_X+30, 0, cz1, CITY_X+34, 0, cz2, "black_concrete"))
    for x in range(cx1, cx2, 6):
        lines.append(fill(x, 0, CITY_Z, x+2, 0, CITY_Z, "yellow_concrete"))

    for i in range(3):
        xo, zo, w, d, h, name = SKYSCRAPERS[i]
        build_tower(lines, CITY_X+xo, CITY_Z+zo, w, d, h, i, name)

    lines.append("function mtn_city2")
    write_func("mtn_city1", lines)

    # ── City part 2: towers 3-5 + street furniture ──
    lines = [comment("Phase 5b: Towers 4-6 + street furniture")]
    for i in range(3, 6):
        xo, zo, w, d, h, name = SKYSCRAPERS[i]
        build_tower(lines, CITY_X+xo, CITY_Z+zo, w, d, h, i, name)

    # Street lights
    for x in range(cx1+5, cx2, 15):
        lines.append(fill(x, 1, CITY_Z-4, x, 4, CITY_Z-4, "iron_block"))
        lines.append(sb(x, 5, CITY_Z-4, "glowstone"))
        lines.append(fill(x, 1, CITY_Z+4, x, 4, CITY_Z+4, "iron_block"))
        lines.append(sb(x, 5, CITY_Z+4, "glowstone"))

    # Park
    lines.append(fill(CITY_X-12, 0, CITY_Z-12, CITY_X-4, 0, CITY_Z+25, "grass_block"))
    random.seed(77)
    for _ in range(8):
        px = CITY_X-11 + random.randint(0, 6)
        pz = CITY_Z-10 + random.randint(0, 32)
        for dy in range(1, 5):
            lines.append(sb(px, dy, pz, "oak_log"))
        lines.append(fill(px-1, 5, pz-1, px+1, 6, pz+1, "oak_leaves"))

    write_func("mtn_city2", lines)

# ── Generate all ──
if __name__ == "__main__":
    print("Generating Mountain + Skyscraper City...")
    gen_master()
    gen_clear()
    gen_mountain()
    gen_city()
    print("\nDone! Run /function build_mountain_city in-game.")
