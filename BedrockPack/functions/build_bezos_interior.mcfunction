# ============================================================
# BEZOS WARNER ESTATE - PHASE 2: INTERIOR ROOMS
# ============================================================

# ============================================================
# GRAND ENTRANCE HALL (double-height, center of back section)
# X=35-55, Z=52-65 - with dual curved staircases
# ============================================================

# Divider walls isolating foyer from side rooms
fill ~34 ~1 ~52 ~34 ~13 ~73 quartz_block
fill ~56 ~1 ~52 ~56 ~13 ~73 quartz_block
# Doorways from foyer to side rooms
fill ~34 ~2 ~56 ~34 ~4 ~58 air
fill ~56 ~2 ~56 ~56 ~4 ~58 air

# Double-height ceiling (remove floor between stories in foyer)
fill ~35 ~7 ~52 ~55 ~7 ~64 air

# Patterned foyer floor
fill ~36 ~ ~52 ~54 ~ ~64 quartz_block
fill ~38 ~ ~54 ~52 ~ ~62 dark_oak_planks
fill ~41 ~ ~56 ~49 ~ ~60 gold_block
fill ~44 ~ ~57 ~46 ~ ~59 quartz_block

# Grand dual staircase (left side curving up)
fill ~36 ~1 ~62 ~38 ~1 ~64 quartz_block
fill ~36 ~2 ~60 ~38 ~2 ~61 quartz_block
fill ~36 ~3 ~58 ~38 ~3 ~59 quartz_block
fill ~36 ~4 ~56 ~38 ~4 ~57 quartz_block
fill ~36 ~5 ~54 ~38 ~5 ~55 quartz_block
fill ~36 ~6 ~52 ~38 ~6 ~53 quartz_block
fill ~36 ~7 ~52 ~38 ~7 ~53 dark_oak_planks

# Grand dual staircase (right side curving up)
fill ~52 ~1 ~62 ~54 ~1 ~64 quartz_block
fill ~52 ~2 ~60 ~54 ~2 ~61 quartz_block
fill ~52 ~3 ~58 ~54 ~3 ~59 quartz_block
fill ~52 ~4 ~56 ~54 ~4 ~57 quartz_block
fill ~52 ~5 ~54 ~54 ~5 ~55 quartz_block
fill ~52 ~6 ~52 ~54 ~6 ~53 quartz_block
fill ~52 ~7 ~52 ~54 ~7 ~53 dark_oak_planks

# Grand chandelier (cut-glass inspired)
setblock ~45 ~12 ~58 glowstone
setblock ~44 ~11 ~58 glowstone
setblock ~46 ~11 ~58 glowstone
setblock ~45 ~11 ~57 glowstone
setblock ~45 ~11 ~59 glowstone
setblock ~43 ~10 ~58 glowstone
setblock ~47 ~10 ~58 glowstone
setblock ~45 ~10 ~56 glowstone
setblock ~45 ~10 ~60 glowstone
setblock ~45 ~13 ~58 chain

# Staircase railing (iron bars)
fill ~36 ~2 ~63 ~36 ~7 ~63 iron_bars
fill ~38 ~2 ~63 ~38 ~7 ~63 iron_bars
fill ~52 ~2 ~63 ~52 ~7 ~63 iron_bars
fill ~54 ~2 ~63 ~54 ~7 ~63 iron_bars

# ============================================================
# FORMAL LIVING ROOM (Left wing front, X=2-23, Z=27-43)
# 18th-century English paneling, Chinese wallpaper, fireplace
# ============================================================

# Interior walls (spruce for wood paneling)
fill ~2 ~1 ~27 ~23 ~3 ~27 spruce_planks
fill ~2 ~1 ~43 ~23 ~3 ~43 spruce_planks
fill ~2 ~1 ~27 ~2 ~3 ~43 spruce_planks
fill ~23 ~1 ~27 ~23 ~3 ~43 spruce_planks
# Upper walls (lighter)
fill ~2 ~4 ~27 ~23 ~5 ~27 quartz_block
fill ~2 ~4 ~43 ~23 ~5 ~43 quartz_block
fill ~2 ~4 ~27 ~2 ~5 ~43 quartz_block
fill ~23 ~4 ~27 ~23 ~5 ~43 quartz_block

