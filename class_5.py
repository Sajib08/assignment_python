'''
To create a mobile phone shop which is started with category mobile phone stored.
Now update daily sell and manage customer.
'''
#This is the list of mobile phone store in the shop.
mobile_name=['samsung galaxy','samsung note','samsung prime','i phone','one plus','blackberry','walton']
# One customer want to see the mobile list 
for name in mobile_name:
    print(name)
#One customer want to search one kind of mobile phone store in the shop.
customer_mobile=input("Enter your phone name which phone do you search: ")
if customer_mobile in mobile_name:
    print('Good news, This mobile is stored.')
else:
    print('Sorry Sir, It is not stored .')

# New phone is come to the shop. Now the shopkeper want to add this mobile phone in the list.
mobile_name.append('Huwei')
print(mobile_name)

# Suddenly one plus is stocked out from your shop. Now updating your list.
mobile_name.remove('one plus')
print(mobile_name)

# Samsung lunch their new phone. Now you store this phone beside the samsung phone.
mobile_name.insert(3,'samsung Z')
print(mobile_name)

# There are some new types mobile phone lunch in the market. Add them your shop.
new_mobile=['itone','symphone','nokia','gmobile'] 
mobile_name.extend(new_mobile)
print(mobile_name+new_mobile) #Another way to add your phone list.
print(mobile_name)

    # Use list , index print formatting showing result.
students_name=['sajib','preetom','showrov','toha','najmul','anik','fahim','akhi','chowa','saifa']
students_number=[83,45,76,91,56,82,67,90,63,34]
student='showrov'
a=(students_name.index('showrov'))
print("%s's number is %d"%(students_name[a],students_number[a]))


# To add two list in one list and access index
students_name=['sajib','preetom','showrov','toha','najmul','anik','fahim','akhi','chowa','saifa']
students_number=[83,45,76,91,56,82,67,90,63,34]
x=[str(i) for i in students_number]
print(x)

add=students_name+x
print(add)
add.sort()
print(add)


# To add two list in one list and access index
students_name=['sajib','preetom','showrov','toha','najmul','anik','fahim','akhi','chowa','saifa']
students_number=[83,45,76,91,56,82,67,90,63,34]
one_list=[students_name+students_number]
print(one_list)
print(one_list[0][3])                   #To access value in the list
print(one_list[0].index(76))            #To see vlaue index in the list.
print(one_list[0][-1])                  #To see the value from the list.
print(one_list[0][4:])                  #To see the value from the certain value.
print(one_list[0][:4])                  #To see the value up to the certain value.
print(students_name[::-1])              #To reverse using this method.
print(one_list[0][1:19:2])              #To see the value x to y range.
print(one_list.sort())

""" 
To use tuple making a vegitable shop. Using method manage your shop.
"""
vegitable=('onion','potato','ginger','cucumber')
for name in vegitable:
    print(name)

print(vegitable[3])
print(vegitable[1:3])
vegitable[1]='ladies fingur'
print(vegitable) #It doesn't work. Tuple can't chenge and add. This is the main properties from the list.
new_vlaue=(3.1416,80)
print(vegitable+(new_vlaue))

'''
Md Nesser Uddin
Batch-PYTH N212-2
'''

#step-1:::Normally print name and age list
name=["max","alica","cruso","jenifer"]
age=[12,14,26,30,12]
print(name,age)
#step-2:::append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
add_name_age=name,age
print(add_name_age)
count_func1=name.count("max")
count_func2=age.count(12)
print(count_func1,count_func2)
name.extend(age)
print(name)
name.append(age)
print(name)
name.insert(0,"nelson")
age.insert(0,20)
print(name,age)
print(name.index("cruso"))
age.reverse()
print(age)
age.sort()
print(age)
age.remove(age[0])
print(age)
age.clear()
print(age)
age=name.copy()
print(age)
print(age.pop())

#step-3::::'count', 'index'
tpl1=(1,2,3,3,5)
tpl2=("Adif","akif","adnan","jenifar","jaslin")
print(type(tpl1))
print(type(tpl2))
print(tpl1.count(3))
print(tpl2.count("akif"))
indx=tpl2.index("adnan")
print(f"Index number: {indx}")
#check_ type of tuple attribute
for i in tpl2:
    print(i,":", type(i))
for i in tpl1:
    print(i,":", type(i))
#if,if..clse, if..elif..else condition
new_list = ["foodpanda", "hungrinaki", "efood", "sohoj", "sheba"]
update_list=[]
print(update_list)
print((new_list))
while True:
    user_input = input("Enter your choice: ")
    if user_input in new_list:
        print(f"welcome!! now you are {user_input} user")
    else:
        print("Invalid Name!!!!")
