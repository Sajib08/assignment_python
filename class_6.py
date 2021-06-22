t=('sajib','preetom','toha')

# To see index in tuple's element.
print(t.index('preetom'))

# To access the tuple value.
print(t[1])

# Doesn't add any value with tuple.
t.append(1)

# Doesn't exchang any value in tuple.
print(t[0]=10)

# In the tuple value rediclar.
print(t+('toha',))
print(t)

# In the tuple has one hacks to reasign value.
t+=('toha',)
print(t)
myset1={2,5,6,3,8,1,19}
myset2={10,20,1,27,3,7,8}

''' add(...)
      Add an element to a set.
This has no effect if the element is already present.'''
myset1.add(4)         #this is existed.
myset1.add("sajib")   #this is existed.
myset1.add(5)         #Already it has. It isn't existed.
print(myset1)

"""
clear(...)
       Remove all elements from this set. 
 """
myset2.clear() # Clear to all the elements from the set.
print(myset2)

""" 
copy(...)
       Return a shallow copy of a set.
 """
myset3=myset1.copy()
print(myset3)

""" difference(...)
       Return the difference of two or more sets as a new set.
 
       (i.e. all elements that are in this set but not the others.) """
myset1={2,5,6,3,8,1,19}
myset2={10,20,1,27,3,7,8}
print(myset1.difference(myset2))#{2, 19, 5, 6}
print(myset1)      # In this differece method myset1 doesn't update.{1, 2, 3, 5, 6, 8, 19}
(myset1.difference_update(myset2))
print(myset1)     #{2, 5, 6, 19} Remove all elements of another set from this set.

""" discard(...)
       Remove an element from a set if it is a member.
 
       If the element is not a member, do nothing. """
myset1={2,5,6,3,8,1,19}
myset1.discard(6)   # It removes
myset1.discard(10)  # It doesn't removes
print(myset1)

""" intersection(...)
       Return the intersection of two sets as a new set.
       (i.e. all elements that are in both sets.) """
myset1={2,5,6,3,8,1,19}
myset2={10,20,1,27,3,7,8}
print(myset1.intersection(myset2))#{8, 1, 3}
print(myset1)      # In this intersection method myset1 doesn't update.{1, 2, 3, 5, 6, 8, 19}
(myset1.intersection_update(myset2))
print(myset1)     #{8, 1, 3} Remove all elements of another set from this set.

""" isdisjoint(...)
       Return True if two sets have a null intersection. """
myset1={2,5,6,3,8,1,19}
myset2={10,20,1,27,3,7,8}
print(myset1.isdisjoint(myset2)) # Match value between two set. OP: Flase
myset1={2,5,}
myset2={10,20}
print(myset1.isdisjoint(myset2)) # Doesn't match any value for this reasion result out True.

""" issubset(...)
       Report whether another set contains this set. """

""" issuperset(...)
       Report whether this set contains another set. """
myset1={2,5,10,20}
myset2={10,20}
print(myset1.issubset(myset2)) # OP: Flase. myset1 isn't subset of myset2
print(myset2.issubset(myset1)) # OP: True. myset1 is subset of myset2
print(myset2.issuperset(myset1)) # Subset and superset are reverse.

""" pop(...)
       Remove and return an arbitrary set element.
       Raises KeyError if the set is empty. """
myset1={2,5,10,20}
myset1.pop()
print(myset1)
myset1.pop()
print(myset1)
myset1.pop()
print(myset1)
myset1.pop()
print(myset1)
myset1.pop()
print(myset1) # For the empty set raise KeyError.
""" remove(...)
      Remove an element from a set; it must be a member.
 
       If the element is not a member, raise a KeyError. """
myset1={2,5,10,20}
myset1.remove(5) # It works
print(myset1)
myset1.remove(30) # It doesn't work.
print(myset1)     # Raise KeyError becuse 30 is not member of this set.

"""  symmetric_difference(...)
     symmetric_difference_update(...)
       Return the symmetric difference of two sets as a new set.
 
       (i.e. all elements that are in exactly one of the sets.) """
