# ============================================================
# BEZOS WARNER ESTATE - PHASE 1: CLEAR, LANDSCAPE, EXTERIOR
# ============================================================

# Clear the entire compound (160x160 area)
fill ~-10 ~-2 ~-10 ~160 ~25 ~160 air

# Base landscape (grass)
fill ~-10 ~-1 ~-10 ~160 ~-1 ~160 grass_block

# ============================================================
# DRIVEWAY & MOTOR COURT
# ============================================================
fill ~42 ~ ~-5 ~48 ~ ~25 polished_deepslate
fill ~42 ~-1 ~-5 ~48 ~-1 ~25 polished_deepslate

# Circular motor court
fill ~30 ~ ~22 ~60 ~ ~34 polished_deepslate
fill ~30 ~-1 ~22 ~60 ~-1 ~34 polished_deepslate

# Central fountain
fill ~41 ~1 ~26 ~49 ~1 ~30 quartz_block
fill ~43 ~2 ~27 ~47 ~2 ~29 prismarine
fill ~44 ~3 ~28 ~46 ~3 ~28 prismarine
fill ~45 ~4 ~28 ~45 ~4 ~28 sea_lantern

# Driveway trees (6 sycamores flanking)
fill ~39 ~1 ~0 ~39 ~5 ~0 oak_log
fill ~37 ~5 ~-2 ~41 ~8 ~2 leaves
fill ~51 ~1 ~0 ~51 ~5 ~0 oak_log
fill ~49 ~5 ~-2 ~53 ~8 ~2 leaves
fill ~39 ~1 ~8 ~39 ~5 ~8 oak_log
fill ~37 ~5 ~6 ~41 ~8 ~10 leaves
fill ~51 ~1 ~8 ~51 ~5 ~8 oak_log
fill ~49 ~5 ~6 ~53 ~8 ~10 leaves
fill ~39 ~1 ~16 ~39 ~5 ~16 oak_log
fill ~37 ~5 ~14 ~41 ~8 ~18 leaves
fill ~51 ~1 ~16 ~51 ~5 ~16 oak_log
fill ~49 ~5 ~14 ~53 ~8 ~18 leaves

# ============================================================
# MAIN MANSION - U-SHAPE EXTERIOR
# Back section: X=0-90, Z=50-75
# Left wing:   X=0-25, Z=25-50
# Right wing:  X=65-90, Z=25-50
# ============================================================

# Foundation
fill ~ ~-1 ~25 ~90 ~-1 ~75 quartz_block
fill ~ ~-1 ~50 ~90 ~-1 ~75 quartz_block

# Ground floor (dark oak throughout)
fill ~ ~ ~25 ~90 ~ ~75 dark_oak_planks

# --- BACK SECTION walls (ground floor, 6 high) ---
fill ~ ~1 ~50 ~90 ~6 ~75 quartz_block
fill ~2 ~1 ~52 ~88 ~6 ~73 air

# --- LEFT WING walls ---
fill ~ ~1 ~25 ~25 ~6 ~50 quartz_block
fill ~2 ~1 ~27 ~23 ~6 ~49 air

# --- RIGHT WING walls ---
fill ~65 ~1 ~25 ~90 ~6 ~50 quartz_block
fill ~67 ~1 ~27 ~88 ~6 ~49 air

# Connect wings to back section (remove internal dividers)
fill ~2 ~1 ~49 ~23 ~6 ~52 air
fill ~67 ~1 ~49 ~88 ~6 ~52 air

# --- SECOND FLOOR ---
fill ~ ~7 ~25 ~90 ~7 ~75 quartz_block
fill ~2 ~7 ~27 ~88 ~7 ~73 dark_oak_planks
fill ~2 ~7 ~27 ~23 ~7 ~49 dark_oak_planks
fill ~67 ~7 ~27 ~88 ~7 ~49 dark_oak_planks

# Second floor walls
fill ~ ~8 ~50 ~90 ~13 ~75 quartz_block
fill ~2 ~8 ~52 ~88 ~13 ~73 air
fill ~ ~8 ~25 ~25 ~13 ~50 quartz_block
fill ~2 ~8 ~27 ~23 ~13 ~49 air
fill ~65 ~8 ~25 ~90 ~13 ~50 quartz_block
fill ~67 ~8 ~27 ~88 ~13 ~49 air
fill ~2 ~8 ~49 ~23 ~13 ~52 air
fill ~67 ~8 ~49 ~88 ~13 ~52 air

# --- ROOF (flat Georgian with parapet) ---
fill ~ ~14 ~25 ~90 ~14 ~75 quartz_block
fill ~ ~14 ~50 ~90 ~14 ~75 quartz_block
# Top parapet walls
fill ~ ~15 ~25 ~25 ~15 ~25 stone_bricks
fill ~ ~15 ~75 ~90 ~15 ~75 stone_bricks
fill ~ ~15 ~25 ~ ~15 ~75 stone_bricks
fill ~90 ~15 ~25 ~90 ~15 ~75 stone_bricks
fill ~25 ~15 ~50 ~25 ~15 ~50 stone_bricks
fill ~65 ~15 ~50 ~65 ~15 ~50 stone_bricks
fill ~25 ~15 ~25 ~65 ~15 ~25 stone_bricks

