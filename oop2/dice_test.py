from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheat_Slider

cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()
cheater3 = Cheat_Slider()

cheater1.roll()
cheater2.roll()
cheater3.roll()

cheater1.cheat()
cheater2.cheat()

print("Cheater 3 rolled" + str(cheater3.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

if sum(cheater2.get_dice()) == sum(cheater3.get_dice()):
  print("Draw!")

elif sum(cheater2.get_dice()) > sum(cheater3.get_dice()):
  print("Cheater 2 wins!")

else:
  print("Cheater 3 wins!")

