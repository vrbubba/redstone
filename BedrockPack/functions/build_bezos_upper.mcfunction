# ============================================================
# BEZOS WARNER ESTATE - PHASE 3: UPPER FLOOR & GROUNDS
# ============================================================

# ============================================================
# SECOND FLOOR - MASTER SUITE & 7 BEDROOMS
# ============================================================

# Central hallway (runs east-west through back section)
fill ~35 ~8 ~60 ~55 ~13 ~72 air
fill ~34 ~8 ~60 ~34 ~13 ~72 quartz_block
fill ~56 ~8 ~60 ~56 ~13 ~72 quartz_block

# --- MASTER SUITE (center back, X=36-54, Z=67-73) ---
fill ~36 ~8 ~66 ~54 ~13 ~66 quartz_block
fill ~42 ~8 ~66 ~48 ~10 ~66 air
# Master bed
fill ~42 ~8 ~71 ~48 ~8 ~73 white_wool
fill ~42 ~8 ~73 ~48 ~9 ~73 dark_oak_planks
# Master fireplace
fill ~44 ~8 ~73 ~46 ~11 ~73 cobblestone
setblock ~45 ~8 ~73 netherrack
# Master sitting area
fill ~37 ~8 ~68 ~39 ~8 ~68 spruce_planks
fill ~37 ~8 ~71 ~39 ~8 ~71 spruce_planks
# Master bath (his/hers)
fill ~36 ~8 ~67 ~40 ~13 ~67 quartz_block
fill ~37 ~8 ~67 ~38 ~10 ~67 air
fill ~50 ~8 ~67 ~54 ~13 ~67 quartz_block
fill ~51 ~8 ~67 ~52 ~10 ~67 air

# --- LEFT WING BEDROOMS (4 rooms) ---
# Divider walls
fill ~2 ~8 ~34 ~23 ~13 ~34 quartz_block
fill ~2 ~8 ~42 ~23 ~13 ~42 quartz_block
fill ~12 ~8 ~27 ~12 ~13 ~49 quartz_block
# Doorways
fill ~12 ~8 ~29 ~12 ~10 ~31 air
fill ~12 ~8 ~37 ~12 ~10 ~39 air
fill ~12 ~8 ~45 ~12 ~10 ~47 air
fill ~5 ~8 ~34 ~7 ~10 ~34 air
fill ~5 ~8 ~42 ~7 ~10 ~42 air
fill ~16 ~8 ~34 ~18 ~10 ~34 air
fill ~16 ~8 ~42 ~18 ~10 ~42 air
# Beds in each room
fill ~4 ~8 ~29 ~6 ~8 ~31 white_wool
fill ~4 ~8 ~37 ~6 ~8 ~39 white_wool
fill ~16 ~8 ~29 ~18 ~8 ~31 white_wool
fill ~16 ~8 ~37 ~18 ~8 ~39 white_wool

# --- LEFT WING BEDROOMS continued (in back section) ---
fill ~2 ~8 ~56 ~32 ~13 ~56 quartz_block
fill ~14 ~8 ~52 ~14 ~13 ~65 quartz_block
fill ~14 ~8 ~54 ~14 ~10 ~55 air
fill ~14 ~8 ~58 ~14 ~10 ~60 air
fill ~6 ~8 ~56 ~8 ~10 ~56 air
fill ~20 ~8 ~56 ~22 ~10 ~56 air
fill ~4 ~8 ~53 ~8 ~8 ~55 white_wool
fill ~4 ~8 ~58 ~8 ~8 ~60 white_wool
fill ~18 ~8 ~53 ~22 ~8 ~55 white_wool

# --- RIGHT WING BEDROOMS (3 rooms) ---
fill ~67 ~8 ~34 ~88 ~13 ~34 quartz_block
fill ~67 ~8 ~42 ~88 ~13 ~42 quartz_block
fill ~78 ~8 ~27 ~78 ~13 ~49 quartz_block
fill ~78 ~8 ~29 ~78 ~10 ~31 air
fill ~78 ~8 ~37 ~78 ~10 ~39 air
fill ~78 ~8 ~45 ~78 ~10 ~47 air
fill ~70 ~8 ~34 ~72 ~10 ~34 air
fill ~70 ~8 ~42 ~72 ~10 ~42 air
fill ~82 ~8 ~34 ~84 ~10 ~34 air
fill ~82 ~8 ~42 ~84 ~10 ~42 air
fill ~70 ~8 ~29 ~72 ~8 ~31 white_wool
fill ~70 ~8 ~37 ~72 ~8 ~39 white_wool
fill ~82 ~8 ~29 ~84 ~8 ~31 white_wool
fill ~82 ~8 ~37 ~84 ~8 ~39 white_wool
fill ~70 ~8 ~45 ~72 ~8 ~47 white_wool
fill ~82 ~8 ~45 ~84 ~8 ~47 white_wool

