# скопируй код подомной
from random import *
class Cet:
  def __init__(self, сet):
	  self.name = сet
	  self.live = 9
	  self.enegiya = 100
	  self.alive = True
  def to_play ( self ):
    print("вермя игать")
    self.enegiya -5
  def to_sharpen ( self ):
    print("вермя точить коготки")
    self .enegiya -15
  def to_hunting ( self ):
    print("вредя охоты")
    self .enegiya -25
    self .live -2
  def to_acrobatics ( self ):
    print("время прогулки по балкону")
    self .enegiya -12
    self .live -1
  def is_alive(self):
	  if self.live < 0:
		  print("котик не выжил :(")
		  self.alive = False
  def is_tired(seif):
    if self.enegiya < 0:
      print("котик устал")
  def live(self, day):
	  day = "Day " + str(day) + " of " + self.name + " life"
	  print(day)
  live_cube = randint(1,4)
if live_cube == 1:
			self.to_play()
elif live_cube == 2:
			self.to_sharpen()
elif live_cube == 3:
			self.to_hunting()
elif live_cube == 4:
			self.to_acrobatics ()
self.statics()
self.is_alive()