"""
Roller Coaster Generator with Minecart Rails
Generates a full circuit roller coaster for Minecraft Bedrock Edition
"""
import os

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

# ── Track constants ──
BASE_Y = 3          # station height
PEAK_Y = 28         # big hill peak
PEAK2_Y = 15        # second hill peak

def lay_rail(lines, x, y, z, powered=False):
    """Place one rail segment: support column + track bed + rail"""
    # Support column from ground
    if y > 0:
        lines.append(fill(x, 0, z, x, y-1, z, "stone_bricks"))
    # Track bed + rail
    if powered:
        lines.append(sb(x, y, z, "redstone_block"))
        lines.append(sb(x, y+1, z, "golden_rail"))
    else:
        lines.append(sb(x, y, z, "stone_bricks"))
        lines.append(sb(x, y+1, z, "rail"))

def lay_section(lines, points, powered_every=6, all_powered=False):
    """Lay rail along a list of (x, y, z) points"""
    for i, (x, y, z) in enumerate(points):
        powered = all_powered or (i % powered_every == 0)
        lay_rail(lines, x, y, z, powered)

# ═══════════════════════════════════════════
# TRACK LAYOUT (rectangular circuit)
#
#   STATION ──East──> CLIMB ──> PEAK ──> DROP ──>┐
#      ^                                          │ South
#      │ North                                    v
#      └──West── FIREWORKS ── HILL2 ── TUNNEL ──┘
#
# East leg: Z=0,  X=0..80
# South connector: X=80, Z=0..40
# West leg: Z=40, X=80..0
# North connector: X=0, Z=40..0
# ═══════════════════════════════════════════

def gen_master():
    lines = [
        comment("EPIC ROLLER COASTER WITH MINECART RAILS"),
        comment("After building, place a minecart on the station rail and hop in!"),
        comment("Run /function coaster_fireworks at the finale for fireworks!"),
        "function coaster_clear",
    ]
    write_func("build_coaster", lines)

def gen_clear():
    lines = [comment("Phase 1: Clear area")]
    # Clear in strips to avoid overload
    for xs in range(-10, 100, 40):
        xe = min(xs + 39, 100)
        lines.append(fill(xs, -1, -10, xe, PEAK_Y + 10, 50, "air"))
    lines.append(fill(-10, -1, -10, 100, 0, 50, "grass_block"))
    lines.append("function coaster_station")
    write_func("coaster_clear", lines)

def gen_station():
    lines = [comment("Phase 2: Station platform + launch")]

    # ── Station platform ──
    lines.append(fill(-5, BASE_Y, -4, 12, BASE_Y, 4, "quartz_block"))
    lines.append(fill(-5, 0, -4, 12, BASE_Y-1, -4, "quartz_block"))  # front wall
    lines.append(fill(-5, 0, 4, 12, BASE_Y-1, 4, "quartz_block"))    # back wall
    lines.append(fill(-5, 0, -3, -5, BASE_Y-1, 3, "quartz_block"))   # left wall
    # Stairs up to platform
    for i in range(BASE_Y):
        lines.append(fill(-5-i, i, -2, -5-i, i, 2, "quartz_block"))

    # ── Grand entrance arch ──
    lines.append(fill(-2, BASE_Y+1, -5, -2, BASE_Y+6, -5, "red_concrete"))
    lines.append(fill(10, BASE_Y+1, -5, 10, BASE_Y+6, -5, "red_concrete"))
    lines.append(fill(-1, BASE_Y+6, -5, 9, BASE_Y+7, -5, "red_concrete"))
    lines.append(fill(0, BASE_Y+7, -5, 8, BASE_Y+8, -5, "yellow_concrete"))
    # Sign posts
    lines.append(fill(2, BASE_Y+6, -5, 6, BASE_Y+6, -5, "white_concrete"))
    # Lights on arch
    lines.append(sb(0, BASE_Y+7, -5, "glowstone"))
    lines.append(sb(8, BASE_Y+7, -5, "glowstone"))
    lines.append(sb(4, BASE_Y+8, -5, "sea_lantern"))

    # ── Station rails ──
    # Brake/stop section (powered OFF = brakes)
    for x in range(0, 5):
        lines.append(sb(x, BASE_Y, 0, "stone_bricks"))
        lines.append(sb(x, BASE_Y+1, 0, "rail"))

    # Launch section (all powered rails on redstone blocks)
    points_launch = [(x, BASE_Y, 0) for x in range(5, 19)]
    lay_section(lines, points_launch, all_powered=True)

    # ── Safety railings along station ──
    lines.append(fill(0, BASE_Y+1, -1, 12, BASE_Y+1, -1, "iron_bars"))
    lines.append(fill(0, BASE_Y+1, 1, 12, BASE_Y+1, 1, "iron_bars"))

    # ── Station lighting ──
    for x in range(-3, 12, 4):
        lines.append(sb(x, BASE_Y+4, 0, "glowstone"))

    lines.append("function coaster_climb")
    write_func("coaster_station", lines)

