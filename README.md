# Redstone Minecraft Projects

This repository contains ready-to-use add-ons for both Java and Bedrock to instantly spawn fully automated Redstone machines.

## 🚀 Flying Machine Launcher

We've set up complete, drag-and-drop packs so you don't have to copy-paste any command blocks!

### 🛑 QUICK FALLBACK: Raw Commands (No Pack Required)
If your Minecraft version is outright refusing to load the Datapack or Behavior Pack due to recent strict version update differences, just grab a Command Block (`/give @s command_block`), place it, paste this exact code inside it, and activate it with a button. It will instantly spawn the flying machine directly above the command block!

**Java Edition All-in-One Initializer:**
```mcfunction
summon falling_block ~ ~3 ~ {BlockState:{Name:"minecraft:observer",Properties:{facing:"west"}},Time:1,Passengers:[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:sticky_piston",Properties:{facing:"east"}},Time:1,Passengers:[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:honey_block"},Time:1,Passengers:[{id:"minecraft:falling_block",BlockState:{Name:"minecraft:honey_block"},Time:1}]}]}]}
```
*(Alternatively, just run the lines below one-by-one in your chat standing in the same spot!)*
```mcfunction
/setblock ~ ~1 ~ observer[facing=west]
/setblock ~1 ~1 ~ sticky_piston[facing=east]
/setblock ~2 ~1 ~ honey_block
/setblock ~3 ~1 ~ honey_block
/setblock ~1 ~ ~ slime_block
/setblock ~2 ~ ~ slime_block
/setblock ~3 ~ ~ sticky_piston[facing=west]
/setblock ~4 ~ ~ observer[facing=east]
/setblock ~-1 ~1 ~ redstone_block
/setblock ~-1 ~1 ~ air
```

---

### How to Install Using the Packs (Automated Method)
**For Java Edition:**
1. Copy the `JavaPack` folder from this repository.
2. Paste it directly into your Minecraft world's datapack folder: `\saves\<Your World Name>\datapacks\`
3. Leave your world and jump back in (or type `/reload`) to clear its Datapack cache.
4. Aim high up in the air and type: `/function redstone:launch_java`

**For Bedrock Edition:**
1. Copy the `BedrockPack` folder from this directory.
2. Paste it into your `development_behavior_packs` folder (usually located in `%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs`).
3. Open your world settings, go to Behavior Packs, and activate the "Redstone Launcher Behavior Pack".
4. Jump back into your world, aim up in the sky, and type `/function launch_bedrock`
