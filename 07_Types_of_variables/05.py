# **data member is a variable of the class whose values can be accessed across all functions of the class**

class School:
  scnm='PRMIT&R'
  def show(self,scnm):
    print(f'local- school name is {scnm}')
    print(f'global- school name is {self.scnm}')
  def display(self):
    print(self.scnm)

obj=School()
obj.show("zp school")
obj.display()




class Player:
  def __init__(self):
    self.playernm="Not available"
    self.country="NA"
  def takedata(self):
    self.playernm=input('Enter player name : ')
    self.country=input('Enter country : ')
  def showdata(self):
    print(f"Player name is {self.playernm}")
    print(f"Country is {self.country}")

p=Player()
p.takedata()
p.showdata()
obj=Player()
obj.showdata()