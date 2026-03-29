"""
Bezos Warner Estate Mega Mansion Generator
Generates 15 .mcfunction files for Minecraft Bedrock Edition
"""
import os

OUT = r"c:\Users\abhbu\repos\redstone\BedrockPack\functions"

def write_func(name, lines):
    path = os.path.join(OUT, f"{name}.mcfunction")
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"  Wrote {name}.mcfunction ({len(lines)} commands)")

def fill(x1,y1,z1,x2,y2,z2,block):
    return f"fill ~{x1} ~{y1} ~{z1} ~{x2} ~{y2} ~{z2} {block}"

def sb(x,y,z,block):
    return f"setblock ~{x} ~{y} ~{z} {block}"

def comment(text):
    return f"# {text}"

# Layout constants
# Main palace U-shape
BACK_X1, BACK_X2 = 0, 140  # back section X
BACK_Z1, BACK_Z2 = 60, 100 # back section Z
LW_X1, LW_X2 = 0, 35       # left wing X
LW_Z1, LW_Z2 = 25, 60      # left wing Z
RW_X1, RW_X2 = 105, 140    # right wing X
RW_Z1, RW_Z2 = 25, 60      # right wing Z
WALL = 2                    # wall thickness offset
FH = 8                      # floor height
FLOORS = 3

def gen_master():
    """Master file that chains all phases"""
    lines = [
        comment("BEZOS WARNER ESTATE - ULTRA MEGA MANSION"),
        comment("Run this one command to build the entire compound"),
        comment("WARNING: ~300x250 blocks, find a VERY flat open area!"),
        "function bezos_clear",
    ]
    write_func("build_bezos_mansion", lines)

def gen_clear():
    lines = [
        comment("Phase 1: Clear and landscape"),
        fill(-50,-6,-20, 200,30,260, "air"),
        fill(-50,-1,-20, 200,-1,260, "grass_block"),
        "function bezos_driveway",
    ]
    write_func("bezos_clear", lines)

def gen_driveway():
    lines = [comment("Phase 2: Driveway, motor court, gate, perimeter")]
    # Grand driveway
    for z in range(-15, 26):
        lines.append(fill(65,-1,z, 75,-1,z, "polished_deepslate"))
        lines.append(fill(65,0,z, 75,0,z, "polished_deepslate"))
    # Motor court circle
    lines.append(fill(40,0,22, 100,0,38, "polished_deepslate"))
    lines.append(fill(40,-1,22, 100,-1,38, "polished_deepslate"))
    # Fountain
    lines.append(fill(63,1,27, 77,1,33, "quartz_block"))
    lines.append(fill(65,2,28, 75,2,32, "prismarine"))
    lines.append(fill(67,3,29, 73,3,31, "prismarine"))
    lines.append(fill(69,4,30, 71,4,30, "sea_lantern"))
    lines.append(sb(70,5,30, "gold_block"))
    # Driveway trees (8 sycamores)
    for i, z in enumerate(range(-10, 22, 8)):
        for x in [62, 78]:
            lines.append(fill(x,1,z, x,6,z, "oak_log"))
            lines.append(fill(x-2,6,z-2, x+2,9,z+2, "leaves"))
    # Front flower beds (at ground level, not floating)
    lines.append(fill(20,0,20, 55,0,22, "grass_block"))
    lines.append(fill(85,0,20, 120,0,22, "grass_block"))
    for x in range(22, 55, 4):
        lines.append(sb(x,1,21, "red_flower" if x%8==2 else "yellow_flower"))
    for x in range(87, 120, 4):
        lines.append(sb(x,1,21, "yellow_flower" if x%8==3 else "red_flower"))
    # Gate pillars
    lines.append(fill(61,1,-18, 64,8,-18, "stone_bricks"))
    lines.append(fill(76,1,-18, 79,8,-18, "stone_bricks"))
    lines.append(sb(62,9,-18, "sea_lantern"))
    lines.append(sb(77,9,-18, "sea_lantern"))
    lines.append(fill(65,1,-18, 75,5,-18, "iron_bars"))
    # Perimeter hedges
    lines.append(fill(-50,1,-20, 60,5,-20, "leaves"))
    lines.append(fill(80,1,-20, 200,5,-20, "leaves"))
    lines.append(fill(-50,1,-20, -50,5,260, "leaves"))
    lines.append(fill(200,1,-20, 200,5,260, "leaves"))
    lines.append(fill(-50,1,260, 200,5,260, "leaves"))
    lines.append("function bezos_exterior")
    write_func("bezos_driveway", lines)

