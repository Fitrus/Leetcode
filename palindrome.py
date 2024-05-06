x = input("value ")
value = x
value_list = list()
reverse = list()

for i in value:
    value_list.append(i)
        
reverse = list(reversed(value_list))

print("Original list:", value_list)
print("Reversed list:", reverse)

if value_list == reverse:
    print ("The list is same")
else:
    print("The lists are different.")