# It means that between two set uncommon value return. to creat set extract common value.
myset1={2,5,6,3,8,1,19}
myset2={10,20,1,27,3,7,8}
print(myset1.symmetric_difference(myset2))
print(myset1)   # In this print the myset1 is not updated.
print(myset1.symmetric_difference_update(myset2))
print(myset1)   # In this print the myset1 is updated.

""" union(...)
 |     Return the union of sets as a new set.
 
       (i.e. all elements that are in either set.)
 
   update(...)
       Update a set with the union of itself and others. """
myset1={2,5,6,3,8,1,19}
myset2={10,20,1,27,3,7,8}
print(myset1.union(myset2))
print(myset1)
print(myset1.update(myset2))
print(myset1)



""" 
Dictonary In-Built function.
len(), any(), all(), sorted()
 """
mydic1={1:4,5:8,6:3,4:9}
mydic2={'':2,0:3}
mydic3={'a':2,0:3}
mydic4={1:4,5:8,6:3,'':9}
print(len(mydic1))
print(any(mydic2)) # In this dictonary there is no keyword. That's why Flase.
print(any(mydic3)) # In this dictonary find out one keyword. That's why print True.
print(any(mydic4)) # In this dictonary any keyword is null. That's why print True.

""" clear(...)
       D.clear() -> None.  Remove all items from D. """

a={'a':34,'b':23,'c':12}
a.clear()
print(a)

""" copy(...)
       D.copy() -> a shallow copy of D """
a={'a':34,'b':23,'c':12}
b={'d':32}
b=a.copy()
print(b)

""" get(self, key, default=None, /)
       Return the value for key if key is in the dictionary, else default. """
a={'a':34,'b':23,'c':12}
b=a.get('b')
print(b)
d=a.get('s')# Don't raise up if there are no value in the dict.

""" items(...)
    keys(...)
    values(...)
      D.items() -> a set-like object providing a view on D's items """
a={'a':34,'b':23,'c':12}
print(a.items())
print(a.keys())
print(a.values())

"""  pop(...)
      popitem(self, /)
       D.pop(k[,d]) -> v, remove specified key and return the corresponding value. 
       If key is not found, d is returned if given, otherwise KeyError is raised """

a={'a':34,'b':23,'c':12}
a.pop('b')
print(a)
a.popitem()

"""  setdefault(self, key, default=None, /)
       Insert key with a value of default if key is not in the dictionary.
 
       Return the value for key if key is in the dictionary, else default. """

a={'a':34,'b':23,'c':12}
b=a.setdefault('d',56)
print(b)

#dictionary::clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
card_number={"alex":123,"jon":456,"tom":890,"jerry":972}
#password={"Forest":12345,"Gump":7699878,"jenny":909822,"lord":2666282}
vowel={"a","e","i","o","u"}
values="vowel"
print(type(card_number))
print(card_number["alex"])#output::123
upd1={"lord":156}
card_number.update(upd1)
print(card_number) #output::{'alex': 123, 'jon': 456, 'tom': 890, 'jerry': 972, 'lord': 156}
upd2=card_number.values()
print(upd2) #output::dict_values([123, 456, 890, 972, 156])
upd3=card_number.setdefault("alex")
print(f"Alex={upd3}")  #output::Alex=123
upd4=card_number.pop("lord")
print(upd4) #output::156
print(card_number) #output::{'alex': 123, 'jon': 456, 'tom': 890, 'jerry': 972}
upd5=card_number.popitem()
print(upd5) #output::('jerry', 972)
print(card_number) #output::{'alex': 123, 'jon': 456, 'tom': 890}
upd6=card_number.keys()
print(upd6) #output::dict_keys(['alex', 'jon', 'tom'])
upd7=card_number.items()
print(upd7) #output::dict_items([('alex', 123), ('jon', 456), ('tom', 890)])
upd8=card_number.get("alit")
print(upd8) #output::None
upd9=card_number.get("alex",100)
print(upd9) #output::123
print(vowel) #output::{'a', 'o', 'u', 'e', 'i'}
upd10=dict.fromkeys(vowel)
print(upd10) #output::{'o': None, 'i': None, 'u': None, 'e': None, 'a': None}
upd11=dict.fromkeys(vowel,values)
print(upd11) #output::{'u': 'vowel', 'e': 'vowel', 'o': 'vowel', 'a': 'vowel', 'i': 'vowel'}
upd12=card_number.copy()
print(upd12) #output::{'alex': 123, 'jon': 456, 'tom': 890}
upd13=card_number.clear()
print(upd13)#output::None

