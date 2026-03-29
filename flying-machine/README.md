# Minecraft Flying Machines

This folder contains two `.mcfunction` files that will instantly build and launch a flying machine at your current position when run.

One file is explicitly for **Java Edition** and the other is for **Bedrock Edition**, because their redstone mechanics operate differently (namely, piston block-dropping behavior).

### How to Use

If you have cheats enabled in your world, you can copy the instructions inside standard command blocks or run them manually in your chat line by line! 

Alternatively, if you're using this within a datapack (Java) or behavior pack (Bedrock), you can simply call them with the `function` command:

**Java:**
```mcpl
/function redstone:flying-machine/launch_java
```

**Bedrock:**
```mcpl
/function redstone:flying-machine/launch_bedrock
```

### The Mechanism

The machines are built facing East (positive X) and spawn instantly:

1. They clear a small 2x2 section of space in front of you.
2. They place the Observer + Piston push/pull engines utilizing both Honey and Slime blocks so the sides smoothly slide past each other without breaking the 12-block push limit.
3. Automatically applies a redstone update to the rear observer to start the engines immediately.

*Just make sure you are high enough in the air so it doesn't get stuck to the ground before running!*