# Grand fireplace (west wall center)
fill ~2 ~1 ~34 ~2 ~5 ~36 cobblestone
fill ~2 ~1 ~33 ~2 ~5 ~37 stone_bricks
fill ~3 ~1 ~34 ~3 ~1 ~36 cobblestone
setblock ~3 ~1 ~35 netherrack
# Mantelpiece
fill ~2 ~4 ~33 ~3 ~4 ~37 dark_oak_planks

# Seating arrangement
fill ~8 ~1 ~32 ~12 ~1 ~32 spruce_planks
fill ~8 ~1 ~38 ~12 ~1 ~38 spruce_planks
fill ~16 ~1 ~34 ~16 ~1 ~36 spruce_planks

# Doorway from living room to library
fill ~12 ~1 ~43 ~14 ~3 ~43 air

# ============================================================
# LIBRARY (Left wing back area, X=2-23, Z=45-48 + back section left X=2-32, Z=52-73)
# Floor-to-ceiling bookshelves, reading area
# ============================================================

# Library spans the left section of back block
# Interior divider between library and hallway
fill ~2 ~1 ~66 ~32 ~6 ~66 spruce_planks
fill ~14 ~1 ~66 ~18 ~3 ~66 air

# Bookshelves along all walls
fill ~2 ~1 ~52 ~2 ~5 ~65 bookshelf
fill ~2 ~1 ~67 ~2 ~5 ~73 bookshelf
fill ~3 ~1 ~73 ~32 ~5 ~73 bookshelf
fill ~3 ~1 ~52 ~32 ~2 ~52 bookshelf

# Reading area center
fill ~12 ~1 ~58 ~22 ~1 ~58 dark_oak_planks
fill ~12 ~1 ~62 ~22 ~1 ~62 dark_oak_planks

# Library carpet
fill ~4 ~ ~54 ~30 ~ ~71 red_wool

# ============================================================
# FORMAL DINING ROOM (Above foyer area, X=35-55, Z=67-73)
# French wallpaper, marble mantelpiece, long table
# ============================================================

# Divider wall
fill ~35 ~1 ~66 ~55 ~6 ~66 quartz_block
fill ~42 ~1 ~66 ~48 ~3 ~66 air

# Long dining table (seats 14+)
fill ~38 ~1 ~68 ~52 ~1 ~68 dark_oak_planks
fill ~38 ~1 ~72 ~52 ~1 ~72 dark_oak_planks
fill ~39 ~1 ~69 ~51 ~1 ~71 dark_oak_planks

# Dining chandelier
setblock ~45 ~5 ~70 glowstone
setblock ~44 ~5 ~70 glowstone
setblock ~46 ~5 ~70 glowstone
setblock ~45 ~5 ~69 glowstone
setblock ~45 ~5 ~71 glowstone
setblock ~45 ~6 ~70 chain

# Marble fireplace (back wall)
fill ~43 ~1 ~73 ~47 ~4 ~73 quartz_block
fill ~44 ~1 ~73 ~46 ~2 ~73 air
setblock ~44 ~1 ~73 netherrack

# Lapis accents on mantelpiece
setblock ~43 ~3 ~73 lapis_block
setblock ~47 ~3 ~73 lapis_block

# ============================================================
# SCREENING ROOM (Right back section, X=58-88, Z=52-65)
# Plush theater with rows of seating
# ============================================================

# Interior dividers
fill ~57 ~1 ~66 ~88 ~6 ~66 dark_oak_planks
fill ~70 ~1 ~66 ~74 ~3 ~66 air