def gen_exterior():
    lines = [comment("Phase 3: Palace exterior shell - 3 stories")]
    # Foundation
    lines.append(fill(BACK_X1,-1,LW_Z1, BACK_X2,-1,BACK_Z2, "quartz_block"))
    lines.append(fill(LW_X1,-1,LW_Z1, LW_X2,-1,LW_Z2, "quartz_block"))
    lines.append(fill(RW_X1,-1,RW_Z1, RW_X2,-1,RW_Z2, "quartz_block"))
    # Build each floor
    for floor in range(FLOORS):
        yb = floor * FH  # y base
        yt = yb + FH     # y top
        flr = "dark_oak_planks"
        # Floor surface
        lines.append(fill(BACK_X1,yb,LW_Z1, BACK_X2,yb,BACK_Z2, flr))
        lines.append(fill(LW_X1,yb,LW_Z1, LW_X2,yb,BACK_Z1, flr))
        lines.append(fill(RW_X1,yb,RW_Z1, RW_X2,yb,BACK_Z1, flr))
        # Walls - back section
        lines.append(fill(BACK_X1,yb+1,BACK_Z1, BACK_X2,yt,BACK_Z2, "quartz_block"))
        lines.append(fill(BACK_X1+WALL,yb+1,BACK_Z1+WALL, BACK_X2-WALL,yt,BACK_Z2-WALL, "air"))
        # Walls - left wing
        lines.append(fill(LW_X1,yb+1,LW_Z1, LW_X2,yt,LW_Z2, "quartz_block"))
        lines.append(fill(LW_X1+WALL,yb+1,LW_Z1+WALL, LW_X2-WALL,yt,LW_Z2-WALL, "air"))
        # Walls - right wing
        lines.append(fill(RW_X1,yb+1,RW_Z1, RW_X2,yt,RW_Z2, "quartz_block"))
        lines.append(fill(RW_X1+WALL,yb+1,RW_Z1+WALL, RW_X2-WALL,yt,RW_Z2-WALL, "air"))
        # Connect wings to back (remove internal walls)
        lines.append(fill(LW_X1+WALL,yb+1,LW_Z2-WALL, LW_X2-WALL,yt,BACK_Z1+WALL, "air"))
        lines.append(fill(RW_X1+WALL,yb+1,RW_Z2-WALL, RW_X2-WALL,yt,BACK_Z1+WALL, "air"))
        # Gold trim at floor level
        lines.append(fill(BACK_X1,yb+1,BACK_Z1, BACK_X2,yb+1,BACK_Z1, "gold_block"))
        lines.append(fill(BACK_X1,yb+1,BACK_Z2, BACK_X2,yb+1,BACK_Z2, "gold_block"))
        lines.append(fill(LW_X1,yb+1,LW_Z1, LW_X2,yb+1,LW_Z1, "gold_block"))
        lines.append(fill(RW_X1,yb+1,RW_Z1, RW_X2,yb+1,RW_Z1, "gold_block"))
    # Roof
    lines.append(fill(BACK_X1,FLOORS*FH,LW_Z1, BACK_X2,FLOORS*FH,BACK_Z2, "quartz_block"))
    lines.append(fill(LW_X1,FLOORS*FH,LW_Z1, LW_X2,FLOORS*FH,BACK_Z1, "quartz_block"))
    lines.append(fill(RW_X1,FLOORS*FH,RW_Z1, RW_X2,FLOORS*FH,BACK_Z1, "quartz_block"))
    # Parapet
    h = FLOORS*FH+1
    lines.append(fill(BACK_X1,h,BACK_Z2, BACK_X2,h,BACK_Z2, "stone_bricks"))
    lines.append(fill(BACK_X1,h,LW_Z1, BACK_X2,h,LW_Z1, "stone_bricks"))
    lines.append(fill(LW_X1,h,LW_Z1, LW_X1,h,BACK_Z2, "stone_bricks"))
    lines.append(fill(BACK_X2,h,LW_Z1, BACK_X2,h,BACK_Z2, "stone_bricks"))
    # Grand portico (8 columns)
    lines.append(fill(52,0,42, 88,0,60, "quartz_block"))
    lines.append(fill(52,FLOORS*FH,42, 88,FLOORS*FH,60, "quartz_block"))
    for cx in [55,60,65,70,75,80,85]:
        lines.append(fill(cx,1,43, cx+1,FLOORS*FH-1,43, "quartz_block"))
        lines.append(sb(cx,FLOORS*FH-1,43, "gold_block"))
        lines.append(sb(cx+1,FLOORS*FH-1,43, "gold_block"))
    # Grand entrance
    lines.append(fill(64,1,BACK_Z1, 76,6,BACK_Z1, "air"))
    # Gold door frame
    lines.append(fill(63,1,BACK_Z1, 63,7,BACK_Z1, "gold_block"))
    lines.append(fill(77,1,BACK_Z1, 77,7,BACK_Z1, "gold_block"))
    lines.append(fill(64,7,BACK_Z1, 76,7,BACK_Z1, "gold_block"))
    lines.append("function bezos_windows")
    write_func("bezos_exterior", lines)

def gen_windows():
    lines = [comment("Phase 4: Georgian windows on all faces")]
    for floor in range(FLOORS):
        yb = floor * FH
        wy1 = yb + 2
        wy2 = yb + FH - 2
        # Left wing front (Z=25)
        for x in range(4, 32, 7):
            lines.append(fill(x,wy1,LW_Z1, x+3,wy2,LW_Z1, "glass"))
        # Right wing front (Z=25)
        for x in range(109, 137, 7):
            lines.append(fill(x,wy1,RW_Z1, x+3,wy2,RW_Z1, "glass"))
        # Back face (Z=100)
        for x in range(5, 135, 10):
            lines.append(fill(x,wy1,BACK_Z2, x+5,wy2,BACK_Z2, "glass"))
        # Left side (X=0)
        for z in range(30, 96, 10):
            lines.append(fill(LW_X1,wy1,z, LW_X1,wy2,z+5, "glass"))
        # Right side (X=140)
        for z in range(30, 96, 10):
            lines.append(fill(BACK_X2,wy1,z, BACK_X2,wy2,z+5, "glass"))
        # Inner U faces
        for z in range(30, 56, 10):
            lines.append(fill(LW_X2,wy1,z, LW_X2,wy2,z+5, "glass"))
            lines.append(fill(RW_X1,wy1,z, RW_X1,wy2,z+5, "glass"))
        # Center front face (Z=60)
        for x in range(40, 55, 10):
            lines.append(fill(x,wy1,BACK_Z1, x+5,wy2,BACK_Z1, "glass"))
        for x in range(85, 100, 10):
            lines.append(fill(x,wy1,BACK_Z1, x+5,wy2,BACK_Z1, "glass"))
    lines.append("function bezos_foyer")
    write_func("bezos_windows", lines)

