numberlen = int(input("How many integers you want to sort: "))
numbers = []

for i in range(numberlen):
      numbers.append(int(input("Enter "+str(i+1) +" integer: ")))

ascsortednum=sorted(numbers,reverse=False)
descsortednum=sorted(numbers,reverse= True)

print("Ascending order :"+str(ascsortednum))
print("Descending order :"+str(descsortednum))