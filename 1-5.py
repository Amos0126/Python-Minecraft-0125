from mcpi.minecraft import Minecraft
import time
amos = Minecraft.create()

i =0
time.sleep(2)
while True:
    i = i+1
    amos.postToChat("Number:"+str(i))
    time.sleep(1)