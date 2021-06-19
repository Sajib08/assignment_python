'''
To create a mobile phone shop which is started with category mobile phone stored.
Now update daily sell and manage customer.
'''
#This is the list of mobile phone store in the shop.
mobile_name=['samsung galaxy','samsung note','samsung prime','i phone','one plus','blackberry','walton']
# One customer want to see the mobile list 
for name in mobile_name:
    for i in range(1,13):
        print(i,'.', name,end=' ')
    print()