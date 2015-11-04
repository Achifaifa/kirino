#
# Consumable item file
# 
# Potions:
#   potion type:name:HP:MP:price
#
hp_potions=[  ["Basic HP potion",        10,   0,    10],
              ["HP potion",              20,   0,    25],
              ["Big HP potion",          50,   0,    60],
              ["Huge HP potion",         100,  0,    110]]
mp_potions=[  ["Basic MP potion",        0,    10,   10],
              ["MP potion",              0,    20,   25],
              ["Big MP potion",          0,    50,   60],
              ["Huge MP potion",         0,    100,  110]]
rec_potions=[ ["Basic recovery potion",  10,   10,   30],
              ["Recovery potion",        20,   20,   60 ],
              ["Big recovery potion",    50,   50,   150],
              ["Huge recovery potion",   100,  100,  300]]
#
# Tomes:
#   name:STR:INT:DEX:PER:CON:WIL:CHA:price
#
tomes=[ ["Tome of muscles",       1, 0, -1, 0, 0, 0, 0, 100],
        ["Tome of knowledge",     0, 1, 0, -1, 0, 0, 0, 100],
        ["Tome of cats",          0, 0, 1, 0, -1, 0, 0, 100],
        ["Tome of telepathy",     0, 0, 0, 1, 0, -1, 0, 100],
        ["Tome of survival",      0, 0, 0, 0, 1, 0, -1, 100],
        ["Tome of determination", 0, 0, 0, -1, 0, 1, 0, 100],
        ["Tome of charming",      0, 0, -1, 0, 0, 0, 1, 100],
        ["Tome of the gods",      1, 1, 1, 1, 1, 1, 1, 10000]]
#
# Food:
#   3:name:hunger:bad:price
#     badness ratings
#       0:No adverse effects under any circumstances
#       1:Occasional adverse effects
#       2:Damage or adverse effects assured
#
food=[["Moldy bread",           15, 1, 5],
      ["Hard bread",            20, 0, 7],
      ["Bread",                 50, 0, 10],
      ["Apple",                 25, 0, 10],
      ["Moldy apple",           20, 1, 5],
      ["Suspicious sandwich",   20, 1, 20],
      ["Sandwich",              20, 0, 30],
      ["Wine",                  10, 1, 50],
      ["Chocolate",             15, 0, 100],
      ["Moldy chocolate",       10, 1, 30],
      ["Golden Apple",          0,  2, 500],
      ["Moldy golden apple",    0,  2, 250],
      ["Moldy mold",            0,  2, 1]]
#
# Attack:
#   2:name:area type:size:damage:damage per turn
#   Area type:
#     0 - none
#     1 - straight line
#     2 - Circle
#     3 - Around player
#
# Not implemented