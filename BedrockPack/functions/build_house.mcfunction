# Modern 2-Story House - Bedrock Edition
# Bedrock uses same block names as Java for 1.20+
# Run this from flat ground, facing any direction

# Clear the area
fill ~-1 ~-1 ~-1 ~16 ~12 ~16 air

# Foundation
fill ~ ~-1 ~ ~15 ~-1 ~15 smooth_quartz

# Ground floor (dark oak)
fill ~ ~ ~ ~15 ~ ~15 dark_oak_planks

# Floor 1 outer walls
fill ~ ~1 ~ ~15 ~4 ~15 white_concrete
fill ~1 ~1 ~1 ~14 ~4 ~14 air

# Second floor base (quartz slab ceiling/floor)
fill ~ ~5 ~ ~15 ~5 ~15 quartz_block

# Floor 2 outer walls
fill ~ ~6 ~ ~15 ~9 ~15 white_concrete
fill ~1 ~6 ~1 ~14 ~9 ~14 air

# Flat roof
fill ~ ~10 ~ ~15 ~10 ~15 smooth_quartz

# Accent trim between floors
fill ~-1 ~5 ~-1 ~16 ~5 ~-1 smooth_quartz
fill ~-1 ~5 ~16 ~16 ~5 ~16 smooth_quartz
fill ~-1 ~5 ~ ~-1 ~5 ~15 smooth_quartz
fill ~16 ~5 ~ ~16 ~5 ~15 smooth_quartz

# Front door opening
fill ~7 ~1 ~ ~8 ~2 ~ air

# Front & back large windows floor 1
fill ~2 ~2 ~ ~5 ~4 ~ cyan_stained_glass_pane
fill ~10 ~2 ~ ~13 ~4 ~ cyan_stained_glass_pane
fill ~2 ~2 ~15 ~13 ~4 ~15 cyan_stained_glass_pane

# Front & back large windows floor 2
fill ~2 ~7 ~ ~13 ~9 ~ cyan_stained_glass_pane
fill ~2 ~7 ~15 ~13 ~9 ~15 cyan_stained_glass_pane

# Side windows floor 1
fill ~ ~2 ~2 ~ ~4 ~5 cyan_stained_glass_pane
fill ~15 ~2 ~2 ~15 ~4 ~5 cyan_stained_glass_pane
fill ~ ~2 ~10 ~ ~4 ~13 cyan_stained_glass_pane
fill ~15 ~2 ~10 ~15 ~4 ~13 cyan_stained_glass_pane

# Side windows floor 2
fill ~ ~7 ~2 ~ ~9 ~13 cyan_stained_glass_pane
fill ~15 ~7 ~2 ~15 ~9 ~13 cyan_stained_glass_pane

# Internal staircase (floor 1 to floor 2)
setblock ~13 ~1 ~13 quartz_stairs ["weirdo_direction"=3]
setblock ~13 ~2 ~12 quartz_stairs ["weirdo_direction"=3]
setblock ~13 ~3 ~11 quartz_stairs ["weirdo_direction"=3]
setblock ~13 ~4 ~10 quartz_stairs ["weirdo_direction"=3]
setblock ~13 ~5 ~9 quartz_stairs ["weirdo_direction"=3]

# Stairwell opening in floor 2 slab
fill ~12 ~5 ~9 ~14 ~5 ~13 air

# Sea lantern lighting (hidden in corners)
setblock ~2 ~4 ~2 sea_lantern
setblock ~13 ~4 ~2 sea_lantern
setblock ~2 ~4 ~13 sea_lantern
setblock ~13 ~4 ~13 sea_lantern
setblock ~2 ~9 ~2 sea_lantern
setblock ~13 ~9 ~2 sea_lantern
setblock ~2 ~9 ~13 sea_lantern
setblock ~13 ~9 ~13 sea_lantern
