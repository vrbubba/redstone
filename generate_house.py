import os

def generate_house(filename="JavaPack/data/redstone/function/build_house.mcfunction"):
    commands = []
    
    # House Dimensions
    W = 15 # Width (X axis)
    L = 20 # Length (Z axis)
    H = 6  # Height of first floor walls
    
    # Origin is ~ ~ ~ (bottom left corner of the front face)
    
    # 1. Clear the area entirely
    commands.append(f"fill ~-1 ~-1 ~-1 ~{W+1} ~{H+10} ~{L+1} air")
    
    # 2. Floor (Cobblestone)
    commands.append(f"fill ~ ~-1 ~ ~{W} ~-1 ~{L} cobblestone")
    commands.append(f"fill ~ ~ ~ ~{W} ~ ~{L} oak_planks") # Interior floor
    
    # 3. Outer Walls (Cobblestone base, Oak Planks above)
    commands.append(f"fill ~ ~1 ~ ~{W} ~{H} ~{L} oak_planks")
    commands.append(f"fill ~1 ~1 ~1 ~{W-1} ~{H} ~{L-1} air") # Hollow out the interior
    
    # 4. Support Pillars (Oak Logs at the 4 corners)
    commands.append(f"fill ~ ~ ~ ~ ~{H} ~ oak_log")
    commands.append(f"fill ~{W} ~ ~ ~{W} ~{H} ~ oak_log")
    commands.append(f"fill ~ ~ ~{L} ~ ~{H} ~{L} oak_log")
    commands.append(f"fill ~{W} ~ ~{L} ~{W} ~{H} ~{L} oak_log")
    
    # 5. Windows
    # Front and Back Windows
    commands.append(f"fill ~4 ~2 ~ ~{W-4} ~3 ~ glass")
    commands.append(f"fill ~4 ~2 ~{L} ~{W-4} ~3 ~{L} glass")
    
    # Side Windows
    commands.append(f"fill ~ ~2 ~4 ~ ~3 ~{L-4} glass")
    commands.append(f"fill ~{W} ~2 ~4 ~{W} ~3 ~{L-4} glass")
    
    # 6. Door (Front center)
    center_x = W // 2
    commands.append(f"fill ~{center_x} ~1 ~ ~{center_x+1} ~2 ~ air")
    # Place standard doors requires blocks, so we just leave an archway or use actual door blocks
    # Spruce door requires bottom and top half:
    commands.append(f'setblock ~{center_x} ~1 ~ spruce_door[half=lower,facing=north]')
    commands.append(f'setblock ~{center_x} ~2 ~ spruce_door[half=upper,facing=north]')
    commands.append(f'setblock ~{center_x+1} ~1 ~ spruce_door[half=lower,facing=north,hinge=right]')
    commands.append(f'setblock ~{center_x+1} ~2 ~ spruce_door[half=upper,facing=north,hinge=right]')
    
    # 7. Roof (A-Frame Pitched Roof)
    # The roof will peak in the middle of X
    roof_height = (W // 2) + 1
    for i in range(roof_height + 1):
        y_level = H + 1 + i
        
        # Left side stairs
        left_x = i
        commands.append(f"fill ~{left_x} ~{y_level} ~-1 ~{left_x} ~{y_level} ~{L+1} oak_stairs[facing=east]")
        
        # Right side stairs
        right_x = W - i
        commands.append(f"fill ~{right_x} ~{y_level} ~-1 ~{right_x} ~{y_level} ~{L+1} oak_stairs[facing=west]")
        
        # Fill the gable (the triangular wall piece under the roof on the front and back)
        if i > 0 and left_x < right_x:
            commands.append(f"fill ~{left_x+1} ~{y_level-1} ~ ~{right_x-1} ~{y_level-1} ~ oak_planks")
            commands.append(f"fill ~{left_x+1} ~{y_level-1} ~{L} ~{right_x-1} ~{y_level-1} ~{L} oak_planks")
            
    # Add a ridge line at the very absolute top if it's an even dimension width, but W=15 is odd. 
    # Center is at X=7. 
    final_y = H + 1 + roof_height
    commands.append(f"fill ~{center_x} ~{final_y} ~-1 ~{center_x} ~{final_y} ~{L+1} oak_slab[type=bottom]")
    
    # 8. Interior Lighting (Torches)
    commands.append(f"setblock ~2 ~3 ~2 torch")
    commands.append(f"setblock ~{W-2} ~3 ~2 torch")
    commands.append(f"setblock ~2 ~3 ~{L-2} torch")
    commands.append(f"setblock ~{W-2} ~3 ~{L-2} torch")
    
    # 9. Inside feature: A simple bed and crafting area
    commands.append(f"setblock ~2 ~1 ~{L-2} crafting_table")
    commands.append(f"setblock ~3 ~1 ~{L-2} furnace")
    commands.append(f"setblock ~4 ~1 ~{L-2} chest")
    commands.append(f"setblock ~2 ~1 ~{L-4} red_bed[part=head,facing=south]")
    commands.append(f"setblock ~2 ~1 ~{L-5} red_bed[part=foot,facing=south]")

    # Write out
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("\n".join(commands))
        
    print(f"Generated {len(commands)} commands successfully to {filename}!")

if __name__ == "__main__":
    generate_house()
