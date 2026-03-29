# Modern 2-Story House - Bedrock Edition (Simplified, no block states)

# Clear the area
fill ~-1 ~-1 ~-1 ~16 ~12 ~16 air

# Foundation
fill ~ ~-1 ~ ~15 ~-1 ~15 quartz_block

# Ground floor (dark oak)
fill ~ ~ ~ ~15 ~ ~15 dark_oak_planks

# Floor 1 outer walls (white concrete)
fill ~ ~1 ~ ~15 ~4 ~15 white_concrete
fill ~1 ~1 ~1 ~14 ~4 ~14 air

# Second floor base
fill ~ ~5 ~ ~15 ~5 ~15 quartz_block

# Floor 2 outer walls
fill ~ ~6 ~ ~15 ~9 ~15 white_concrete
fill ~1 ~6 ~1 ~14 ~9 ~14 air

# Flat roof
fill ~ ~10 ~ ~15 ~10 ~15 quartz_block

# Accent trim between floors (all 4 sides)
fill ~-1 ~5 ~-1 ~16 ~5 ~-1 quartz_block
fill ~-1 ~5 ~16 ~16 ~5 ~16 quartz_block
fill ~-1 ~5 ~ ~-1 ~5 ~15 quartz_block
fill ~16 ~5 ~ ~16 ~5 ~15 quartz_block

# Front door opening
fill ~7 ~1 ~ ~8 ~2 ~ air

# Front large windows floor 1
fill ~2 ~2 ~ ~5 ~4 ~ glass
fill ~10 ~2 ~ ~13 ~4 ~ glass

# Back large windows floor 1
fill ~2 ~2 ~15 ~13 ~4 ~15 glass

# Front large windows floor 2
fill ~2 ~7 ~ ~13 ~9 ~ glass

# Back large windows floor 2
fill ~2 ~7 ~15 ~13 ~9 ~15 glass

# Side windows floor 1
fill ~ ~2 ~2 ~ ~4 ~5 glass
fill ~15 ~2 ~2 ~15 ~4 ~5 glass
fill ~ ~2 ~10 ~ ~4 ~13 glass
fill ~15 ~2 ~10 ~15 ~4 ~13 glass

# Side windows floor 2
fill ~ ~7 ~2 ~ ~9 ~13 glass
fill ~15 ~7 ~2 ~15 ~9 ~13 glass

# Internal staircase (simple quartz block steps)
setblock ~13 ~1 ~13 quartz_block
setblock ~13 ~2 ~12 quartz_block
setblock ~13 ~3 ~11 quartz_block
setblock ~13 ~4 ~10 quartz_block
setblock ~13 ~5 ~9 quartz_block

# Stairwell opening in floor 2
fill ~12 ~5 ~9 ~14 ~5 ~13 air

# Sea lantern lighting
setblock ~2 ~4 ~2 sea_lantern
setblock ~13 ~4 ~2 sea_lantern
setblock ~2 ~4 ~13 sea_lantern
setblock ~13 ~4 ~13 sea_lantern
setblock ~2 ~9 ~2 sea_lantern
setblock ~13 ~9 ~2 sea_lantern
setblock ~2 ~9 ~13 sea_lantern
setblock ~13 ~9 ~13 sea_lantern