def gen_climb():
    lines = [comment("Phase 3: Big hill climb (Y=3 to Y=28)")]

    # ── Climb section: 25 blocks up ──
    points = []
    for i in range(25):
        points.append((19 + i, BASE_Y + 1 + i, 0))
    lay_section(lines, points, powered_every=2)  # lots of power for climbing

    # ── Colored arches over the climb (every 5 blocks) ──
    colors = ["red_concrete", "orange_concrete", "yellow_concrete",
              "lime_concrete", "blue_concrete"]
    for i, color in enumerate(colors):
        cx = 21 + i * 5
        cy = BASE_Y + 3 + i * 5
        lines.append(fill(cx, cy, -2, cx, cy+3, -2, color))
        lines.append(fill(cx, cy, 2, cx, cy+3, 2, color))
        lines.append(fill(cx, cy+3, -1, cx, cy+3, 1, color))

    # ── Support cross-beams (A-frame supports) ──
    for i in range(0, 25, 4):
        cx = 19 + i
        cy = BASE_Y + 1 + i
        if cy > 5:
            lines.append(fill(cx, 0, -1, cx, cy-1, -1, "iron_block"))
            lines.append(fill(cx, 0, 1, cx, cy-1, 1, "iron_block"))

    lines.append("function coaster_peak")
    write_func("coaster_climb", lines)

def gen_peak():
    lines = [comment("Phase 4: Peak + big drop")]

    # ── Peak platform at Y=28 ──
    points_peak = [(x, PEAK_Y, 0) for x in range(44, 51)]
    lay_section(lines, points_peak, powered_every=3)

    # Observation platform at peak
    lines.append(fill(45, PEAK_Y, -3, 49, PEAK_Y, 3, "quartz_block"))
    lines.append(fill(45, PEAK_Y+1, -3, 45, PEAK_Y+2, -3, "iron_bars"))
    lines.append(fill(49, PEAK_Y+1, -3, 49, PEAK_Y+2, -3, "iron_bars"))
    lines.append(fill(45, PEAK_Y+1, 3, 49, PEAK_Y+1, 3, "iron_bars"))
    # Lights at peak
    lines.append(sb(47, PEAK_Y+1, -3, "sea_lantern"))
    lines.append(sb(47, PEAK_Y+1, 3, "sea_lantern"))
    # Flag on peak
    lines.append(fill(47, PEAK_Y+1, -4, 47, PEAK_Y+5, -4, "iron_block"))
    lines.append(fill(47, PEAK_Y+4, -4, 47, PEAK_Y+5, -3, "red_wool"))

    # ── Big drop: Y=28 down to Y=3 (25 blocks) ──
    points_drop = []
    for i in range(25):
        points_drop.append((51 + i, PEAK_Y - 1 - i, 0))
    lay_section(lines, points_drop, powered_every=8)

    # Drop warning signs (colored blocks)
    lines.append(fill(50, PEAK_Y+1, -2, 50, PEAK_Y+3, -2, "yellow_concrete"))
    lines.append(fill(50, PEAK_Y+1, 2, 50, PEAK_Y+3, 2, "yellow_concrete"))

    # ── Flat run-out after drop ──
    points_flat = [(x, BASE_Y, 0) for x in range(76, 81)]
    lay_section(lines, points_flat, powered_every=3)

    lines.append("function coaster_south")
    write_func("coaster_peak", lines)

