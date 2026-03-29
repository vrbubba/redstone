# ============================================================
# BEZOS WARNER ESTATE - MEGA MANSION
# Inspired by the $165M Jack Warner Estate in Beverly Hills
# Georgian-style ~ 80x60 main house + grounds
# ============================================================

# --- PHASE 1: CLEAR THE ENTIRE COMPOUND (100x120 area) ---
fill ~-5 ~-1 ~-5 ~105 ~25 ~125 air

# --- PHASE 2: LANDSCAPE & GROUNDS ---
# Main manicured lawn (grass)
fill ~-5 ~-1 ~-5 ~105 ~-1 ~125 grass_block

# Grand driveway (stone brick path from entrance ~50 blocks long)
fill ~38 ~ ~-5 ~42 ~ ~15 polished_deepslate
fill ~38 ~-1 ~-5 ~42 ~-1 ~15 polished_deepslate

# Circular driveway/fountain area in front of house
fill ~30 ~ ~12 ~50 ~ ~18 polished_deepslate
fill ~36 ~1 ~14 ~44 ~1 ~16 quartz_block
fill ~38 ~2 ~15 ~42 ~2 ~15 prismarine
fill ~39 ~3 ~15 ~41 ~3 ~15 prismarine
fill ~40 ~4 ~15 ~40 ~4 ~15 sea_lantern

# ============================================================
# --- PHASE 3: MAIN MANSION (80 x 40, starting at ~0,0,~20) ---
# ============================================================

# Foundation
fill ~ ~-1 ~20 ~80 ~-1 ~60 quartz_block

# Ground floor
fill ~ ~ ~20 ~80 ~ ~60 dark_oak_planks

# --- GROUND FLOOR WALLS (Height 6) ---
fill ~ ~1 ~20 ~80 ~6 ~60 quartz_block
fill ~2 ~1 ~22 ~78 ~6 ~58 air

# --- SECOND FLOOR ---
fill ~ ~7 ~20 ~80 ~7 ~60 quartz_block
fill ~2 ~7 ~22 ~78 ~7 ~58 dark_oak_planks
fill ~ ~8 ~20 ~80 ~13 ~60 quartz_block
fill ~2 ~8 ~22 ~78 ~13 ~58 air

# --- ROOF (flat Georgian style with parapet) ---
fill ~ ~14 ~20 ~80 ~14 ~60 quartz_block
fill ~ ~15 ~20 ~80 ~15 ~20 quartz_block
fill ~ ~15 ~60 ~80 ~15 ~60 quartz_block
fill ~ ~15 ~20 ~ ~15 ~60 quartz_block
fill ~80 ~15 ~20 ~80 ~15 ~60 quartz_block

# ============================================================
# --- PHASE 4: GRAND ENTRANCE (Front - Georgian Columns) ---
# ============================================================

# Grand front entrance portico (extends out from main building)
fill ~32 ~ ~16 ~48 ~ ~20 quartz_block
fill ~32 ~14 ~16 ~48 ~14 ~20 quartz_block

# 8 Grand pillars (2 blocks wide, 14 high)
fill ~33 ~1 ~16 ~34 ~13 ~16 quartz_pillar
fill ~37 ~1 ~16 ~38 ~13 ~16 quartz_pillar
fill ~42 ~1 ~16 ~43 ~13 ~16 quartz_pillar
fill ~46 ~1 ~16 ~47 ~13 ~16 quartz_pillar

# Main double doors (grand 4-wide, 4-tall opening)
fill ~38 ~1 ~20 ~42 ~4 ~20 air

# Floor in portico
fill ~33 ~ ~17 ~47 ~ ~19 quartz_block

# ============================================================
# --- PHASE 5: WINDOWS (Tall Georgian windows) ---
# ============================================================