# ============================================================
# LIGHTING (Sea lanterns in ceilings throughout)
# ============================================================

# Ground floor
setblock ~12 ~6 ~35 sea_lantern
setblock ~12 ~6 ~60 sea_lantern
setblock ~24 ~6 ~60 sea_lantern
setblock ~12 ~6 ~70 sea_lantern
setblock ~24 ~6 ~70 sea_lantern
setblock ~45 ~6 ~70 sea_lantern
setblock ~73 ~6 ~57 sea_lantern
setblock ~83 ~6 ~57 sea_lantern
setblock ~73 ~6 ~70 sea_lantern
setblock ~75 ~6 ~33 sea_lantern
setblock ~83 ~6 ~33 sea_lantern
setblock ~75 ~6 ~44 sea_lantern

# Second floor
setblock ~6 ~13 ~30 sea_lantern
setblock ~18 ~13 ~30 sea_lantern
setblock ~6 ~13 ~38 sea_lantern
setblock ~18 ~13 ~38 sea_lantern
setblock ~6 ~13 ~46 sea_lantern
setblock ~45 ~13 ~64 sea_lantern
setblock ~45 ~13 ~70 sea_lantern
setblock ~73 ~13 ~30 sea_lantern
setblock ~83 ~13 ~30 sea_lantern
setblock ~73 ~13 ~38 sea_lantern
setblock ~83 ~13 ~38 sea_lantern
setblock ~73 ~13 ~46 sea_lantern

# Portico lighting
setblock ~40 ~13 ~47 sea_lantern
setblock ~45 ~13 ~47 sea_lantern
setblock ~50 ~13 ~47 sea_lantern

# ============================================================
# SWIMMING POOL WITH NEOCLASSICAL PAVILION
# Behind the mansion (Z=80-115)
# ============================================================

# Pool deck
fill ~20 ~-1 ~80 ~70 ~-1 ~105 quartz_block
fill ~20 ~ ~80 ~70 ~ ~105 quartz_block

# Long rectangular pool
fill ~28 ~-1 ~82 ~62 ~-1 ~100 light_blue_concrete
fill ~28 ~ ~82 ~62 ~ ~100 water

# Pool border
fill ~27 ~ ~81 ~63 ~ ~81 quartz_block
fill ~27 ~ ~101 ~63 ~ ~101 quartz_block
fill ~27 ~ ~82 ~27 ~ ~100 quartz_block
fill ~63 ~ ~82 ~63 ~ ~100 quartz_block

# Pool lounge area
setblock ~25 ~1 ~85 quartz_block
setblock ~25 ~1 ~90 quartz_block
setblock ~25 ~1 ~95 quartz_block
setblock ~65 ~1 ~85 quartz_block
setblock ~65 ~1 ~90 quartz_block
setblock ~65 ~1 ~95 quartz_block

# Neoclassical pool pavilion (behind pool)
fill ~30 ~ ~103 ~60 ~ ~115 quartz_block
fill ~30 ~1 ~103 ~60 ~6 ~115 quartz_block
fill ~32 ~1 ~105 ~58 ~6 ~113 air
fill ~30 ~7 ~103 ~60 ~7 ~115 quartz_block

# Pavilion columns (4 across front)
fill ~33 ~1 ~103 ~34 ~6 ~103 quartz_block
fill ~40 ~1 ~103 ~41 ~6 ~103 quartz_block
fill ~49 ~1 ~103 ~50 ~6 ~103 quartz_block
fill ~56 ~1 ~103 ~57 ~6 ~103 quartz_block

# Pavilion entrance
fill ~36 ~1 ~103 ~54 ~4 ~103 air

# Pavilion interior (lounge)
fill ~34 ~1 ~108 ~56 ~1 ~108 spruce_planks
fill ~34 ~1 ~112 ~56 ~1 ~112 spruce_planks
setblock ~45 ~6 ~108 sea_lantern

# ============================================================
# TENNIS COURT
# ============================================================

