# Java Edition Flying Machine (Already Launched)
# Spawns a basic 2-way capable flying machine facing East (+X) and automatically updates it to start moving.
# Since Java edition allows 1-tick pulses to drop blocks, we use 2 sticky pistons.

# Clear space
fill ~ ~ ~ ~6 ~1 ~2 air

# Build the Back Engine (The pushers towards +X)
setblock ~ ~1 ~ observer[facing=west]
setblock ~1 ~1 ~ sticky_piston[facing=east]
setblock ~2 ~1 ~ honey_block
setblock ~3 ~1 ~ honey_block

# Build the Front Engine (The pullers attached to the Honey blocks)
# We offset this side so the Observer attaches to Slime and the Piston touches the Honey
setblock ~1 ~ ~ slime_block
setblock ~2 ~ ~ slime_block
setblock ~3 ~ ~ sticky_piston[facing=west]
setblock ~4 ~ ~ observer[facing=east]

# Launch the machine!
# By placing a block behind the starting observer and immediately breaking it, we give it a block update!
setblock ~-1 ~1 ~ redstone_block
setblock ~-1 ~1 ~ air