# --- FRONT FACE (Z=20) ---
# Ground floor windows (left wing)
fill ~5 ~2 ~20 ~8 ~5 ~20 glass
fill ~12 ~2 ~20 ~15 ~5 ~20 glass
fill ~19 ~2 ~20 ~22 ~5 ~20 glass
fill ~26 ~2 ~20 ~29 ~5 ~20 glass

# Ground floor windows (right wing)
fill ~51 ~2 ~20 ~54 ~5 ~20 glass
fill ~58 ~2 ~20 ~61 ~5 ~20 glass
fill ~65 ~2 ~20 ~68 ~5 ~20 glass
fill ~72 ~2 ~20 ~75 ~5 ~20 glass

# Second floor windows (full front)
fill ~5 ~9 ~20 ~8 ~12 ~20 glass
fill ~12 ~9 ~20 ~15 ~12 ~20 glass
fill ~19 ~9 ~20 ~22 ~12 ~20 glass
fill ~26 ~9 ~20 ~29 ~12 ~20 glass
fill ~36 ~9 ~20 ~39 ~12 ~20 glass
fill ~41 ~9 ~20 ~44 ~12 ~20 glass
fill ~51 ~9 ~20 ~54 ~12 ~20 glass
fill ~58 ~9 ~20 ~61 ~12 ~20 glass
fill ~65 ~9 ~20 ~68 ~12 ~20 glass
fill ~72 ~9 ~20 ~75 ~12 ~20 glass

# --- BACK FACE (Z=60) ---
fill ~5 ~2 ~60 ~12 ~5 ~60 glass
fill ~18 ~2 ~60 ~25 ~5 ~60 glass
fill ~55 ~2 ~60 ~62 ~5 ~60 glass
fill ~68 ~2 ~60 ~75 ~5 ~60 glass
fill ~5 ~9 ~60 ~12 ~12 ~60 glass
fill ~18 ~9 ~60 ~25 ~12 ~60 glass
fill ~35 ~9 ~60 ~45 ~12 ~60 glass
fill ~55 ~9 ~60 ~62 ~12 ~60 glass
fill ~68 ~9 ~60 ~75 ~12 ~60 glass

# --- SIDE FACES ---
# Left side (X=0)
fill ~ ~2 ~25 ~ ~5 ~28 glass
fill ~ ~2 ~35 ~ ~5 ~38 glass
fill ~ ~2 ~45 ~ ~5 ~48 glass
fill ~ ~2 ~53 ~ ~5 ~56 glass
fill ~ ~9 ~25 ~ ~12 ~28 glass
fill ~ ~9 ~35 ~ ~12 ~38 glass
fill ~ ~9 ~45 ~ ~12 ~48 glass
fill ~ ~9 ~53 ~ ~12 ~56 glass

# Right side (X=80)
fill ~80 ~2 ~25 ~80 ~5 ~28 glass
fill ~80 ~2 ~35 ~80 ~5 ~38 glass
fill ~80 ~2 ~45 ~80 ~5 ~48 glass
fill ~80 ~2 ~53 ~80 ~5 ~56 glass
fill ~80 ~9 ~25 ~80 ~12 ~28 glass
fill ~80 ~9 ~35 ~80 ~12 ~38 glass
fill ~80 ~9 ~45 ~80 ~12 ~48 glass
fill ~80 ~9 ~53 ~80 ~12 ~56 glass

# ============================================================
# --- PHASE 6: INTERIOR - GROUND FLOOR ---
# ============================================================

# Grand Foyer (double-height entrance hall)
fill ~35 ~7 ~22 ~45 ~7 ~32 air
fill ~35 ~1 ~22 ~35 ~13 ~32 quartz_block
fill ~45 ~1 ~22 ~45 ~13 ~32 quartz_block

# Foyer floor (patterned)
fill ~36 ~ ~22 ~44 ~ ~32 quartz_block
fill ~38 ~ ~24 ~42 ~ ~30 dark_oak_planks
fill ~39 ~ ~26 ~41 ~ ~28 gold_block

