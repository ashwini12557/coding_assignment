import math 
def SupportFunction(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def MainFunction(array_val,n,k,l):
    result = +2147483647 
    final_output.clear()
    array_val.sort()
    print(array_val)    
    for i in range(n-k+1): 
        result = int(min(result, array_val[i+k-1] - array_val[i])) 
    for j in range(0,l):
        for name,value in input_items.items():
            if(k>math.ceil(n/2)):
                if(int(value)==array_val[k-j]):
                    val = SupportFunction([name,value])
                    final_output.update(val);
            elif(int(value)==array_val[k+j]):
                val = SupportFunction([name,value])
                final_output.update(val)
    return result

#Open input file
open_input_file = open("sample_input.txt",'r')
global input_items, final_output 
input_items = {}
final_output = {}
#reading input file data and storing in input array
for line in open_input_file:
    lines = line.split(":")
    val = SupportFunction(lines)
    input_items.update(val)
    
print(input_items);
val = (input_items.values())
print(val);
actual = []
#read of int value prices and store in actual array
for n in val:
    actual.append(int(n))
print(actual);
arr= actual 
n =len(arr) 
open_input_file.close()
while(True):
    f = open("sample_output.txt", "a")
    k = int(input("Please Enter Number of employees : ")) 
    f.write("Number of employees : "+str(k))
    f.write("\n")
    f.write("Here the input_items that are selected for distribution are:")
    f.write("\n")
    result = MainFunction(arr, n, k,k)
    for name,value in final_output.items():
        f.write(name+" : "+value)
    f.write("\n")
    print("Output File Written")
    f.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(result))
    f.write("\n")
    f.close()

