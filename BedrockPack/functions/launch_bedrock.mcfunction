# Bedrock Edition Flying Machine (Already Launched)
# Bedrock doesn't drop blocks from 1-tick pulses, so a 1-way "caterpillar" machine requires one Normal Piston and one Sticky Piston.
# This spawns an automated flying machine moving East (+X).

# Clear space
fill ~ ~ ~ ~6 ~1 ~2 air

# Bedrock uses ["facing_direction"=0(Down), 1(Up), 2(North), 3(South), 4(West), 5(East)]
# 4 = West (-X), 5 = East (+X)

# Push Engine (Normal piston pushes, doesn't pull back)
setblock ~ ~1 ~ observer ["facing_direction"=4]
setblock ~1 ~1 ~ piston ["facing_direction"=5]
setblock ~2 ~1 ~ honey_block
setblock ~3 ~1 ~ honey_block

# Pull Engine (Sticky piston grabs and pulls the rest forward)
setblock ~1 ~ ~ slime_block
setblock ~2 ~ ~ slime_block
setblock ~3 ~ ~ sticky_piston ["facing_direction"=4]
setblock ~4 ~ ~ observer ["facing_direction"=5]

# Launch the machine!
setblock ~-1 ~1 ~ redstone_block
setblock ~-1 ~1 ~ air
