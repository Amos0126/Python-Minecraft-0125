from mcpi.minecraft import Minecraft
import time
amos = Minecraft.create()

x = 1000
y = 1000
z = 100

time.sleep(5)
while 1+1==2 :
    amos.player.setPos(x,y,z)
    x = x - 50