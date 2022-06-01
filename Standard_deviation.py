import math
import csv 

from google.colab import files
a=files.upload()


with open("data.csv") as f:
  read = csv.reader(f)
  file_data = list(read)
  data = file_data[0]
def man(data):
  l = len(data)
  total = 0
  for x in data:
    total += float(x)
  mean = total/l
  return mean  

  sq_list=[]
for n in data:
  a = int(n)-mean(data)
  a = a*a
  sq_list.append(a)

  
sum=0
for i in sq_list:
  sum += i
  result = sum/len(data)
  std_dev = math.sqrt(result)
  print(std_dev)
