#Categorizing Values

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

print(myMixedTypeList[3])
print(myMixedTypeList)

for item in myMixedTypeList:
    print(f"{item} is the type of {type(item)}")

#for i in range (5):
#   print(i)

for i in range(4, len(myMixedTypeList)):
    print(myMixedTypeList[i])
    
for i in range(2,5):
    print(i)