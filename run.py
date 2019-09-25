from MonsterInc import *

monster1 = Monster('Gary','soft',['being cute','amazing agility','good companion'],'very cute')
print('name of monster = ', monster1.name)
print('number of eyes = ',monster1.nu_of_eyes)
print('skills = ',monster1.skills)
print('cuteness = ',monster1.cute)

print(monster1.tired())
print(monster1.sleep())
print(monster1.nightmare())
print('/////////////////////////')

monster2 = Monster('Josh','no fur',['bargainer','lone wolf','amazing swimmer'],'ugly', 30)
print(monster2.name)

print('name of monster = ', monster2.name)
print('number of eyes = ',monster2.nu_of_eyes)
print('skills = ',monster2.skills)
print('cuteness = ',monster2.cute)

print(monster2.transform('bucket'))
print('/////////////////////////')
monster3 = Monster('Jessica','extremely furry',['telepathic','profficient in python','people person'],'sort of cute', 3)
print('name of monster = ', monster3.name)
print('number of eyes = ',monster3.nu_of_eyes)
print('skills = ',monster3.skills)
print('cuteness = ',monster3.cute)

print(monster3.eat('Hummus'))
print(monster3.scare())
print('/////////////////////////')