def gen_foyer():
    lines = [comment("Phase 5: Grand foyer - triple height, dual staircases")]
    cx = 70  # center X
    # Divider walls
    lines.append(fill(52,1,62, 52,FH*2,98, "quartz_block"))
    lines.append(fill(88,1,62, 88,FH*2,98, "quartz_block"))
    lines.append(fill(53,1,62, 53,FH*2,62, "quartz_block"))
    lines.append(fill(87,1,62, 87,FH*2,62, "quartz_block"))
    # Remove floors for triple height
    lines.append(fill(53,FH,63, 87,FH,85, "air"))
    lines.append(fill(53,FH*2,63, 87,FH*2,85, "air"))
    # CUT STAIR HOLES in floors so stairs actually connect
    lines.append(fill(53,FH,86, 59,FH,98, "air"))
    lines.append(fill(81,FH,86, 87,FH,98, "air"))
    lines.append(fill(53,FH*2,86, 59,FH*2,98, "air"))
    lines.append(fill(81,FH*2,86, 87,FH*2,98, "air"))
    # Gold + lapis inlay floor
    lines.append(fill(54,0,63, 86,0,85, "quartz_block"))
    lines.append(fill(58,0,67, 82,0,81, "gold_block"))
    lines.append(fill(62,0,70, 78,0,78, "lapis_block"))
    lines.append(fill(66,0,72, 74,0,76, "diamond_block"))
    # Dual grand staircases (left)
    for i in range(8):
        lines.append(fill(54,i+1,80+i, 58,i+1,81+i, "quartz_block"))
        lines.append(fill(54,i+2,80+i, 58,FH*3-1,81+i, "air"))  # clear above
    # Dual grand staircases (right)
    for i in range(8):
        lines.append(fill(82,i+1,80+i, 86,i+1,81+i, "quartz_block"))
        lines.append(fill(82,i+2,80+i, 86,FH*3-1,81+i, "air"))  # clear above
    # Second flight to floor 3
    for i in range(8):
        lines.append(fill(54,9+i,88+i, 58,9+i,89+i, "quartz_block"))
        lines.append(fill(54,10+i,88+i, 58,FH*3-1,89+i, "air"))
    for i in range(8):
        lines.append(fill(82,9+i,88+i, 86,9+i,89+i, "quartz_block"))
        lines.append(fill(82,10+i,88+i, 86,FH*3-1,89+i, "air"))
    # Gold stair railings
    for i in range(8):
        lines.append(sb(54,i+2,80+i, "gold_block"))
        lines.append(sb(58,i+2,80+i, "gold_block"))
        lines.append(sb(82,i+2,80+i, "gold_block"))
        lines.append(sb(86,i+2,80+i, "gold_block"))
    # Mega chandelier
    for dx in range(-3,4):
        for dz in range(-3,4):
            if abs(dx)+abs(dz) <= 4:
                lines.append(sb(cx+dx, FH*3-2, 74+dz, "glowstone"))
    lines.append(sb(cx, FH*3-1, 74, "gold_block"))
    for dy in range(FH*3-3, FH*2, -1):
        lines.append(sb(cx, dy, 74, "chain"))
    # Gold-framed doorways to wings
    for dx in [52,88]:
        for z in [68,78]:
            lines.append(fill(dx,1,z, dx,4,z+3, "air"))
            lines.append(fill(dx,5,z, dx,5,z+3, "gold_block"))
    lines.append("function bezos_west_wing")
    write_func("bezos_foyer", lines)

def gen_west_wing():
    lines = [comment("Phase 6: West wing - Living, Library, Ballroom, Art Gallery, Music Room")]
    # FORMAL LIVING ROOM (X=2-33, Z=27-45)
    lines.append(comment("--- Formal Living Room ---"))
    lines.append(fill(2,0,27, 33,0,45, "dark_oak_planks"))
    # Wood paneling lower walls
    lines.append(fill(2,1,27, 2,3,45, "spruce_planks"))
    lines.append(fill(33,1,27, 33,3,45, "spruce_planks"))
    lines.append(fill(2,1,27, 33,3,27, "spruce_planks"))
    lines.append(fill(2,1,45, 33,3,45, "spruce_planks"))
    # Grand fireplace (against outer wall, grounded)
    lines.append(fill(2,1,34, 4,6,38, "stone_bricks"))
    lines.append(fill(3,1,35, 3,3,37, "air"))
    lines.append(sb(3,1,36, "netherrack"))
    lines.append(fill(2,5,34, 4,5,38, "gold_block"))  # gold mantel
    # Sofa set (facing fireplace)
    lines.append(fill(10,1,34, 10,1,38, "spruce_planks"))  # long sofa
    lines.append(fill(10,2,34, 10,2,34, "spruce_planks"))  # arm
    lines.append(fill(10,2,38, 10,2,38, "spruce_planks"))  # arm
    lines.append(fill(16,1,34, 16,1,38, "spruce_planks"))  # opposite sofa
    # Coffee table between sofas
    lines.append(fill(12,1,35, 14,1,37, "dark_oak_planks"))
    # Side table with lamp
    lines.append(sb(20,1,30, "dark_oak_planks"))
    lines.append(sb(20,2,30, "sea_lantern"))
    # Ceiling light (embedded in ceiling, not floating)
    lines.append(sb(17,FH-1,36, "glowstone"))

    # LIBRARY (X=2-33, Z=47-58)
    lines.append(comment("--- Library ---"))
    lines.append(fill(2,1,46, 33,FH,46, "quartz_block"))
    lines.append(fill(14,1,46, 18,4,46, "air"))  # doorway
    lines.append(fill(14,5,46, 18,5,46, "gold_block"))  # gold frame
    lines.append(fill(2,0,47, 33,0,58, "red_wool"))
    # Bookshelves
    lines.append(fill(2,1,47, 2,6,58, "bookshelf"))
    lines.append(fill(3,1,58, 33,6,58, "bookshelf"))
    lines.append(fill(33,1,47, 33,6,57, "bookshelf"))
    lines.append(fill(3,1,47, 20,3,47, "bookshelf"))
    # Reading desk + chair
    lines.append(fill(15,1,52, 19,1,54, "dark_oak_planks"))
    lines.append(sb(17,1,55, "spruce_planks"))  # chair
    # Reading lamp on desk
    lines.append(sb(15,2,52, "sea_lantern"))
    # Ceiling light
    lines.append(sb(17,FH-1,52, "glowstone"))

    # BALLROOM (X=2-50, Z=62-98)
    lines.append(comment("--- Grand Ballroom ---"))
    lines.append(fill(2,0,62, 50,0,98, "quartz_block"))
    lines.append(fill(8,0,68, 44,0,92, "gold_block"))  # gold dance floor
    lines.append(fill(12,0,72, 40,0,88, "quartz_block"))  # inner pattern
    # Emerald pillars (grounded on floor)
    for x in [6, 16, 26, 36, 46]:
        lines.append(fill(x,1,62, x,FH-1,62, "emerald_block"))
        lines.append(fill(x,1,98, x,FH-1,98, "emerald_block"))
    # Side seating benches (grounded)
    lines.append(fill(3,1,70, 3,1,78, "spruce_planks"))
    lines.append(fill(3,1,82, 3,1,90, "spruce_planks"))
    lines.append(fill(48,1,70, 48,1,78, "spruce_planks"))
    lines.append(fill(48,1,82, 48,1,90, "spruce_planks"))
    # Chandeliers (embedded in ceiling)
    for z in [72, 80, 88]:
        lines.append(sb(26,FH-1,z, "glowstone"))
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            lines.append(sb(26+d[0],FH-1,z+d[1], "glowstone"))

    # ART GALLERY (gold trim on back wall, grounded)
    lines.append(comment("--- Art Gallery ---"))
    lines.append(fill(2,1,98, 50,1,98, "gold_block"))

    # MUSIC ROOM (corner area)
    lines.append(comment("--- Music Room ---"))
    lines.append(fill(2,0,47, 10,0,55, "amethyst_block"))
    lines.append(sb(6,FH-1,51, "glowstone"))

    lines.append("function bezos_east_wing")
    write_func("bezos_west_wing", lines)

