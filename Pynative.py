#Merge two data frames using the following condition


# In[9]:


import pandas as pd

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)


carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
carsDf


# In[12]:


# Concatenate two data frames using the following conditions
import pandas as pd

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)

carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
carsDf


# In[ ]:





# In[18]:


#Sort all cars by Price column
import pandas as pd
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)
carsDf = carsDf1
carsDf = carsDf.sort_values(by=['Company', 'Price'], ascending=True)
carsDf.head(5)


# In[20]:


#Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()

oddElements = listOne[1:4:2]
print("Element at odd-index positions from list one")
print(oddElements)

EvenElement = listTwo[0::2]
print("Element at odd-index positions from list two")
print(EvenElement)

print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)



# In[21]:


#Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list

sampleList = [34, 54, 67, 89, 11, 43, 94]

print("Origigal list ", sampleList)
element = sampleList.pop(4)
print("List After removing element at index 4 ", sampleList)

sampleList.insert(2, element)
print("List after Adding element at index 2 ", sampleList)

sampleList.append(element)
print("List after Adding element at last ", sampleList)


# In[22]:


#Given a list slice it into a 3 equal chunks and rever each list -  range(start, stop, step)
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Origigal list ", sampleList)

length = len(sampleList)
chunkSize  = int(length/3)
start = 0
end = chunkSize
for i in range(1, 4, 1):
  indexes = slice(start, end, 1)
  listChunk = sampleList[indexes]
  print("Chunk ", i , listChunk)
  print("After reversing it ", list(reversed(listChunk)))
  start = end
  if(i != 2):
    end +=chunkSize
  else:
    end += length - chunkSize


# In[25]:


#Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element
sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Origigal list ", sampleList)

countDict = dict()

for item in sampleList:
  if(item in countDict):
    countDict[item] += 1
  else:
    countDict[item] = 1
  
print("Printing count of each item  ",countDict)


# In[28]:


#Given a two list of equal size create a set such that it shows the element from both lists in the pair
firstList = [2, 3, 4, 5, 6, 7, 8]
print("First List ", firstList)

secondList = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", secondList)

result = zip(firstList, secondList)
print(result)


# In[30]:


#Given a following two sets find the intersection and remove those elements from the first set
firstSet  = {23, 42, 65, 57, 78, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", firstSet)
print("Second Set ", secondSet)

intersection = firstSet.intersection(secondSet)
print("Intersection is ", intersection)
for item in intersection:
  firstSet.remove(item)

print("First Set after removing common element ", firstSet)


# In[31]:


#Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list
rollNumber  = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict  ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97} 

print("List -", rollNumber)
print("Dictionary - ", sampleDict)

rollNumber[:] = [item for item in rollNumber if item in sampleDict.values()]
print("after removing unwanted elemnts from list ", rollNumber)


# In[ ]:




