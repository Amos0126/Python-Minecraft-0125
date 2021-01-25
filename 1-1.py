from mcpi.minecraft import Minecraft
Amos = Minecraft.create()

print(Amos.player.getTilePos())
(Amos.postToChat("<Amos2021> abc"))
(Amos.createExplosion(22,40,302,power=10000000))
Amos.player.setTilePos(100,100,100)