def gen_south():
    lines = [comment("Phase 5: South turn + connector")]

    # ── Corner at (80, 3, 0) — rail auto-turns ──
    # Already have rail at (80, 3, 0) from the flat section

    # ── South connector: small rolling hills ──
    points = []
    for z in range(1, 41):
        # Small sine-wave hills
        if 8 <= z <= 12:
            y = BASE_Y + (z - 8)  # climb 5
        elif 13 <= z <= 17:
            y = BASE_Y + (17 - z)  # drop 5
        elif 22 <= z <= 26:
            y = BASE_Y + (z - 22)  # climb 5
        elif 27 <= z <= 31:
            y = BASE_Y + (31 - z)  # drop 5
        else:
            y = BASE_Y
        points.append((80, y, z))
    lay_section(lines, points, powered_every=4)

    # ── Decorative tunnel of rings ──
    for z in [10, 15, 25, 30]:
        y = BASE_Y + 2
        lines.append(fill(78, y, z, 78, y+4, z, "purple_concrete"))
        lines.append(fill(82, y, z, 82, y+4, z, "purple_concrete"))
        lines.append(fill(79, y+4, z, 81, y+4, z, "purple_concrete"))
    # Lanterns along the south section
    for z in range(2, 40, 5):
        lines.append(sb(78, BASE_Y+2, z, "sea_lantern"))
        lines.append(sb(82, BASE_Y+2, z, "sea_lantern"))

    lines.append("function coaster_tunnel")
    write_func("coaster_south", lines)

def gen_tunnel():
    lines = [comment("Phase 6: West leg + tunnel")]

    # ── Corner at (80, 3, 40) ──
    lay_rail(lines, 80, BASE_Y, 40)

    # ── Flat approach to tunnel ──
    points_flat = [(x, BASE_Y, 40) for x in range(79, 64, -1)]
    lay_section(lines, points_flat, powered_every=5)

    # ── TUNNEL SECTION (x=64 to x=40) ──
    lines.append(comment("--- Themed Tunnel ---"))
    # Build tunnel walls and ceiling
    lines.append(fill(40, 0, 37, 64, 0, 43, "stone_bricks"))
    lines.append(fill(40, 1, 37, 64, BASE_Y+5, 37, "stone_bricks"))  # south wall
    lines.append(fill(40, 1, 43, 64, BASE_Y+5, 43, "stone_bricks"))  # north wall
    lines.append(fill(40, BASE_Y+5, 38, 64, BASE_Y+5, 42, "stone_bricks")) # ceiling
    # Hollow interior
    lines.append(fill(40, 1, 38, 64, BASE_Y+4, 42, "air"))
    # Restore ground inside
    lines.append(fill(40, 0, 38, 64, 0, 42, "stone_bricks"))

    # Track through tunnel
    points_tunnel = [(x, BASE_Y, 40) for x in range(64, 39, -1)]
    lay_section(lines, points_tunnel, powered_every=5)

    # Tunnel decorations
    # Glowstone strips on ceiling
    for x in range(42, 64, 3):
        lines.append(sb(x, BASE_Y+4, 40, "glowstone"))
    # Lava windows (behind glass)
    for x in range(44, 62, 6):
        lines.append(fill(x, 2, 37, x+2, 4, 37, "glass"))
        lines.append(fill(x, 2, 36, x+2, 4, 36, "lava"))
        lines.append(fill(x, 2, 43, x+2, 4, 43, "glass"))
        lines.append(fill(x, 2, 44, x+2, 4, 44, "lava"))
    # Nether theme strips
    for x in range(41, 63, 4):
        lines.append(sb(x, 1, 38, "netherrack"))
        lines.append(sb(x, 1, 42, "netherrack"))

    # ── After tunnel: flat to hill ──
    points_after = [(x, BASE_Y, 40) for x in range(39, 34, -1)]
    lay_section(lines, points_after, powered_every=4)

    lines.append("function coaster_finale")
    write_func("coaster_tunnel", lines)

