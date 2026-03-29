# Modern 2-Story House (15x15)

# Clear the area (15 width X, 11 height Y, 15 length Z)
fill ~-1 ~-1 ~-1 ~16 ~12 ~16 air

# Foundation
fill ~ ~-1 ~ ~15 ~-1 ~15 smooth_quartz

# Floor 1 Ground Floor (Dark Oak)
fill ~ ~ ~ ~15 ~ ~15 dark_oak_planks

# Floor 1 Outer Walls (White Concrete)
fill ~ ~1 ~ ~15 ~4 ~15 white_concrete

# Floor 1 Hollow Interior
fill ~1 ~1 ~1 ~14 ~4 ~14 air

# Floor 2 Slab Base (Ceiling of Floor 1 / Floor 2 Ground)
fill ~ ~5 ~ ~15 ~5 ~15 quartz_slab[type=top]

# Floor 2 Walls
fill ~ ~6 ~ ~15 ~9 ~15 white_concrete

# Floor 2 Hollow Interior
fill ~1 ~6 ~1 ~14 ~9 ~14 air

# Roof Ceiling (Flat Modern Roof)
fill ~ ~10 ~ ~15 ~10 ~15 smooth_quartz

# Exterior Wrap Around Accents (Line separating floor 1 and 2)
fill ~-1 ~5 ~-1 ~16 ~5 ~-1 smooth_quartz
fill ~-1 ~5 ~16 ~16 ~5 ~16 smooth_quartz
fill ~-1 ~5 ~ ~-1 ~5 ~15 smooth_quartz
fill ~16 ~5 ~ ~16 ~5 ~15 smooth_quartz

# Front Door (Oak/Dark Oak styling)
fill ~7 ~1 ~ ~8 ~2 ~ air
setblock ~7 ~1 ~ dark_oak_door[half=lower,facing=north]
setblock ~7 ~2 ~ dark_oak_door[half=upper,facing=north]
setblock ~8 ~1 ~ dark_oak_door[half=lower,facing=north,hinge=right]
setblock ~8 ~2 ~ dark_oak_door[half=upper,facing=north,hinge=right]

# Huge Modern Windows - Front and Back
fill ~2 ~2 ~ ~5 ~4 ~ cyan_stained_glass_pane
fill ~10 ~2 ~ ~13 ~4 ~ cyan_stained_glass_pane

fill ~2 ~2 ~15 ~13 ~4 ~15 cyan_stained_glass_pane
fill ~2 ~7 ~15 ~13 ~9 ~15 cyan_stained_glass_pane

fill ~2 ~7 ~ ~13 ~9 ~ cyan_stained_glass_pane

# Side Windows
fill ~ ~2 ~2 ~ ~4 ~5 cyan_stained_glass_pane
fill ~ ~2 ~10 ~ ~4 ~13 cyan_stained_glass_pane

fill ~15 ~2 ~2 ~15 ~4 ~5 cyan_stained_glass_pane
fill ~15 ~2 ~10 ~15 ~4 ~13 cyan_stained_glass_pane

fill ~ ~7 ~2 ~ ~9 ~13 cyan_stained_glass_pane
fill ~15 ~7 ~2 ~15 ~9 ~13 cyan_stained_glass_pane

# Internal Staircase (X=13, Z=13 to Z=9)
fill ~13 ~5 ~11 ~14 ~5 ~9 air
setblock ~13 ~1 ~13 quartz_stairs[facing=north]
setblock ~13 ~2 ~12 quartz_stairs[facing=north]
setblock ~13 ~3 ~11 quartz_stairs[facing=north]
setblock ~13 ~4 ~10 quartz_stairs[facing=north]
setblock ~13 ~5 ~9 quartz_stairs[facing=north]

# Internal Lighting (Hide sea lanterns in ceiling corners)
setblock ~2 ~4 ~2 sea_lantern
setblock ~13 ~4 ~2 sea_lantern
setblock ~2 ~4 ~13 sea_lantern
setblock ~10 ~4 ~13 sea_lantern

setblock ~2 ~9 ~2 sea_lantern
setblock ~13 ~9 ~2 sea_lantern
setblock ~2 ~9 ~13 sea_lantern
setblock ~13 ~9 ~13 sea_lantern
