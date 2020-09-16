# Building a character sheet

## The Problem
Playing a tabletop RPG requires a lot of stuff to be tracked on a piece of paper called **Character Sheet** - stuff like character stats, modifiers, inventory, gold amount, traits and much more. We want to simplify that process by creating a python app that is going to manage it for the players. Eventually, we are going to build a cool UI for this, but at first, we must think about **how we are going to store that data**.

As a part of the first part of this project, we are going to build a **data structure** and a **set of functions** that are going to manipulate that structure. Propreties that we want to track for now are the following:
- Name of the Character
- Their race (Human, Elf, Dwarf, etc...)
- Their gender (Male/Female)
- Their class (Fighter, Ranger, Priest, Wizard, etc...)
- Character's bio - a short description of the character.
- All of their attributes (numbers, varying from 3 to 20. Attributes are the following: Strength, Agility, Constitution, Intelligence, Wizdom, Charisma)
- Traits (A set of keywords that describe the character and thrir background - e.g. "Noble", "War Veteran", "Scholar", "Actor", etc...)
- Inventory (A set of items that the character is carrying on them at the momement - e.g. "Steel broadsword", "A length of rope", "A vial of poison", "Health potion", etc...)

Functions that will have to be implemented:
- Roll new character - should take in a name and a gender and return a newly-created random character with properties that make sense.
- Describe - should take in the character and return a paragraph of text describing the character.