fill ~100 ~-1 ~30 ~135 ~-1 ~60 green_concrete
fill ~100 ~ ~30 ~135 ~ ~60 green_concrete
# Court lines
fill ~101 ~ ~30 ~134 ~ ~30 white_concrete
fill ~101 ~ ~60 ~134 ~ ~60 white_concrete
fill ~100 ~ ~31 ~100 ~ ~59 white_concrete
fill ~135 ~ ~31 ~135 ~ ~59 white_concrete
fill ~117 ~ ~31 ~118 ~ ~59 white_concrete
# Service lines
fill ~108 ~ ~31 ~108 ~ ~59 white_concrete
fill ~127 ~ ~31 ~127 ~ ~59 white_concrete
# Net
fill ~117 ~1 ~31 ~118 ~2 ~59 cobblestone_wall

# ============================================================
# GUEST HOUSE 1 (southwest)
# ============================================================
fill ~-5 ~-1 ~85 ~18 ~-1 ~105 quartz_block
fill ~-5 ~ ~85 ~18 ~ ~105 dark_oak_planks
fill ~-5 ~1 ~85 ~18 ~5 ~105 quartz_block
fill ~-3 ~1 ~87 ~16 ~5 ~103 air
fill ~-5 ~6 ~85 ~18 ~6 ~105 quartz_block
fill ~5 ~1 ~85 ~8 ~3 ~85 air
fill ~-5 ~2 ~90 ~-5 ~4 ~95 glass
fill ~-5 ~2 ~98 ~-5 ~4 ~102 glass
fill ~18 ~2 ~90 ~18 ~4 ~95 glass
fill ~18 ~2 ~98 ~18 ~4 ~102 glass
fill ~4 ~2 ~105 ~12 ~4 ~105 glass
# Interior
fill ~2 ~1 ~90 ~6 ~1 ~92 white_wool
setblock ~6 ~5 ~90 sea_lantern
setblock ~6 ~5 ~100 sea_lantern

# ============================================================
# GUEST HOUSE 2 "MARILYN MONROE'S" (southeast)
# ============================================================
fill ~75 ~-1 ~85 ~98 ~-1 ~105 quartz_block
fill ~75 ~ ~85 ~98 ~ ~105 dark_oak_planks
fill ~75 ~1 ~85 ~98 ~5 ~105 quartz_block
fill ~77 ~1 ~87 ~96 ~5 ~103 air
fill ~75 ~6 ~85 ~98 ~6 ~105 quartz_block
fill ~84 ~1 ~85 ~88 ~3 ~85 air
fill ~75 ~2 ~90 ~75 ~4 ~95 glass
fill ~75 ~2 ~98 ~75 ~4 ~102 glass
fill ~98 ~2 ~90 ~98 ~4 ~95 glass
fill ~98 ~2 ~98 ~98 ~4 ~102 glass
fill ~80 ~2 ~105 ~92 ~4 ~105 glass
fill ~80 ~1 ~90 ~84 ~1 ~92 white_wool
setblock ~86 ~5 ~90 sea_lantern
setblock ~86 ~5 ~100 sea_lantern

# ============================================================
# 3 GREENHOUSES (glass structures, northeast)
# ============================================================
fill ~105 ~ ~72 ~118 ~ ~80 stone_bricks
fill ~105 ~1 ~72 ~118 ~4 ~80 glass
fill ~106 ~1 ~73 ~117 ~3 ~79 air
fill ~105 ~5 ~72 ~118 ~5 ~80 glass
setblock ~111 ~3 ~76 sea_lantern

fill ~105 ~ ~83 ~118 ~ ~91 stone_bricks
fill ~105 ~1 ~83 ~118 ~4 ~91 glass
fill ~106 ~1 ~84 ~117 ~3 ~90 air
fill ~105 ~5 ~83 ~118 ~5 ~91 glass
setblock ~111 ~3 ~87 sea_lantern

fill ~105 ~ ~94 ~118 ~ ~102 stone_bricks
fill ~105 ~1 ~94 ~118 ~4 ~102 glass
fill ~106 ~1 ~95 ~117 ~3 ~101 air
fill ~105 ~5 ~94 ~118 ~5 ~102 glass
setblock ~111 ~3 ~98 sea_lantern

# ============================================================
# TERRACED GARDENS, FOUNTAINS, STONE BRIDGES
# ============================================================

# Terraced garden (between mansion and pool)
fill ~5 ~ ~76 ~20 ~1 ~79 stone_bricks
fill ~6 ~ ~77 ~19 ~ ~78 grass_block
fill ~8 ~1 ~77 ~8 ~1 ~77 red_flower
fill ~12 ~1 ~77 ~12 ~1 ~77 yellow_flower
fill ~16 ~1 ~77 ~16 ~1 ~77 red_flower

