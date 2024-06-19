# Clases

class EmptyUser:
  pass

print(EmptyUser)
print(EmptyUser())

class User:
  def __init__(self, name, surname, alias = ""):
    self.name = name.lower()
    self.surname = surname.lower()
    if alias == "":
      self.alias = self.name[0].capitalize() + self.surname.capitalize()
    else:
      self.alias = alias

  def walk (self):
      print(f"{self.alias}, está caminando")

my_user = User("diego", "Chiapa")
print(my_user.name, my_user.surname, my_user.alias)
my_user.walk()

my_other_user = User("diego", "Chiapa", "Degolas")
print(my_other_user.name, my_other_user.surname, my_other_user.alias)
my_other_user.walk()