
def IndexOfElements(elements):


    CopyOflist=elements[:]
    sorted_list=sorted(CopyOflist)
    print("Sorted List :",sorted_list)
    lowest_number=sorted_list[0]
    highest_number=sorted_list[-1]

    indexoflowestnumber=0
    indexofhighestnumber=0

    for n in elements:
        if lowest_number==n:
            break
        else:
            indexoflowestnumber+=1

    for n in elements:
        if highest_number==n:
            break
        else:
            indexofhighestnumber+=1

    print("The lowest number is ", lowest_number, " and it's index is ",indexoflowestnumber)
    print("The highest number is ", highest_number, " and it's index is ",indexofhighestnumber)
        


def main():
   
    elements=[]
    print("enter 10 numbers")
    for n in range(1,11):
        numbers=int(input("Enter a number: "))
        elements.append(numbers)

    print(f"List of entered numbers: ,{elements}")

    IndexOfElements(elements)

main()