# ============================================================
# GRAND PORTICO (6 Doric Columns)
# Center of back section front face, projecting south
# ============================================================
fill ~33 ~ ~44 ~57 ~ ~50 quartz_block
fill ~33 ~14 ~44 ~57 ~14 ~50 quartz_block
fill ~33 ~15 ~44 ~57 ~15 ~44 stone_bricks

# 6 Grand columns (each 2 blocks wide)
fill ~35 ~1 ~45 ~36 ~13 ~45 quartz_block
fill ~39 ~1 ~45 ~40 ~13 ~45 quartz_block
fill ~43 ~1 ~45 ~44 ~13 ~45 quartz_block
fill ~46 ~1 ~45 ~47 ~13 ~45 quartz_block
fill ~50 ~1 ~45 ~51 ~13 ~45 quartz_block
fill ~54 ~1 ~45 ~55 ~13 ~45 quartz_block

# Grand entrance door (5 wide, 5 tall)
fill ~42 ~1 ~50 ~48 ~5 ~50 air

# ============================================================
# WINDOWS - GEORGIAN STYLE (all faces)
# ============================================================

# --- LEFT WING FRONT (Z=25) ---
fill ~4 ~2 ~25 ~7 ~5 ~25 glass
fill ~11 ~2 ~25 ~14 ~5 ~25 glass
fill ~18 ~2 ~25 ~21 ~5 ~25 glass
fill ~4 ~9 ~25 ~7 ~12 ~25 glass
fill ~11 ~9 ~25 ~14 ~12 ~25 glass
fill ~18 ~9 ~25 ~21 ~12 ~25 glass

# --- RIGHT WING FRONT (Z=25) ---
fill ~69 ~2 ~25 ~72 ~5 ~25 glass
fill ~76 ~2 ~25 ~79 ~5 ~25 glass
fill ~83 ~2 ~25 ~86 ~5 ~25 glass
fill ~69 ~9 ~25 ~72 ~12 ~25 glass
fill ~76 ~9 ~25 ~79 ~12 ~25 glass
fill ~83 ~9 ~25 ~86 ~12 ~25 glass

# --- BACK FACE (Z=75) ---
fill ~5 ~2 ~75 ~10 ~5 ~75 glass
fill ~18 ~2 ~75 ~23 ~5 ~75 glass
fill ~32 ~2 ~75 ~37 ~5 ~75 glass
fill ~53 ~2 ~75 ~58 ~5 ~75 glass
fill ~67 ~2 ~75 ~72 ~5 ~75 glass
fill ~80 ~2 ~75 ~85 ~5 ~75 glass
fill ~5 ~9 ~75 ~10 ~12 ~75 glass
fill ~18 ~9 ~75 ~23 ~12 ~75 glass
fill ~32 ~9 ~75 ~37 ~12 ~75 glass
fill ~42 ~9 ~75 ~48 ~12 ~75 glass
fill ~53 ~9 ~75 ~58 ~12 ~75 glass
fill ~67 ~9 ~75 ~72 ~12 ~75 glass
fill ~80 ~9 ~75 ~85 ~12 ~75 glass

# --- LEFT SIDES (X=0) ---
fill ~ ~2 ~30 ~ ~5 ~34 glass
fill ~ ~2 ~40 ~ ~5 ~44 glass
fill ~ ~2 ~55 ~ ~5 ~60 glass
fill ~ ~2 ~65 ~ ~5 ~70 glass
fill ~ ~9 ~30 ~ ~12 ~34 glass
fill ~ ~9 ~40 ~ ~12 ~44 glass
fill ~ ~9 ~55 ~ ~12 ~60 glass
fill ~ ~9 ~65 ~ ~12 ~70 glass

# --- RIGHT SIDES (X=90) ---
fill ~90 ~2 ~30 ~90 ~5 ~34 glass
fill ~90 ~2 ~40 ~90 ~5 ~44 glass
fill ~90 ~2 ~55 ~90 ~5 ~60 glass
fill ~90 ~2 ~65 ~90 ~5 ~70 glass
fill ~90 ~9 ~30 ~90 ~12 ~34 glass
fill ~90 ~9 ~40 ~90 ~12 ~44 glass
fill ~90 ~9 ~55 ~90 ~12 ~60 glass
fill ~90 ~9 ~65 ~90 ~12 ~70 glass

# --- INNER U-FACE windows (facing courtyard) ---
# Left wing east face (X=25, Z=25-50)
fill ~25 ~2 ~30 ~25 ~5 ~34 glass
fill ~25 ~2 ~40 ~25 ~5 ~44 glass
fill ~25 ~9 ~30 ~25 ~12 ~34 glass
fill ~25 ~9 ~40 ~25 ~12 ~44 glass

# Right wing west face (X=65, Z=25-50)
fill ~65 ~2 ~30 ~65 ~5 ~34 glass
fill ~65 ~2 ~40 ~65 ~5 ~44 glass
fill ~65 ~9 ~30 ~65 ~12 ~34 glass
fill ~65 ~9 ~40 ~65 ~12 ~44 glass

# Back section front face (Z=50, between wings)
fill ~28 ~2 ~50 ~33 ~5 ~50 glass
fill ~57 ~2 ~50 ~62 ~5 ~50 glass
fill ~28 ~9 ~50 ~33 ~12 ~50 glass
fill ~42 ~9 ~50 ~48 ~12 ~50 glass
fill ~57 ~9 ~50 ~62 ~12 ~50 glass

# Chain to phase 2
function build_bezos_interior