# Grand chandelier in foyer
setblock ~40 ~12 ~27 glowstone
setblock ~39 ~11 ~27 glowstone
setblock ~41 ~11 ~27 glowstone
setblock ~40 ~11 ~26 glowstone
setblock ~40 ~11 ~28 glowstone
setblock ~40 ~13 ~27 chain

# Grand staircase (left side going up)
fill ~36 ~1 ~30 ~38 ~1 ~32 quartz_block
fill ~36 ~2 ~32 ~38 ~2 ~34 quartz_block
fill ~36 ~3 ~34 ~38 ~3 ~36 quartz_block
fill ~36 ~4 ~36 ~38 ~4 ~38 quartz_block
fill ~36 ~5 ~38 ~38 ~5 ~40 quartz_block
fill ~36 ~6 ~40 ~38 ~6 ~42 quartz_block
fill ~36 ~7 ~42 ~44 ~7 ~42 dark_oak_planks

# Grand staircase (right side going up)
fill ~42 ~1 ~30 ~44 ~1 ~32 quartz_block
fill ~42 ~2 ~32 ~44 ~2 ~34 quartz_block
fill ~42 ~3 ~34 ~44 ~3 ~36 quartz_block
fill ~42 ~4 ~36 ~44 ~4 ~38 quartz_block
fill ~42 ~5 ~38 ~44 ~5 ~40 quartz_block
fill ~42 ~6 ~40 ~44 ~6 ~42 quartz_block

# --- LEFT WING: Living / Library ---
# Divider wall
fill ~33 ~1 ~22 ~33 ~6 ~58 quartz_block
fill ~33 ~2 ~26 ~33 ~4 ~30 air
fill ~33 ~2 ~40 ~33 ~4 ~44 air

# Living room (left front)
fill ~3 ~ ~22 ~32 ~ ~38 dark_oak_planks
# Fireplace
fill ~2 ~1 ~30 ~2 ~4 ~30 cobblestone
fill ~2 ~1 ~29 ~2 ~4 ~31 cobblestone
fill ~2 ~1 ~30 ~2 ~1 ~30 netherrack
# Light the fireplace (place fire on netherrack)

# Library (left back)
fill ~3 ~ ~40 ~32 ~ ~58 dark_oak_planks
# Bookshelves lining the walls
fill ~2 ~1 ~41 ~2 ~4 ~57 bookshelf
fill ~3 ~1 ~58 ~31 ~4 ~58 bookshelf
fill ~3 ~1 ~40 ~10 ~4 ~40 bookshelf

# --- RIGHT WING: Dining / Screening Room ---
# Divider wall
fill ~47 ~1 ~22 ~47 ~6 ~58 quartz_block
fill ~47 ~2 ~26 ~47 ~4 ~30 air
fill ~47 ~2 ~40 ~47 ~4 ~44 air

# Formal dining room (right front)
fill ~48 ~ ~22 ~78 ~ ~38 dark_oak_planks
# Long dining table
fill ~55 ~1 ~28 ~70 ~1 ~32 dark_oak_planks
# Chandelier above table
setblock ~62 ~5 ~30 glowstone
setblock ~61 ~5 ~30 glowstone
setblock ~63 ~5 ~30 glowstone
setblock ~62 ~5 ~29 glowstone
setblock ~62 ~5 ~31 glowstone
setblock ~62 ~6 ~30 chain

# Screening room (right back)
fill ~48 ~ ~40 ~78 ~ ~58 dark_oak_planks
fill ~48 ~1 ~58 ~78 ~4 ~58 black_concrete
# Seating
fill ~52 ~1 ~48 ~74 ~1 ~48 quartz_block
fill ~52 ~1 ~52 ~74 ~1 ~52 quartz_block

# ============================================================
# --- PHASE 7: INTERIOR - SECOND FLOOR (8 Bedrooms) ---
# ============================================================

