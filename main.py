from package.subpack1.module1 import *
import package.subpack2.module2 as md2 

pl1 = md2.player()
pl2 = md2.player(1,1)
myProfile = md2.person(myName, myYob, myHometown)

print(pl1.x, pl1.y)
print(pl2.x, pl2.y)
print(myProfile.name, myProfile.yob, myProfile.ht)