def gen_east_wing():
    lines = [comment("Phase 7: East wing - Dining, Screening, Bar, Billiard, Kitchen, Wine Cellar, Spa")]
    ex = 107  # east wing inner X

    # FORMAL DINING (X=90-138, Z=62-78)
    lines.append(comment("--- Formal Dining Room (seats 24) ---"))
    lines.append(fill(90,0,62, 138,0,78, "dark_oak_planks"))
    # Long dining table
    lines.append(fill(100,1,68, 128,1,72, "dark_oak_planks"))
    # Chairs along both sides (grounded on floor)
    for x in range(101, 128, 3):
        lines.append(sb(x,1,67, "spruce_planks"))
        lines.append(sb(x,1,73, "spruce_planks"))
    # Head chairs
    lines.append(sb(99,1,70, "spruce_planks"))
    lines.append(sb(129,1,70, "spruce_planks"))
    # Centerpiece (gold, on the table)
    lines.append(sb(114,2,70, "gold_block"))
    # Lapis + marble fireplace (built from floor)
    lines.append(fill(138,1,68, 138,6,72, "quartz_block"))
    lines.append(fill(138,1,69, 138,3,71, "air"))
    lines.append(sb(138,1,70, "netherrack"))
    lines.append(sb(138,5,68, "lapis_block"))
    lines.append(sb(138,5,72, "lapis_block"))
    # Chandeliers (embedded in ceiling)
    for x in [106, 122]:
        lines.append(sb(x,FH-1,70, "glowstone"))
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            lines.append(sb(x+d[0],FH-1,70+d[1], "glowstone"))

    # SCREENING ROOM (X=107-138, Z=27-45)
    lines.append(comment("--- Private Screening Room (20 seats) ---"))
    lines.append(fill(ex,0,27, 138,0,45, "black_wool"))
    lines.append(fill(ex,1,27, 138,FH,27, "black_concrete"))
    lines.append(fill(ex,1,45, 138,FH,45, "black_concrete"))
    lines.append(fill(138,1,28, 138,FH,44, "black_concrete"))
    lines.append(fill(109,2,45, 136,6,45, "white_concrete"))  # screen
    for row, z in enumerate([32, 36, 40]):
        h = row
        lines.append(fill(112,1,z, 134,1+h,z, "quartz_block"))
        lines.append(fill(112,2+h,z, 134,2+h,z, "spruce_planks"))

    # WINE CELLAR (underground, X=90-130, Z=80-98)
    lines.append(comment("--- Wine Cellar ---"))
    lines.append(fill(90,-5,80, 130,-1,98, "stone_bricks"))
    lines.append(fill(92,-4,82, 128,-2,96, "air"))
    lines.append(fill(92,-4,82, 92,-2,96, "barrel"))
    lines.append(fill(128,-4,82, 128,-2,96, "barrel"))
    lines.append(fill(93,-5,82, 127,-5,96, "prismarine"))
    # Stairs down
    for i in range(5):
        lines.append(fill(108,-(i+1),62+i*2, 112,-(i+1),63+i*2, "quartz_block"))

    # DOMED BAR (X=107-138, Z=47-58)
    lines.append(comment("--- Domed Bar ---"))
    lines.append(fill(ex,0,47, 138,0,58, "dark_oak_planks"))
    lines.append(fill(110,1,50, 110,2,56, "dark_oak_planks"))  # bar counter
    lines.append(fill(109,1,50, 109,5,56, "spruce_planks"))  # back shelves
    lines.append(fill(109,3,51, 109,3,55, "glowstone"))  # lit shelves
    lines.append(sb(120,FH-1,53, "glowstone"))
    lines.append(sb(120,FH,53, "gold_block"))

    # BILLIARD ROOM (X=90-105, Z=80-98)
    lines.append(comment("--- Billiard Room ---"))
    lines.append(fill(90,0,80, 105,0,98, "dark_oak_planks"))
    lines.append(fill(94,1,85, 101,1,93, "emerald_block"))  # billiard table
    lines.append(sb(97,FH-1,89, "glowstone"))

    # SPA (X=107-138, Z=80-98)
    lines.append(comment("--- Luxury Spa ---"))
    lines.append(fill(ex,0,80, 138,0,98, "quartz_block"))
    lines.append(fill(110,0,84, 120,0,90, "amethyst_block"))  # treatment area
    # Spa pool - contained basin (walls BEFORE water)
    lines.append(fill(124,-1,83, 136,1,91, "prismarine"))
    lines.append(fill(125,-1,84, 135,-1,90, "prismarine"))
    lines.append(fill(125,0,84, 135,0,90, "air"))
    lines.append(fill(126,-1,85, 134,-1,89, "water"))
    # Diamond treatment tables
    lines.append(fill(112,1,86, 114,1,88, "diamond_block"))
    lines.append(fill(117,1,86, 119,1,88, "diamond_block"))

    lines.append("function bezos_floor2")
    write_func("bezos_east_wing", lines)