# Central hallway
fill ~35 ~8 ~23 ~45 ~13 ~57 air
fill ~35 ~8 ~22 ~35 ~13 ~58 quartz_block
fill ~45 ~8 ~22 ~45 ~13 ~58 quartz_block
fill ~36 ~7 ~23 ~44 ~7 ~57 dark_oak_planks

# Left wing bedrooms (4 rooms)
fill ~17 ~8 ~22 ~17 ~13 ~58 quartz_block
# Room divider walls
fill ~2 ~8 ~30 ~33 ~13 ~30 quartz_block
fill ~2 ~8 ~40 ~33 ~13 ~40 quartz_block
fill ~2 ~8 ~50 ~33 ~13 ~50 quartz_block
# Doorways
fill ~17 ~8 ~25 ~17 ~10 ~27 air
fill ~17 ~8 ~34 ~17 ~10 ~36 air
fill ~17 ~8 ~44 ~17 ~10 ~46 air
fill ~17 ~8 ~54 ~17 ~10 ~56 air

# Right wing bedrooms (4 rooms)
fill ~63 ~8 ~22 ~63 ~13 ~58 quartz_block
fill ~48 ~8 ~30 ~78 ~13 ~30 quartz_block
fill ~48 ~8 ~40 ~78 ~13 ~40 quartz_block
fill ~48 ~8 ~50 ~78 ~13 ~50 quartz_block
# Doorways
fill ~63 ~8 ~25 ~63 ~10 ~27 air
fill ~63 ~8 ~34 ~63 ~10 ~36 air
fill ~63 ~8 ~44 ~63 ~10 ~46 air
fill ~63 ~8 ~54 ~63 ~10 ~56 air

# ============================================================
# --- PHASE 8: LIGHTING (Sea lanterns throughout) ---
# ============================================================

# Ground floor ceiling lights
fill ~10 ~6 ~30 ~10 ~6 ~30 sea_lantern
fill ~20 ~6 ~30 ~20 ~6 ~30 sea_lantern
fill ~10 ~6 ~50 ~10 ~6 ~50 sea_lantern
fill ~20 ~6 ~50 ~20 ~6 ~50 sea_lantern
fill ~60 ~6 ~30 ~60 ~6 ~30 sea_lantern
fill ~70 ~6 ~30 ~70 ~6 ~30 sea_lantern
fill ~60 ~6 ~50 ~60 ~6 ~50 sea_lantern
fill ~70 ~6 ~50 ~70 ~6 ~50 sea_lantern

# Second floor ceiling lights
fill ~10 ~13 ~25 ~10 ~13 ~25 sea_lantern
fill ~25 ~13 ~25 ~25 ~13 ~25 sea_lantern
fill ~10 ~13 ~45 ~10 ~13 ~45 sea_lantern
fill ~25 ~13 ~45 ~25 ~13 ~45 sea_lantern
fill ~55 ~13 ~25 ~55 ~13 ~25 sea_lantern
fill ~70 ~13 ~25 ~70 ~13 ~25 sea_lantern
fill ~55 ~13 ~45 ~55 ~13 ~45 sea_lantern
fill ~70 ~13 ~45 ~70 ~13 ~45 sea_lantern

# Hallway lights
fill ~40 ~13 ~30 ~40 ~13 ~30 sea_lantern
fill ~40 ~13 ~40 ~40 ~13 ~40 sea_lantern
fill ~40 ~13 ~50 ~40 ~13 ~50 sea_lantern

# Portico and entrance lights
setblock ~35 ~13 ~17 sea_lantern
setblock ~45 ~13 ~17 sea_lantern
setblock ~40 ~13 ~17 sea_lantern

# ============================================================
# --- PHASE 9: SWIMMING POOL (right side of estate) ---
# ============================================================

# Pool deck
fill ~85 ~-1 ~30 ~100 ~-1 ~55 quartz_block
fill ~85 ~ ~30 ~100 ~ ~55 quartz_block

# Pool basin (dug into ground)
fill ~87 ~-1 ~32 ~98 ~-1 ~53 light_blue_concrete
fill ~87 ~ ~32 ~98 ~ ~53 water

