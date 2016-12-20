import server
from mcpi import minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
#from time import sleep
import time

mc = minecraft.Minecraft.create(server.address)

mcdrawing = minecraftstuff.MinecraftDrawing(mc)


def labBlock():
    b = mc.getBlock(173, 2, -1451)
    if b == 14:
        mc.setBlock(180, 5, -1451, 41)
    else:
        mc.setBlock(180, 5, -1451, 0)          
        

while True:
    labBlock()
    #labSphere()
    


#END