# Dark walls for theater atmosphere
fill ~58 ~1 ~52 ~88 ~5 ~52 black_concrete
fill ~58 ~1 ~65 ~88 ~5 ~65 black_concrete
fill ~88 ~1 ~52 ~88 ~5 ~65 black_concrete

# Screen (white wall)
fill ~60 ~2 ~65 ~86 ~5 ~65 white_concrete

# Theater seating (3 rows)
fill ~62 ~1 ~55 ~84 ~1 ~55 spruce_planks
fill ~62 ~1 ~58 ~84 ~1 ~58 spruce_planks
fill ~62 ~1 ~61 ~84 ~1 ~61 spruce_planks

# Raised seating (back rows higher)
fill ~62 ~1 ~58 ~84 ~1 ~58 quartz_block
fill ~62 ~2 ~58 ~84 ~2 ~58 spruce_planks
fill ~62 ~1 ~61 ~84 ~2 ~61 quartz_block
fill ~62 ~3 ~61 ~84 ~3 ~61 spruce_planks

# Dark carpet
fill ~59 ~ ~53 ~87 ~ ~64 black_wool

# ============================================================
# DOMED BAR (Right back section, X=58-88, Z=67-73)
# Semi-circular bar, antique chandelier
# ============================================================

# Bar counter (L-shaped, dark oak)
fill ~60 ~1 ~68 ~60 ~1 ~72 dark_oak_planks
fill ~60 ~1 ~68 ~68 ~1 ~68 dark_oak_planks
fill ~60 ~2 ~68 ~60 ~2 ~72 dark_oak_planks
fill ~60 ~2 ~68 ~68 ~2 ~68 dark_oak_planks

# Shelves behind bar
fill ~59 ~1 ~68 ~59 ~4 ~72 spruce_planks
fill ~59 ~3 ~69 ~59 ~3 ~71 glowstone

# Bar seating
fill ~62 ~1 ~70 ~62 ~1 ~72 spruce_planks
fill ~65 ~1 ~70 ~65 ~1 ~72 spruce_planks
fill ~68 ~1 ~70 ~68 ~1 ~72 spruce_planks

# Antique chandelier
setblock ~70 ~5 ~70 glowstone
setblock ~69 ~5 ~70 glowstone
setblock ~71 ~5 ~70 glowstone
setblock ~70 ~6 ~70 chain

# ============================================================
# CARD ROOM (Right wing front, X=67-88, Z=27-38)
# Gaming tables, intimate scale, green felt
# ============================================================

fill ~68 ~ ~28 ~87 ~ ~37 green_wool
# Gaming tables
fill ~72 ~1 ~31 ~76 ~1 ~34 dark_oak_planks
fill ~80 ~1 ~31 ~84 ~1 ~34 dark_oak_planks

# ============================================================
# OVAL SITTING ROOM (Right wing back, X=67-88, Z=40-48)
# Venetian mirror, neoclassical chandelier, fireplace
# ============================================================

# Interior wall divider
fill ~67 ~1 ~39 ~88 ~6 ~39 quartz_block
fill ~75 ~1 ~39 ~79 ~3 ~39 air

fill ~68 ~ ~40 ~87 ~ ~48 red_wool

# Fireplace
fill ~88 ~1 ~43 ~88 ~4 ~45 cobblestone
fill ~88 ~1 ~42 ~88 ~4 ~46 stone_bricks
fill ~87 ~1 ~43 ~87 ~1 ~45 cobblestone
setblock ~87 ~1 ~44 netherrack
fill ~88 ~3 ~42 ~87 ~3 ~46 dark_oak_planks

# Seating
fill ~73 ~1 ~43 ~73 ~1 ~45 spruce_planks
fill ~78 ~1 ~42 ~82 ~1 ~42 spruce_planks
fill ~78 ~1 ~46 ~82 ~1 ~46 spruce_planks

# Chain to phase 3
function build_bezos_upper