# Pool border trim
fill ~86 ~ ~31 ~99 ~ ~31 quartz_block
fill ~86 ~ ~54 ~99 ~ ~54 quartz_block
fill ~86 ~ ~32 ~86 ~ ~53 quartz_block
fill ~99 ~ ~32 ~99 ~ ~53 quartz_block

# Pool lounge chairs (quartz slabs)
setblock ~86 ~1 ~35 quartz_block
setblock ~86 ~1 ~40 quartz_block
setblock ~86 ~1 ~45 quartz_block
setblock ~86 ~1 ~50 quartz_block

# ============================================================
# --- PHASE 10: GUEST HOUSE 1 (left rear) ---
# ============================================================

# Foundation
fill ~-5 ~-1 ~75 ~15 ~-1 ~95 quartz_block
fill ~-5 ~ ~75 ~15 ~ ~95 dark_oak_planks

# Walls
fill ~-5 ~1 ~75 ~15 ~5 ~95 quartz_block
fill ~-3 ~1 ~77 ~13 ~5 ~93 air

# Roof
fill ~-5 ~6 ~75 ~15 ~6 ~95 quartz_block

# Door
fill ~5 ~1 ~75 ~6 ~3 ~75 air

# Windows
fill ~-5 ~2 ~80 ~-5 ~4 ~85 glass
fill ~-5 ~2 ~88 ~-5 ~4 ~92 glass
fill ~15 ~2 ~80 ~15 ~4 ~85 glass
fill ~15 ~2 ~88 ~15 ~4 ~92 glass
fill ~2 ~2 ~95 ~8 ~4 ~95 glass

# Interior lights
setblock ~5 ~5 ~82 sea_lantern
setblock ~5 ~5 ~90 sea_lantern

# ============================================================
# --- PHASE 11: GUEST HOUSE 2 (right rear) ---
# ============================================================

# Foundation
fill ~65 ~-1 ~75 ~85 ~-1 ~95 quartz_block
fill ~65 ~ ~75 ~85 ~ ~95 dark_oak_planks

# Walls
fill ~65 ~1 ~75 ~85 ~5 ~95 quartz_block
fill ~67 ~1 ~77 ~83 ~5 ~93 air

# Roof
fill ~65 ~6 ~75 ~85 ~6 ~95 quartz_block

# Door
fill ~74 ~1 ~75 ~76 ~3 ~75 air

# Windows
fill ~65 ~2 ~80 ~65 ~4 ~85 glass
fill ~65 ~2 ~88 ~65 ~4 ~92 glass
fill ~85 ~2 ~80 ~85 ~4 ~85 glass
fill ~85 ~2 ~88 ~85 ~4 ~92 glass
fill ~72 ~2 ~95 ~78 ~4 ~95 glass

# Interior lights
setblock ~75 ~5 ~82 sea_lantern
setblock ~75 ~5 ~90 sea_lantern

# ============================================================
# --- PHASE 12: GARDENS & LANDSCAPING ---
# ============================================================

# Hedge rows flanking driveway (leaves)
fill ~35 ~1 ~-3 ~37 ~3 ~10 leaves
fill ~43 ~1 ~-3 ~45 ~3 ~10 leaves

# Front garden flower beds (left)
fill ~5 ~1 ~16 ~28 ~1 ~18 grass_block
fill ~8 ~ ~17 ~8 ~ ~17 red_flower
fill ~12 ~ ~17 ~12 ~ ~17 yellow_flower
fill ~16 ~ ~17 ~16 ~ ~17 red_flower
fill ~20 ~ ~17 ~20 ~ ~17 yellow_flower
fill ~24 ~ ~17 ~24 ~ ~17 red_flower