def make_bedroom(lines, x1, z1, y_base, width=10, depth=8, carpet="white_wool", gold_headboard=True):
    """Generate one fully furnished luxury bedroom"""
    x2, z2 = x1+width, z1+depth
    lines.append(fill(x1,y_base,z1, x2,y_base+FH,z2, "quartz_block"))
    lines.append(fill(x1+1,y_base+1,z1+1, x2-1,y_base+FH-1,z2-1, "air"))
    lines.append(fill(x1+1,y_base,z1+1, x2-1,y_base,z2-1, carpet))
    # Bed (king size with gold headboard)
    bx = x1 + width//2 - 1
    lines.append(fill(bx,y_base+1,z2-3, bx+2,y_base+1,z2-2, "white_wool"))
    if gold_headboard:
        lines.append(fill(bx,y_base+1,z2-1, bx+2,y_base+2,z2-1, "gold_block"))
        lines.append(fill(bx,y_base+1,z2-2, bx+2,y_base+1,z2-2, "red_wool"))  # bedspread
    # Nightstands (both sides of bed)
    lines.append(sb(bx-1,y_base+1,z2-2, "dark_oak_planks"))
    lines.append(sb(bx+3,y_base+1,z2-2, "dark_oak_planks"))
    # Bedside lamps (on nightstands, not floating)
    lines.append(sb(bx-1,y_base+2,z2-2, "sea_lantern"))
    lines.append(sb(bx+3,y_base+2,z2-2, "sea_lantern"))
    # Dresser against side wall
    lines.append(fill(x2-2,y_base+1,z1+2, x2-2,y_base+1,z1+4, "dark_oak_planks"))
    # Armchair
    lines.append(sb(x1+2,y_base+1,z1+2, "spruce_planks"))
    # Rug
    lines.append(fill(bx-1,y_base,z2-4, bx+3,y_base,z2-3, carpet))
    # Window
    lines.append(fill(x1+3,y_base+2,z1, x1+width-3,y_base+FH-3,z1, "glass"))
    # Ceiling light (embedded in ceiling, not floating)
    lines.append(sb(x1+width//2, y_base+FH-1, z1+depth//2, "glowstone"))
    # Door opening with gold frame
    lines.append(fill(x1,y_base+1,z1+depth//2, x1,y_base+3,z1+depth//2+1, "air"))
    lines.append(fill(x1,y_base+4,z1+depth//2, x1,y_base+4,z1+depth//2+1, "gold_block"))

def gen_floor2():
    lines = [comment("Phase 8: Floor 2 - Master suite + 14 bedrooms")]
    yb = FH  # floor 2 base

    # MASTER SUITE (center, X=55-85, Z=62-98)
    lines.append(comment("--- Master Suite ---"))
    lines.append(fill(55,yb,75, 85,yb+FH,98, "quartz_block"))
    lines.append(fill(57,yb+1,77, 83,yb+FH-1,96, "air"))
    lines.append(fill(57,yb,77, 83,yb,96, "red_wool"))
    # King bed with gold
    lines.append(fill(66,yb+1,92, 74,yb+1,95, "white_wool"))
    lines.append(fill(66,yb+1,95, 74,yb+2,95, "gold_block"))
    lines.append(fill(66,yb+3,95, 74,yb+3,95, "diamond_block"))
    # Master fireplace
    lines.append(fill(69,yb+1,96, 71,yb+5,96, "cobblestone"))
    lines.append(sb(70,yb+1,96, "netherrack"))
    lines.append(fill(68,yb+4,96, 72,yb+4,96, "gold_block"))
    # His bathroom
    lines.append(fill(57,yb,77, 63,yb+FH,82, "quartz_block"))
    lines.append(fill(58,yb+1,78, 62,yb+FH-1,81, "air"))
    lines.append(fill(58,yb,78, 62,yb,81, "quartz_block"))
    lines.append(fill(59,yb+1,79, 61,yb+1,80, "diamond_block"))
    # Her bathroom
    lines.append(fill(77,yb,77, 83,yb+FH,82, "quartz_block"))
    lines.append(fill(78,yb+1,78, 82,yb+FH-1,81, "air"))
    lines.append(fill(78,yb,78, 82,yb,81, "quartz_block"))
    lines.append(fill(79,yb+1,79, 81,yb+1,80, "diamond_block"))
    # Chandelier
    lines.append(sb(70,yb+FH-1,86, "glowstone"))
    for d in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]:
        lines.append(sb(70+d[0],yb+FH-1,86+d[1], "glowstone"))
    lines.append(sb(70,yb+FH,86, "gold_block"))

    # 14 BEDROOMS along wings
    carpets = ["white_wool","red_wool","blue_wool","green_wool","yellow_wool",
               "pink_wool","cyan_wool","light_blue_wool","orange_wool","magenta_wool",
               "purple_wool","lime_wool","gray_wool","brown_wool"]
    room_idx = 0
    # Left wing bedrooms (7 rooms)
    for i in range(7):
        z = LW_Z1 + 2 + i * (8+1)
        if z + 8 > BACK_Z2 - 2: break
        make_bedroom(lines, 2, z, yb, 12, 8, carpets[room_idx % len(carpets)])
        room_idx += 1
    # Right wing bedrooms (7 rooms)
    for i in range(7):
        z = RW_Z1 + 2 + i * (8+1)
        if z + 8 > BACK_Z2 - 2: break
        make_bedroom(lines, RW_X1+2, z, yb, 12, 8, carpets[room_idx % len(carpets)])
        room_idx += 1

    lines.append("function bezos_floor3")
    write_func("bezos_floor2", lines)

def gen_floor3():
    lines = [comment("Phase 9: Floor 3 - 15 bedrooms + observatory")]
    yb = FH * 2
    carpets = ["cyan_wool","magenta_wool","lime_wool","pink_wool","light_blue_wool",
               "orange_wool","white_wool","red_wool","blue_wool","green_wool",
               "yellow_wool","purple_wool","gray_wool","brown_wool","black_wool"]
    room_idx = 0
    # Left wing (7 rooms)
    for i in range(7):
        z = LW_Z1 + 2 + i * 9
        if z + 8 > BACK_Z2 - 2: break
        make_bedroom(lines, 2, z, yb, 12, 8, carpets[room_idx % len(carpets)])
        room_idx += 1
    # Right wing (7 rooms)
    for i in range(7):
        z = RW_Z1 + 2 + i * 9
        if z + 8 > BACK_Z2 - 2: break
        make_bedroom(lines, RW_X1+2, z, yb, 12, 8, carpets[room_idx % len(carpets)])
        room_idx += 1
    # Center back bedroom
    make_bedroom(lines, 55, 85, yb, 12, 8, carpets[14])

    # OBSERVATORY (center front, X=55-85 on rooftop)
    lines.append(comment("--- Observatory ---"))
    ry = FLOORS * FH
    lines.append(fill(60,ry,65, 80,ry+5,80, "glass"))
    lines.append(fill(62,ry+1,67, 78,ry+4,78, "air"))
    lines.append(fill(62,ry,67, 78,ry,78, "quartz_block"))
    lines.append(fill(69,ry+1,72, 71,ry+3,72, "amethyst_block"))  # telescope
    lines.append(sb(70,ry+4,72, "glowstone"))

    lines.append("function bezos_pool")
    write_func("bezos_floor3", lines)

def gen_pool():
    lines = [comment("Phase 10: Deep infinity pool, hot tubs, pavilion")]
    # Pool deck
    lines.append(fill(25,0,105, 115,0,150, "quartz_block"))
    lines.append(fill(25,-1,105, 115,-1,150, "quartz_block"))
    # Deep pool - dig hole, line with prismarine tiles, fill with water
    # Step 1: Dig the pool basin
    lines.append(fill(35,-5,110, 105,0,140, "air"))
    # Step 2: Line bottom and sides with prismarine (pool tiles)
    lines.append(fill(35,-5,110, 105,-5,140, "prismarine"))  # floor
    lines.append(fill(34,-5,109, 106,-1,109, "prismarine"))  # south wall
    lines.append(fill(34,-5,141, 106,-1,141, "prismarine"))  # north wall
    lines.append(fill(34,-5,110, 34,-1,140, "prismarine"))   # west wall
    lines.append(fill(106,-5,110, 106,-1,140, "prismarine")) # east wall
    # Step 3: Gold edge at surface level (Y=0, one above water top at Y=-1)
    lines.append(fill(34,0,109, 106,0,109, "gold_block"))
    lines.append(fill(34,0,141, 106,0,141, "gold_block"))
    lines.append(fill(34,0,110, 34,0,140, "gold_block"))
    lines.append(fill(106,0,110, 106,0,140, "gold_block"))
    # Step 4: Underwater lighting
    for x in range(40, 105, 10):
        for z in range(115, 140, 10):
            lines.append(sb(x,-5,z, "sea_lantern"))
    # Step 5: Fill with water (surface at Y=-1, contained by gold at Y=0)
    lines.append(fill(35,-4,110, 105,-4,140, "water"))
    lines.append(fill(35,-3,110, 105,-3,140, "water"))
    lines.append(fill(35,-2,110, 105,-2,140, "water"))
    lines.append(fill(35,-1,110, 105,-1,140, "water"))
    # Hot tubs (2) - dig, line, fill
    for hx in [28, 110]:
        lines.append(fill(hx,-2,120, hx+5,0,126, "air"))  # dig
        lines.append(fill(hx,-2,120, hx+5,-2,126, "prismarine"))  # floor
        lines.append(fill(hx,-2,119, hx+5,0,119, "prismarine"))  # walls
        lines.append(fill(hx,-2,127, hx+5,0,127, "prismarine"))
        lines.append(fill(hx-1,-2,120, hx-1,0,126, "prismarine"))
        lines.append(fill(hx+6,-2,120, hx+6,0,126, "prismarine"))
        lines.append(sb(hx+2,-2,123, "sea_lantern"))
        lines.append(fill(hx,-1,120, hx+5,-1,126, "water"))
    # Pool pavilion (8 columns)
    lines.append(fill(40,0,143, 100,0,158, "quartz_block"))
    lines.append(fill(40,8,143, 100,8,158, "quartz_block"))
    for cx in [43,50,57,64,71,78,85,92]:
        lines.append(fill(cx,1,143, cx+1,7,143, "quartz_block"))
        lines.append(sb(cx,7,143, "gold_block"))
        lines.append(sb(cx+1,7,143, "gold_block"))
    lines.append(fill(45,1,143, 95,5,143, "air"))  # open front
    # Pavilion lounge furniture
    lines.append(fill(50,1,150, 50,2,156, "dark_oak_planks"))  # bar
    lines.append(fill(52,1,150, 52,1,156, "spruce_planks"))  # stools
    lines.append(fill(60,1,148, 80,1,148, "spruce_planks"))  # sofas
    lines.append(fill(60,1,155, 80,1,155, "spruce_planks"))
    lines.append(fill(62,1,150, 78,1,150, "dark_oak_planks"))  # coffee table
    lines.append(sb(70,7,150, "glowstone"))

    lines.append("function bezos_guesthouses")
    write_func("bezos_pool", lines)

def gen_guesthouses():
    lines = [comment("Phase 11: Two guest houses with 10 bedrooms each")]
    for side, bx in [("West", -40), ("East", 145)]:
        lines.append(comment(f"--- {side} Guest House (10 bedrooms) ---"))
        gw, gd = 35, 50
        x1, z1 = bx, 105
        x2, z2 = bx+gw, z1+gd
        # Foundation + floors
        lines.append(fill(x1,-1,z1, x2,-1,z2, "quartz_block"))
        for fl in range(2):
            yb = fl * FH
            lines.append(fill(x1,yb,z1, x2,yb,z2, "dark_oak_planks"))
            lines.append(fill(x1,yb+1,z1, x2,yb+FH,z2, "quartz_block"))
            lines.append(fill(x1+2,yb+1,z1+2, x2-2,yb+FH-1,z2-2, "air"))
            # Gold trim
            lines.append(fill(x1,yb+1,z1, x2,yb+1,z1, "gold_block"))
            lines.append(fill(x1,yb+1,z2, x2,yb+1,z2, "gold_block"))
            # Windows
            for z in range(z1+4, z2-4, 8):
                lines.append(fill(x1,yb+2,z, x1,yb+FH-2,z+4, "glass"))
                lines.append(fill(x2,yb+2,z, x2,yb+FH-2,z+4, "glass"))
            # 5 bedrooms per floor
            for i in range(5):
                bz = z1 + 3 + i * 9
                if bz + 8 > z2 - 2: break
                bx1 = x1 + 2
                bw = (gw - 4) // 2
                make_bedroom(lines, bx1, bz, yb, bw, 7,
                    ["white_wool","red_wool","blue_wool","cyan_wool","pink_wool"][i])
                make_bedroom(lines, bx1+bw+1, bz, yb, bw, 7,
                    ["orange_wool","lime_wool","yellow_wool","purple_wool","magenta_wool"][i])
        # Roof
        lines.append(fill(x1,FH*2,z1, x2,FH*2,z2, "quartz_block"))
        # Door
        lines.append(fill(x1+gw//2-2,1,z1, x1+gw//2+2,4,z1, "air"))
        lines.append(fill(x1+gw//2-2,5,z1, x1+gw//2+2,5,z1, "gold_block"))

    lines.append("function bezos_gardens")
    write_func("bezos_guesthouses", lines)

def gen_gardens():
    lines = [comment("Phase 12: Terraced gardens, fountains, greenhouses")]
    # 3-tier terraced garden
    for tier, (z1,z2,h) in enumerate([(100,105,0),(105,108,1),(108,111,2)]):
        lines.append(fill(20,h,z1, 120,h,z2, "stone_bricks"))
        lines.append(fill(22,h,z1+1, 118,h,z2-1, "grass_block"))
        for x in range(25, 115, 6):
            lines.append(sb(x,h+1,z1+1, "red_flower" if x%12<6 else "yellow_flower"))
    # Water cascade - contained channels
    lines.append(fill(67,1,100, 73,2,103, "stone_bricks"))  # channel walls
    lines.append(fill(68,1,101, 72,1,102, "water"))
    lines.append(fill(67,2,104, 73,3,108, "stone_bricks"))  # upper channel walls
    lines.append(fill(68,2,105, 72,2,107, "water"))
    # Stone bridge
    lines.append(fill(65,3,108, 75,3,110, "stone_bricks"))
    lines.append(fill(65,4,108, 65,4,110, "stone_bricks"))
    lines.append(fill(75,4,108, 75,4,110, "stone_bricks"))
    # Grand fountains (2) - basin walls first
    for fx in [35, 100]:
        lines.append(fill(fx,0,103, fx+8,1,107, "stone_bricks"))  # full basin
        lines.append(fill(fx+1,0,104, fx+7,0,106, "air"))  # hollow
        lines.append(fill(fx+1,-1,104, fx+7,-1,106, "stone_bricks"))  # floor
        lines.append(fill(fx+1,0,104, fx+7,0,106, "water"))  # water inside
        lines.append(fill(fx+3,2,105, fx+5,2,105, "prismarine"))
        lines.append(sb(fx+4,3,105, "sea_lantern"))
        lines.append(sb(fx+4,4,105, "gold_block"))
    # 3 Greenhouses
    for i, gz in enumerate([110,122,134]):
        lines.append(fill(150,0,gz, 170,0,gz+10, "stone_bricks"))
        lines.append(fill(150,1,gz, 170,5,gz+10, "glass"))
        lines.append(fill(151,1,gz+1, 169,4,gz+9, "air"))
        lines.append(fill(150,6,gz, 170,6,gz+10, "glass"))
        lines.append(sb(160,3,gz+5, "sea_lantern"))
        for x in range(153,168,3):
            lines.append(sb(x,1,gz+3, "grass_block"))
            lines.append(sb(x,2,gz+3, "red_flower"))
    # Rear trees
    for tx,tz in [(10,130),(30,135),(110,130),(130,135),(70,155),(50,160),(90,160)]:
        lines.append(fill(tx,1,tz, tx,7,tz, "oak_log"))
        lines.append(fill(tx-3,7,tz-3, tx+3,10,tz+3, "leaves"))
    lines.append("function bezos_sports")
    write_func("bezos_gardens", lines)

def gen_sports():
    lines = [comment("Phase 13: Tennis court, golf course, helipad")]
    # TENNIS COURT
    lines.append(fill(150,-1,30, 190,-1,65, "green_concrete"))
    lines.append(fill(150,0,30, 190,0,65, "green_concrete"))
    lines.append(fill(151,0,30, 189,0,30, "white_concrete"))
    lines.append(fill(151,0,65, 189,0,65, "white_concrete"))
    lines.append(fill(150,0,31, 150,0,64, "white_concrete"))
    lines.append(fill(190,0,31, 190,0,64, "white_concrete"))
    lines.append(fill(170,0,31, 170,0,64, "white_concrete"))
    lines.append(fill(170,1,31, 170,2,64, "cobblestone_wall"))
    # Viewing gallery
    lines.append(fill(148,0,40, 148,3,55, "quartz_block"))
    lines.append(fill(148,3,40, 148,3,55, "spruce_planks"))

    # HELIPAD
    lines.append(fill(160,0,80, 180,0,100, "gray_concrete"))
    lines.append(fill(165,0,85, 175,0,95, "white_concrete"))
    # H marking
    lines.append(fill(167,0,87, 168,0,93, "yellow_concrete"))
    lines.append(fill(172,0,87, 173,0,93, "yellow_concrete"))
    lines.append(fill(169,0,89, 171,0,91, "yellow_concrete"))
    # Lights
    for x in [161,179]:
        for z in [81,99]:
            lines.append(sb(x,1,z, "sea_lantern"))

    # 9-HOLE GOLF COURSE
    lines.append(fill(-40,-1,140, 30,-1,250, "grass_block"))
    greens = [(-30,150),(-10,170),(10,155),(-25,190),(5,195),(-15,215),
              (10,220),(-30,235),(0,245)]
    for i,(gx,gz) in enumerate(greens):
        lines.append(fill(gx,0,gz, gx+10,0,gz+8, "lime_concrete"))
        lines.append(sb(gx+5,1,gz+4, "white_wool"))  # flag
        lines.append(sb(gx+5,2,gz+4, "white_wool"))
        if i % 2 == 0:
            lines.append(fill(gx+12,0,gz+2, gx+15,0,gz+6, "sand"))
        if i % 3 == 0:
            # Golf pond - contained basin
            lines.append(fill(gx-6,-2,gz+2, gx-1,0,gz+7, "stone_bricks"))
            lines.append(fill(gx-5,-1,gz+3, gx-2,-1,gz+6, "water"))

    lines.append("function bezos_garage")
    write_func("bezos_sports", lines)

def gen_garage():
    lines = [comment("Phase 14: Underground garage + spaceship sauna")]
    # UNDERGROUND GARAGE (20 cars, below motor court)
    lines.append(fill(45,-6,30, 95,-1,55, "stone_bricks"))
    lines.append(fill(47,-5,32, 93,-2,53, "air"))
    lines.append(fill(47,-5,32, 93,-5,53, "polished_deepslate"))
    # Parking lines
    for x in range(50, 90, 5):
        lines.append(fill(x,-5,33, x,-5,40, "white_concrete"))
        lines.append(fill(x,-5,45, x,-5,52, "white_concrete"))
    # Ramp up
    for i in range(6):
        lines.append(fill(45,-(i+1),28-i*2, 55,-(i+1),29-i*2, "polished_deepslate"))
    # Garage lighting
    for x in range(52, 92, 8):
        lines.append(sb(x,-2,38, "sea_lantern"))
        lines.append(sb(x,-2,48, "sea_lantern"))

    # SPACESHIP SAUNA (Bezos's actual addition)
    lines.append(comment("--- Spaceship Sauna (cone-shaped) ---"))
    lines.append(fill(155,0,105, 165,0,115, "quartz_block"))
    # Cone shape (layers getting smaller)
    for y in range(8):
        r = 5 - y//2
        if r < 1: r = 1
        cx, cz = 160, 110
        lines.append(fill(cx-r,y+1,cz-r, cx+r,y+1,cz+r, "glass"))
        lines.append(fill(cx-r+1,y+1,cz-r+1, cx+r-1,y+1,cz+r-1, "air"))
    lines.append(sb(160,9,110, "gold_block"))  # gold tip
    # Interior
    lines.append(fill(158,1,108, 162,1,112, "spruce_planks"))
    lines.append(sb(160,1,110, "glowstone"))

    lines.append(comment("=== BEZOS WARNER ESTATE COMPLETE! ==="))
    write_func("bezos_garage", lines)

# ============================================================
# GENERATE ALL FILES
# ============================================================
if __name__ == "__main__":
    print("Generating Bezos Warner Estate Mega Mansion...")
    gen_master()
    gen_clear()
    gen_driveway()
    gen_exterior()
    gen_windows()
    gen_foyer()
    gen_west_wing()
    gen_east_wing()
    gen_floor2()
    gen_floor3()
    gen_pool()
    gen_guesthouses()
    gen_gardens()
    gen_sports()
    gen_garage()
    print("\nDone! All function files generated.")
