# Phase 2: Start platform + Stage 1 piston door
fill ~-5 ~0 ~-3 ~9 ~0 ~3 quartz_block
fill ~-5 ~1 ~-3 ~9 ~4 ~-3 quartz_block
fill ~-5 ~1 ~3 ~9 ~4 ~3 quartz_block
fill ~-5 ~1 ~-2 ~-5 ~4 ~2 quartz_block
fill ~-5 ~1 ~-4 ~-5 ~6 ~-4 red_concrete
fill ~9 ~1 ~-4 ~9 ~6 ~-4 red_concrete
fill ~-4 ~6 ~-4 ~8 ~7 ~-4 red_concrete
fill ~0 ~7 ~-4 ~4 ~8 ~-4 yellow_concrete
fill ~0 ~6 ~-4 ~4 ~6 ~-4 white_concrete
# --- Stage 1: Piston Door ---
fill ~1 ~1 ~3 ~3 ~3 ~3 iron_block
setblock ~1 ~1 ~4 sticky_piston ["facing_direction"=2]
setblock ~1 ~2 ~4 sticky_piston ["facing_direction"=2]
setblock ~1 ~3 ~4 sticky_piston ["facing_direction"=2]
setblock ~2 ~1 ~4 sticky_piston ["facing_direction"=2]
setblock ~2 ~2 ~4 sticky_piston ["facing_direction"=2]
setblock ~2 ~3 ~4 sticky_piston ["facing_direction"=2]
setblock ~3 ~1 ~4 sticky_piston ["facing_direction"=2]
setblock ~3 ~2 ~4 sticky_piston ["facing_direction"=2]
setblock ~3 ~3 ~4 sticky_piston ["facing_direction"=2]
setblock ~0 ~2 ~2 stone_button ["facing_direction"=3]
setblock ~0 ~1 ~3 redstone_wire
setblock ~0 ~1 ~4 redstone_wire
setblock ~1 ~1 ~5 redstone_wire
setblock ~2 ~1 ~5 redstone_wire
setblock ~3 ~1 ~5 redstone_wire
fill ~0 ~0 ~3 ~0 ~0 ~4 stone
fill ~1 ~0 ~5 ~3 ~0 ~5 stone
fill ~-2 ~2 ~0 ~-2 ~3 ~0 white_concrete
setblock ~2 ~4 ~-2 sea_lantern
