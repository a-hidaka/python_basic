set_numbers={1,2,3,4,}
print (type(set_numbers) )

set_numbers = {1, 2, 3, 4, 5}
#print (set_numbers [0])

empty_set = set ()
print (type(empty_set) )

empty_set = set ()
print (type(empty_set) )

numbers = 11, 1, 1, 1, 2, 31
convert_to_set = set (numbers)
print (convert_to_set)

convert_to_set.add (1)
convert_to_set.add (100)
print (convert_to_set)

convert_to_set. remove (100)
print (convert_to_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set.union (set2)
# *L<I union_set = set1 | set2
print(union_set) # {1, 2, 3, 4, 5}

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
setc = setA. intersection(setB)
#もしくはsetc=setA&setB
print (setc) # {3, 4}

setA = {11, 2, 3, 4}
setB = {13, 4, 5, 6}
setc = setA.difference (setB)
# L< setC = setA - setB
print (setc) # {1, 2}

setA = {11, 2, 35}
setB = {12, 3, 4}
setC = setA. symmetric_difference(setB)
# *U<d set_C = set_A ^ set_B
print(setC) # {1, 4}

