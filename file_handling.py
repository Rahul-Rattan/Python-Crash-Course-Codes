file=open("hello.txt",'r')
def lenght(file):
    lst=[]
    for line in file:
        a=line.split(" ")
        for word in a:
            word=word.strip("\n")
            if word!="":
                lst.append(word)
    return len(lst)

r=lenght(file)
file.close()
print(r)