# Front garden flower beds (right)
fill ~52 ~1 ~16 ~75 ~1 ~18 grass_block
fill ~55 ~ ~17 ~55 ~ ~17 yellow_flower
fill ~59 ~ ~17 ~59 ~ ~17 red_flower
fill ~63 ~ ~17 ~63 ~ ~17 yellow_flower
fill ~67 ~ ~17 ~67 ~ ~17 red_flower
fill ~71 ~ ~17 ~71 ~ ~17 yellow_flower

# Trees along the driveway
setblock ~36 ~1 ~0 oak_log
setblock ~36 ~2 ~0 oak_log
setblock ~36 ~3 ~0 oak_log
setblock ~36 ~4 ~0 oak_log
fill ~34 ~5 ~-2 ~38 ~7 ~2 leaves

setblock ~44 ~1 ~0 oak_log
setblock ~44 ~2 ~0 oak_log
setblock ~44 ~3 ~0 oak_log
setblock ~44 ~4 ~0 oak_log
fill ~42 ~5 ~-2 ~46 ~7 ~2 leaves

setblock ~36 ~1 ~6 oak_log
setblock ~36 ~2 ~6 oak_log
setblock ~36 ~3 ~6 oak_log
setblock ~36 ~4 ~6 oak_log
fill ~34 ~5 ~4 ~38 ~7 ~8 leaves

setblock ~44 ~1 ~6 oak_log
setblock ~44 ~2 ~6 oak_log
setblock ~44 ~3 ~6 oak_log
setblock ~44 ~4 ~6 oak_log
fill ~42 ~5 ~4 ~46 ~7 ~8 leaves

# Rear garden trees
setblock ~30 ~1 ~65 oak_log
setblock ~30 ~2 ~65 oak_log
setblock ~30 ~3 ~65 oak_log
setblock ~30 ~4 ~65 oak_log
setblock ~30 ~5 ~65 oak_log
fill ~28 ~5 ~63 ~32 ~8 ~67 leaves

setblock ~50 ~1 ~65 oak_log
setblock ~50 ~2 ~65 oak_log
setblock ~50 ~3 ~65 oak_log
setblock ~50 ~4 ~65 oak_log
setblock ~50 ~5 ~65 oak_log
fill ~48 ~5 ~63 ~52 ~8 ~67 leaves

# Rear garden path
fill ~38 ~ ~60 ~42 ~ ~75 polished_deepslate

# ============================================================
# --- PHASE 13: PERIMETER WALL & GATE ---
# ============================================================

# Front gate pillars
fill ~34 ~1 ~-5 ~36 ~5 ~-5 cobblestone
fill ~44 ~1 ~-5 ~46 ~5 ~-5 cobblestone
setblock ~35 ~6 ~-5 sea_lantern
setblock ~45 ~6 ~-5 sea_lantern

# Perimeter hedge (front, left, right)
fill ~-5 ~1 ~-5 ~33 ~3 ~-5 leaves
fill ~47 ~1 ~-5 ~105 ~3 ~-5 leaves
fill ~-5 ~1 ~-5 ~-5 ~3 ~125 leaves
fill ~105 ~1 ~-5 ~105 ~3 ~125 leaves
fill ~-5 ~1 ~125 ~105 ~3 ~125 leaves

# ============================================================
# --- PHASE 14: TENNIS COURT (left side) ---
# ============================================================

fill ~-5 ~-1 ~100 ~25 ~-1 ~120 green_concrete
fill ~-5 ~ ~100 ~25 ~ ~120 green_concrete
# Court lines
fill ~-4 ~ ~100 ~24 ~ ~100 white_concrete
fill ~-4 ~ ~120 ~24 ~ ~120 white_concrete
fill ~-4 ~ ~100 ~-4 ~ ~120 white_concrete
fill ~24 ~ ~100 ~24 ~ ~120 white_concrete
fill ~10 ~ ~100 ~10 ~ ~120 white_concrete
# Net
fill ~10 ~1 ~101 ~10 ~1 ~119 cobblestone_wall

# ============================================================
# --- DONE! Welcome to the Bezos Estate! ---
# ============================================================
