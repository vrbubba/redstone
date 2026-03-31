"""
The Gauntlet - Redstone Minigame Obstacle Course
Features: piston door, arrow traps, lava parkour, ice sprint, piston crushers, fireworks
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

# Course runs along Z axis, x=-2 to x=6 (5-wide corridor)
CX1, CX2 = -2, 6  # corridor X bounds
CW = CX2 - CX1     # corridor width
WALL_H = 6          # wall height
FY = 0              # floor Y

def build_corridor(lines, z1, z2, floor="stone_bricks", wall="stone_bricks", ceil=True):
    """Build a walled corridor section"""
    lines.append(fill(CX1-1, FY, z1, CX2+1, FY, z2, floor))
    lines.append(fill(CX1-1, FY+1, z1, CX1-1, FY+WALL_H, z2, wall))
    lines.append(fill(CX2+1, FY+1, z1, CX2+1, FY+WALL_H, z2, wall))
    if ceil:
        lines.append(fill(CX1, FY+WALL_H, z1, CX2, FY+WALL_H, z2, wall))
    lines.append(fill(CX1, FY+1, z1, CX2, FY+WALL_H-1, z2, "air"))

def gen_master():
    lines = [
        comment("THE GAUNTLET - Redstone Obstacle Course Minigame"),
        comment("6 stages of challenges with real redstone mechanics!"),
        "function gauntlet_clear",
    ]
    write_func("build_gauntlet", lines)

def gen_clear():
    lines = [comment("Phase 1: Clear area")]
    lines.append(fill(-10, -1, -5, 15, 20, 100, "air"))
    lines.append(fill(-10, -1, -5, 15, 0, 100, "stone"))
    lines.append("function gauntlet_start")
    write_func("gauntlet_clear", lines)

def gen_start():
    lines = [comment("Phase 2: Start platform + Stage 1 piston door")]

    # Start platform
    lines.append(fill(-5, FY, -3, 9, FY, 3, "quartz_block"))
    lines.append(fill(-5, FY+1, -3, 9, FY+4, -3, "quartz_block"))
    lines.append(fill(-5, FY+1, 3, 9, FY+4, 3, "quartz_block"))
    lines.append(fill(-5, FY+1, -2, -5, FY+4, 2, "quartz_block"))

    # Entrance arch
    lines.append(fill(-5, FY+1, -4, -5, FY+6, -4, "red_concrete"))
    lines.append(fill(9, FY+1, -4, 9, FY+6, -4, "red_concrete"))
    lines.append(fill(-4, FY+6, -4, 8, FY+7, -4, "red_concrete"))
    lines.append(fill(0, FY+7, -4, 4, FY+8, -4, "yellow_concrete"))
    # "THE GAUNTLET" sign area
    lines.append(fill(0, FY+6, -4, 4, FY+6, -4, "white_concrete"))

    # Piston door (Stage 1)
    lines.append(comment("--- Stage 1: Piston Door ---"))
    # Door blocks (will be pulled by pistons)
    lines.append(fill(1, FY+1, 3, 3, FY+3, 3, "iron_block"))
    # Sticky pistons behind door (facing south, pull door blocks north to open)
    for x in range(1, 4):
        for y in range(FY+1, FY+4):
            lines.append(sb(x, y, 4, 'sticky_piston ["facing_direction"=2]'))
    # Button to open
    lines.append(sb(0, FY+2, 2, 'stone_button ["facing_direction"=3]'))
    # Redstone from button to pistons
    lines.append(sb(0, FY+1, 3, "redstone_wire"))
    lines.append(sb(0, FY+1, 4, "redstone_wire"))
    lines.append(sb(1, FY+1, 5, "redstone_wire"))
    lines.append(sb(2, FY+1, 5, "redstone_wire"))
    lines.append(sb(3, FY+1, 5, "redstone_wire"))
    lines.append(fill(0, FY, 3, 0, FY, 4, "stone"))
    lines.append(fill(1, FY, 5, 3, FY, 5, "stone"))

    # Signs / instructions
    lines.append(fill(-2, FY+2, 0, -2, FY+3, 0, "white_concrete"))
    lines.append(sb(2, FY+4, -2, "sea_lantern"))

    lines.append("function gauntlet_arrows")
    write_func("gauntlet_start", lines)

def gen_arrows():
    lines = [comment("Phase 3: Stage 2 - Arrow Alley with redstone clock")]
    z1, z2 = 5, 28

    # Build corridor
    build_corridor(lines, z1, z2, floor="polished_deepslate", wall="deepslate_bricks")
    # Red warning stripes on floor
    for z in range(z1+1, z2, 3):
        lines.append(fill(CX1, FY, z, CX2, FY, z, "red_concrete"))

    # Dispensers on both walls, facing inward
    lines.append(comment("--- Arrow dispensers ---"))
    for z in range(z1+2, z2-1, 3):
        # Left wall dispenser (facing east = 5)
        lines.append(sb(CX1-1, FY+2, z, 'dispenser ["facing_direction"=5]'))
        # Right wall dispenser (facing west = 4)
        lines.append(sb(CX2+1, FY+2, z, 'dispenser ["facing_direction"=4]'))
        # Fill with arrows
        for slot in range(9):
            lines.append(f"replaceitem block ~{CX1-1} ~{FY+2} ~{z} slot.container {slot} arrow 64")
            lines.append(f"replaceitem block ~{CX2+1} ~{FY+2} ~{z} slot.container {slot} arrow 64")

    # Observer clock (two facing each other = fast pulse)
    lines.append(comment("--- Redstone clock (observer pair) ---"))
    cx, cy, cz = CX1-3, FY+2, z1+10
    # facing_direction: 0=down,1=up,2=north,3=south,4=west,5=east
    lines.append(sb(cx, cy, cz, 'observer ["facing_direction"=5]'))  # facing east
    lines.append(sb(cx+1, cy, cz, 'observer ["facing_direction"=4]'))  # facing west
    # Output from observer back (west side) → wire to dispensers
    lines.append(sb(cx-1, cy, cz, "redstone_wire"))
    lines.append(sb(cx-1, cy-1, cz, "stone"))
    # Run redstone along the wall behind dispensers
    for z in range(z1+1, z2):
        lines.append(sb(CX1-2, FY+2, z, "redstone_wire"))
        lines.append(sb(CX1-2, FY+1, z, "stone"))
    # Connect clock to the wire line
    lines.append(sb(cx-1, cy, cz+1, "redstone_wire"))
    lines.append(sb(cx-1, cy-1, cz+1, "stone"))

    # Right side: separate clock for right dispensers
    cx2 = CX2+3
    lines.append(sb(cx2, cy, cz, 'observer ["facing_direction"=4]'))  # facing west
    lines.append(sb(cx2+1, cy, cz, 'observer ["facing_direction"=5]'))  # facing east
    lines.append(sb(cx2+2, cy, cz, "redstone_wire"))
    lines.append(sb(cx2+2, cy-1, cz, "stone"))
    for z in range(z1+1, z2):
        lines.append(sb(CX2+2, FY+2, z, "redstone_wire"))
        lines.append(sb(CX2+2, FY+1, z, "stone"))

    # Warning lamps at entrance
    lines.append(sb(CX1, FY+4, z1, "redstone_lamp"))
    lines.append(sb(CX2, FY+4, z1, "redstone_lamp"))

    lines.append("function gauntlet_lava")
    write_func("gauntlet_arrows", lines)

def gen_lava():
    lines = [comment("Phase 4: Stage 3 - Lava Parkour")]
    z1, z2 = 30, 55

    # Lava pit with walls
    lines.append(fill(CX1-1, FY-3, z1, CX2+1, FY-3, z2, "stone"))
    lines.append(fill(CX1-1, FY-2, z1, CX2+1, FY, z2, "air"))
    lines.append(fill(CX1-1, FY-2, z1, CX2+1, FY+WALL_H, z1, "stone_bricks"))
    lines.append(fill(CX1-1, FY-2, z2, CX2+1, FY+WALL_H, z2, "stone_bricks"))
    lines.append(fill(CX1-1, FY-2, z1, CX1-1, FY+WALL_H, z2, "stone_bricks"))
    lines.append(fill(CX2+1, FY-2, z1, CX2+1, FY+WALL_H, z2, "stone_bricks"))
    # Lava floor
    lines.append(fill(CX1, FY-2, z1+1, CX2, FY-2, z2-1, "lava"))
    # Entry/exit platforms
    lines.append(fill(CX1, FY, z1, CX2, FY, z1+1, "stone_bricks"))
    lines.append(fill(CX1, FY, z2-1, CX2, FY, z2, "stone_bricks"))

    # Parkour pillars (increasingly spaced)
    pillars = [(2, z1+4), (1, z1+7), (3, z1+11), (0, z1+15),
               (4, z1+18), (2, z1+22), (3, z1+25)]
    for px, pz in pillars:
        lines.append(fill(px, FY-2, pz, px, FY, pz, "stone_bricks"))
        lines.append(sb(px, FY+1, pz, "sea_lantern"))

    # Decorative lava lighting
    for z in range(z1+2, z2-1, 5):
        lines.append(sb(CX1-1, FY+3, z, "glowstone"))
        lines.append(sb(CX2+1, FY+3, z, "glowstone"))

    lines.append("function gauntlet_ice")
    write_func("gauntlet_lava", lines)

def gen_ice():
    lines = [comment("Phase 5: Stage 4 - Ice Sprint + Stage 5 - Piston Crushers")]
    z1, z2 = 57, 72

    # Ice sprint section
    build_corridor(lines, z1, z2, floor="packed_ice", wall="blue_ice")
    # Gaps in ice (fall back to start of section)
    for z in [z1+3, z1+7, z1+11]:
        lines.append(fill(CX1+1, FY, z, CX2-1, FY, z, "air"))
        lines.append(fill(CX1+1, FY-1, z, CX2-1, FY-1, z, "water"))

    # Soul sand slow patches
    for z in [z1+5, z1+9]:
        lines.append(fill(CX1, FY, z, CX2, FY, z, "soul_sand"))

    # Stage 5: Piston crushers
    lines.append(comment("--- Stage 5: Piston Crushers ---"))
    pz1, pz2 = 74, 88
    build_corridor(lines, pz1, pz2, floor="stone_bricks", wall="deepslate_bricks")

    # Sticky pistons on walls at intervals, with blocks attached
    for z in range(pz1+2, pz2-1, 3):
        # Left pistons (facing east = 5)
        lines.append(sb(CX1-1, FY+1, z, 'sticky_piston ["facing_direction"=5]'))
        lines.append(sb(CX1-1, FY+2, z, 'sticky_piston ["facing_direction"=5]'))
        lines.append(sb(CX1, FY+1, z, "stone"))
        lines.append(sb(CX1, FY+2, z, "stone"))
        # Right pistons offset (facing west = 4)
        if z + 1 < pz2:
            lines.append(sb(CX2+1, FY+1, z+1, 'sticky_piston ["facing_direction"=4]'))
            lines.append(sb(CX2+1, FY+2, z+1, 'sticky_piston ["facing_direction"=4]'))
            lines.append(sb(CX2, FY+1, z+1, "stone"))
            lines.append(sb(CX2, FY+2, z+1, "stone"))

    # Observer clocks for pistons (one per side)
    # facing_direction: 4=west, 5=east
    for side_x, dir1, dir2 in [(CX1-3, 5, 4), (CX2+3, 4, 5)]:
        lines.append(sb(side_x, FY+1, pz1+5, f'observer ["facing_direction"={dir1}]'))
        dx = 1 if dir1 == 5 else -1
        lines.append(sb(side_x+dx, FY+1, pz1+5, f'observer ["facing_direction"={dir2}]'))
        # Wire from observer to piston line
        wire_x = CX1-2 if side_x < 0 else CX2+2
        for z in range(pz1+2, pz2):
            lines.append(sb(wire_x, FY+1, z, "redstone_wire"))
            lines.append(sb(wire_x, FY, z, "stone"))

    # Corridor lights
    for z in range(pz1, pz2+1, 4):
        lines.append(sb(CX1, FY+WALL_H-1, z, "redstone_lamp"))
        lines.append(sb(CX2, FY+WALL_H-1, z, "redstone_lamp"))

    lines.append("function gauntlet_finish")
    write_func("gauntlet_ice", lines)

def gen_finish():
    lines = [comment("Phase 6: Stage 6 - Victory Platform")]
    z1 = 90

    # Victory platform
    lines.append(fill(-4, FY, z1, 8, FY, z1+12, "gold_block"))
    lines.append(fill(-4, FY+1, z1+12, 8, FY+5, z1+12, "quartz_block"))
    # Victory arch
    lines.append(fill(-2, FY+1, z1, -2, FY+6, z1, "emerald_block"))
    lines.append(fill(6, FY+1, z1, 6, FY+6, z1, "emerald_block"))
    lines.append(fill(-1, FY+6, z1, 5, FY+7, z1, "emerald_block"))
    lines.append(fill(0, FY+7, z1, 4, FY+8, z1, "diamond_block"))
    # "VICTORY" sign
    lines.append(fill(0, FY+6, z1, 4, FY+6, z1, "white_concrete"))

    # Beacon
    lines.append(fill(1, FY-1, z1+6, 3, FY-1, z1+8, "iron_block"))
    lines.append(fill(0, FY, z1+5, 4, FY, z1+9, "iron_block"))
    lines.append(sb(2, FY+1, z1+7, "beacon"))

    # Firework dispensers (detector plate triggered)
    for x in [-3, 1, 5]:
        lines.append(sb(x, FY, z1+3, 'dispenser ["facing_direction"=1]'))
        for slot in range(5):
            lines.append(f"replaceitem block ~{x} ~{FY} ~{z1+3} slot.container {slot} firework_rocket 1")
    # Pressure plate to trigger fireworks
    lines.append(sb(2, FY+1, z1+3, "stone_pressure_plate"))
    lines.append(sb(2, FY, z1+3, "stone"))
    # Wire connecting pressure plate to dispensers
    lines.append(fill(-3, FY-1, z1+2, 5, FY-1, z1+2, "stone"))
    for x in range(-3, 6):
        lines.append(sb(x, FY, z1+2, "redstone_wire"))

    # Reward chest
    lines.append(sb(2, FY+1, z1+9, "chest"))

    # Celebration lights
    for x in range(-3, 8, 2):
        lines.append(sb(x, FY+1, z1+11, "sea_lantern"))

    # Bonus: manual fireworks function
    lines.append(comment("Run /function gauntlet_fireworks for bonus show!"))
    write_func("gauntlet_finish", lines)

def gen_fireworks():
    lines = [comment("GAUNTLET VICTORY FIREWORKS!")]
    for x in range(-4, 9, 2):
        for z in range(90, 103, 3):
            lines.append(f"summon fireworks_rocket ~{x} ~{FY+5} ~{z}")
    write_func("gauntlet_fireworks", lines)

if __name__ == "__main__":
    print("Generating The Gauntlet Minigame...")
    gen_master()
    gen_clear()
    gen_start()
    gen_arrows()
    gen_lava()
    gen_ice()
    gen_finish()
    gen_fireworks()
    print("\nDone! Run /function build_gauntlet in-game.")
