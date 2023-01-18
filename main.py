from random import *
class Cet:
  def __init__(self, сet):
	  self.name = сet
	  self.lives = 9
	  self.enegiya = 100
	  self.alive = True
  def to_play ( self ):
    print("вермя игать")
    self.enegiya -=5
  def to_sharpen ( self ):
    print("вермя точить коготки")
    self .enegiya -=15
  def to_hunting ( self ):
    print("время охоты")
    self .enegiya -=25
    self .lives -=2
  def to_acrobatics ( self ):
    print("время прогулки по балкону")
    self .enegiya -=12
    self .lives -=1
  def to_company ( self ):
    if white.lives > 0:
     print("время игать с другим котенком")
     self .enegiya +=25
     self .lives +=1
  def is_alive(self):
	  if self.lives < 0:
		  print("котик не выжил :(")
		  self.alive = False
  def is_tired(seif):
    if self.enegiya < 0:
      print("котик устал")
  def live(self, day):
	  day = "Day " + str(day) + " of " + 	self.name + " life"
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
    elif live_cube == 5:
	      self.to_company ()
	  self.is_alive()

black = Cet('Черныш')
for i in range(365):
	if black.alive == False:
		break
	black.live(i)


  
class Cet2:
  def __init__(self, сet2):
	  self.name = сet2
	  self.lives = 9
	  self.enegiya = 100
	  self.alive = True
  def to_play ( self ):
    print("вермя игать")
    self.enegiya -=5
  def to_sharpen ( self ):
    print("вермя точить коготки")
    self .enegiya -=15
  def to_hunting ( self ):
    print("время охоты")
    self .enegiya -=25
    self .lives -=2
  def to_acrobatics ( self ):
    print("время прогулки по балкону")
    self .enegiya -=12
    self .lives -=1
  def to_company ( self ):
    if black.lives > 0:
     print("время игать с другим котенком")
     self .enegiya +=25
     self .lives +=1
    
  def is_alive(self):
	  if self.lives < 0:
		  print("котик не выжил :(")
		  self.alive = False
  def is_tired(seif):
    if self.enegiya < 0:
      print("котик устал")
  def live(self, day):
	  day = "Day " + str(day) + " of " + 	self.name + " life"
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
    elif live_cube == 5:
	      self.to_company ()
    
	  self.is_alive()

white = Cet2('беляш')
for i in range(365):
	if white.alive == False:
		break
	white.live(day)