#::::set::
#'add', 'clear', 'copy', 'difference', 'discard', 'intersection',
#'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'union', 'update'

set1={"a","b","c","e","f"}
set2={1,2,3,4,5}
set3={"c","g","f"}
set4={3,5,7,2}
set5={9,7,2,5}
print(type(set1))
print(type(set2))
set1.add("g")
print(set1) #output::{'f', 'b', 'a', 'e', 'g', 'c'}..   Question???
copy_set=set1.copy()
print(copy_set)  #output::{'c', 'e', 'g', 'b', 'f', 'a'}....Question???
copy_set.clear()
print(copy_set)#output::set()
print(set1.difference(set3))#output::{'a', 'b', 'e'}
print(set3.difference(set1)) #output::set()
set2.discard(2)
print(set2) #output::{1, 3, 4, 5}

set1={"a","b","c","e","f"}
set2={1,2,3,4,5}
set3={"c","g","f"}
set4={3,5,7,2}
set5={9,7,2,5}
print(set2.intersection(set4)) #output::{2, 3, 5}
print(set2.intersection(set4,set5)) #output::{2, 5}

print(set2 & set4)#output::{2, 3, 5}
print(set2 & set4 & set5) #output::{2, 5}
a={1,2,3,4}
b={5,6,7}
c={4,5,6}
print(a.isdisjoint(b)) #True
print(a.isdisjoint(c)) #False
print(a.issuperset(b)) #False
print(a.issubset(c)) #False
print(a.symmetric_difference(c)) #{2, 3, 5, 6}....show uncommon values
print(a.union(b)) #{1, 2, 3, 4, 5, 6, 7}
a.remove(3)
print(a) #{1, 2, 4}
a.pop()
print(a) #{2, 3, 4}
#string manipulation::
st1="hello world"
str2="how\tare\ttyou"
st2="hello"
st3="      hello      "
st4="how are you"
print(st1.capitalize()) #Hello world
print(st1.casefold()) #hello world
spac=st1.center(20,"-") #----hello world-----
print(spac)
print(st1.count("o")) #2
print(st1.encode()) #b'hello world'
print(st1.endswith("d")) #True
print(st1.endswith("world",6,12)) #true
print(str2.expandtabs())#how     are     tyou
print(str2.expandtabs(10))#how       are       tyou
print("Hello {}, how are you, your id number {}?".format("alex",123))#Hello alex, how are you, your id number 123?
print("Hello {0}, how are you, your id number {1}?".format("alex",123))#Hello alex, how are you, your id number 123?
print("Hello {name}, how are you, your id number {id_n}?".format(name="alex",id_n=123))#Hello alex, how are you, your id number 123?
print("Hello {0}, how are you, your id number {id_n}?".format("alex",id_n=123))#Hello alex, how are you, your id number 123?
print(st1.index("rld"))#8
print(st1.isalnum())#false
print(st1.isdecimal())#false
print(st1.isalpha())#false
print(st1.isupper())#false
print(st1.isdigit())#false
print(st1.islower())#True
print(st1.isdigit())#false
print(st1.isspace())#false
print(st1.title())#Hello World
print(st1.istitle())#false
print(st2.ljust(10,"-"))#hello-----
print(st2.rjust(10,"-"))#-----hello
print(st2.swapcase())#HELLO
print(st3.lstrip()) #"hello      "
print(st3.rstrip())#"      hello"
print(st4.partition("are"))#('how ', 'are', ' you')
print(st4.replace("how","what"))#what are you
print(st4.split(" "))#['how', 'are', 'you']
print(st4.startswith("how"))#True