fill ~70 ~ ~76 ~90 ~1 ~79 stone_bricks
fill ~71 ~ ~77 ~89 ~ ~78 grass_block
fill ~74 ~1 ~77 ~74 ~1 ~77 yellow_flower
fill ~78 ~1 ~77 ~78 ~1 ~77 red_flower
fill ~82 ~1 ~77 ~82 ~1 ~77 yellow_flower
fill ~86 ~1 ~77 ~86 ~1 ~77 red_flower

# Garden path (stone brick path from mansion to pool)
fill ~43 ~ ~75 ~47 ~ ~82 stone_bricks

# Decorative garden fountain (between wings and to the sides)
fill ~10 ~1 ~80 ~14 ~1 ~84 stone_bricks
fill ~11 ~ ~81 ~13 ~ ~83 water
setblock ~12 ~2 ~82 sea_lantern

fill ~76 ~1 ~80 ~80 ~1 ~84 stone_bricks
fill ~77 ~ ~81 ~79 ~ ~83 water
setblock ~78 ~2 ~82 sea_lantern

# Stone bridge over decorative water feature
fill ~36 ~ ~77 ~54 ~ ~77 stone_bricks
fill ~38 ~-1 ~77 ~52 ~-1 ~77 water
fill ~36 ~1 ~77 ~36 ~1 ~77 stone_bricks
fill ~54 ~1 ~77 ~54 ~1 ~77 stone_bricks

# Rear trees
fill ~10 ~1 ~110 ~10 ~6 ~110 oak_log
fill ~8 ~6 ~108 ~12 ~9 ~112 leaves
fill ~80 ~1 ~110 ~80 ~6 ~110 oak_log
fill ~78 ~6 ~108 ~82 ~9 ~112 leaves
fill ~45 ~1 ~118 ~45 ~7 ~118 oak_log
fill ~43 ~7 ~116 ~47 ~10 ~120 leaves

# ============================================================
# SIMPLIFIED 3-HOLE GOLF COURSE (far east)
# ============================================================

# Fairway
fill ~105 ~-1 ~110 ~155 ~-1 ~155 grass_block

# Green 1
fill ~110 ~ ~115 ~120 ~ ~125 lime_concrete
setblock ~115 ~1 ~120 white_wool

# Sand bunker 1
fill ~122 ~ ~118 ~125 ~ ~122 sand

# Pond
fill ~130 ~-1 ~120 ~138 ~-1 ~128 light_blue_concrete
fill ~130 ~ ~120 ~138 ~ ~128 water

# Green 2
fill ~140 ~ ~130 ~150 ~ ~140 lime_concrete
setblock ~145 ~1 ~135 white_wool

# Sand bunker 2
fill ~137 ~ ~133 ~139 ~ ~137 sand

# Green 3
fill ~115 ~ ~140 ~125 ~ ~150 lime_concrete
setblock ~120 ~1 ~145 white_wool

# Sand bunker 3
fill ~127 ~ ~143 ~130 ~ ~147 sand

# ============================================================
# PERIMETER HEDGES AND GATE
# ============================================================

# Front gate pillars
fill ~39 ~1 ~-8 ~41 ~6 ~-8 stone_bricks
fill ~49 ~1 ~-8 ~51 ~6 ~-8 stone_bricks
setblock ~40 ~7 ~-8 sea_lantern
setblock ~50 ~7 ~-8 sea_lantern

# Iron gate between pillars
fill ~42 ~1 ~-8 ~48 ~4 ~-8 iron_bars

# Perimeter hedges
fill ~-10 ~1 ~-10 ~38 ~4 ~-10 leaves
fill ~52 ~1 ~-10 ~160 ~4 ~-10 leaves
fill ~-10 ~1 ~-10 ~-10 ~4 ~160 leaves
fill ~160 ~1 ~-10 ~160 ~4 ~160 leaves
fill ~-10 ~1 ~160 ~160 ~4 ~160 leaves

# Front flower beds
fill ~10 ~1 ~20 ~30 ~1 ~22 grass_block
fill ~14 ~2 ~21 ~14 ~2 ~21 red_flower
fill ~18 ~2 ~21 ~18 ~2 ~21 yellow_flower
fill ~22 ~2 ~21 ~22 ~2 ~21 red_flower
fill ~26 ~2 ~21 ~26 ~2 ~21 yellow_flower

fill ~60 ~1 ~20 ~80 ~1 ~22 grass_block
fill ~64 ~2 ~21 ~64 ~2 ~21 yellow_flower
fill ~68 ~2 ~21 ~68 ~2 ~21 red_flower
fill ~72 ~2 ~21 ~72 ~2 ~21 yellow_flower
fill ~76 ~2 ~21 ~76 ~2 ~21 red_flower

# ============================================================
# DONE! Welcome to the Bezos Warner Estate!
# ============================================================
