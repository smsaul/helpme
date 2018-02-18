def menu():
  print("Press L or R")
  input == input()
  if input == "l" or input == "left":
    print("Left Menu")
  elif input == "r" or input == "right":
    print("Right Menu")
  else:
    print("You didn't do it!")
    menu()

menu()
