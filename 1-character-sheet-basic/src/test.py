#!/usr/bin/python
import charactersheet

print("Henrik's character sheet")
new_character = charactersheet.roll_new("Henrik", "M")
print(charactersheet.desribe(new_character))

print("Selena's character sheet")
new_character = charactersheet.roll_new("Selena", "F")
print(charactersheet.desribe(new_character))