def gen_finale():
    lines = [comment("Phase 7: Second hill + finale + return")]

    # ── Second hill climb (x=33 down to x=23, y=3 to y=13) ──
    points_climb2 = []
    for i in range(10):
        points_climb2.append((33 - i, BASE_Y + 1 + i, 40))
    lay_section(lines, points_climb2, powered_every=2)

    # ── Second peak (x=22..20) ──
    points_peak2 = [(x, PEAK2_Y - 2, 40) for x in range(22, 19, -1)]
    lay_section(lines, points_peak2, powered_every=2)

    # ── Second drop (x=19 to x=9, y=13 to 3) ──
    points_drop2 = []
    for i in range(10):
        points_drop2.append((19 - i, PEAK2_Y - 3 - i, 40))
    lay_section(lines, points_drop2, powered_every=8)

    # ── FIREWORKS AREA (x=8 to x=1) ──
    lines.append(comment("--- Fireworks Finale ---"))
    points_finale = [(x, BASE_Y, 40) for x in range(8, 0, -1)]
    lay_section(lines, points_finale, powered_every=2)

    # Fireworks platform
    lines.append(fill(-3, 0, 35, 12, 0, 45, "black_concrete"))
    # Firework launcher pedestals
    for x in [-2, 3, 7, 11]:
        lines.append(fill(x, 1, 35, x, 3, 35, "iron_block"))
        lines.append(sb(x, 4, 35, "sea_lantern"))
        lines.append(fill(x, 1, 45, x, 3, 45, "iron_block"))
        lines.append(sb(x, 4, 45, "sea_lantern"))

    # Colorful arches over finale
    finale_colors = ["red_concrete", "orange_concrete", "yellow_concrete",
                     "green_concrete", "blue_concrete", "purple_concrete"]
    for i, color in enumerate(finale_colors):
        ax = 7 - i
        lines.append(fill(ax, BASE_Y+2, 38, ax, BASE_Y+5, 38, color))
        lines.append(fill(ax, BASE_Y+2, 42, ax, BASE_Y+5, 42, color))
        lines.append(fill(ax, BASE_Y+5, 39, ax, BASE_Y+5, 41, color))

    # "FINISH" sign
    lines.append(fill(1, BASE_Y+3, 38, 5, BASE_Y+4, 38, "white_concrete"))
    lines.append(fill(1, BASE_Y+3, 42, 5, BASE_Y+4, 42, "white_concrete"))

    # Star burst decoration
    lines.append(sb(4, BASE_Y+6, 40, "glowstone"))
    lines.append(sb(3, BASE_Y+7, 40, "gold_block"))
    lines.append(sb(5, BASE_Y+7, 40, "gold_block"))
    lines.append(sb(4, BASE_Y+8, 40, "diamond_block"))

    # ── Corner at (0, 3, 40) ──
    lay_rail(lines, 0, BASE_Y, 40)

    # ── North return to station (z=39 down to z=1) ──
    points_return = [(0, BASE_Y, z) for z in range(39, 0, -1)]
    lay_section(lines, points_return, powered_every=4)

    # Railings along return path
    for z in range(5, 38, 6):
        lines.append(sb(-1, BASE_Y+1, z, "iron_bars"))
        lines.append(sb(1, BASE_Y+1, z, "iron_bars"))
        lines.append(sb(-1, BASE_Y+2, z, "sea_lantern"))

    write_func("coaster_finale", lines)

def gen_fireworks():
    """Separate function: summon firework rockets for the show"""
    lines = [comment("FIREWORKS SHOW! Run this at the finale!")]
    # Summon firework rockets at various positions around the finale area
    positions = [
        (-2, 6, 35), (3, 8, 35), (7, 10, 35), (11, 7, 35),
        (-2, 9, 45), (3, 6, 45), (7, 8, 45), (11, 10, 45),
        (4, 12, 40), (0, 11, 40), (8, 9, 40),
        (-1, 8, 37), (5, 10, 43), (9, 7, 38),
        (2, 15, 40), (6, 13, 40), (10, 11, 40),
    ]
    for x, y, z in positions:
        lines.append(f"summon fireworks_rocket ~{x} ~{y} ~{z}")
    # Extra delayed burst effect via offset positions
    for x, y, z in positions[:8]:
        lines.append(f"summon fireworks_rocket ~{x+1} ~{y+5} ~{z}")
    write_func("coaster_fireworks", lines)

# ── Generate all ──
if __name__ == "__main__":
    print("Generating Epic Roller Coaster...")
    gen_master()
    gen_clear()
    gen_station()
    gen_climb()
    gen_peak()
    gen_south()
    gen_tunnel()
    gen_finale()
    gen_fireworks()
    print("\nDone! Run /function build_coaster in-game.")
    print("After riding, run /function coaster_fireworks for a fireworks show!")
