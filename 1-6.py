from mcpi.minecraft import Minecraft
a = Minecraft.create()

a.postToChat("I'm watching you")

while True:
    x,y,z = a.player.getTilePos()
    a.postToChat(" X:"+str(x)+" Y:"+str(y)+" Z:"+str(z))
    a.setBlock(x, y-1, z,103)