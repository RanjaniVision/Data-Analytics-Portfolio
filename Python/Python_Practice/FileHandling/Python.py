'''this one method for file opening,read and close
file=open('text_file.txt','r')
data=file.read()
print(data)
file.close()'''

#another method for open read  
'''with open('text_file.txt','r') as file:
    data = file.read()
    print(data)'''

    #line by line print
'''with open('text_file.txt','r') as file:
    data=file.read()
    print(data)
    for line in file:
        print(line)'''


with open('text_file.txt','r') as file:
    data=file.read()
    print(data)
    for line in file:
        for word in line.split():
            print(word)

with open('text_file.txt','w') as file:
    file.write("Python")

with open('text_file.txt','r') as file:
    data=file.read()
    print(data)
with open('text_file.txt','a') as file:
    file.write("append")