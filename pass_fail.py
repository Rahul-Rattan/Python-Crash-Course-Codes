passed=0
failed=0

for i in range(1,11):
    n=int(input("Enter Results(1=pass, 2=fail): "))
    if n==1:
        passed+=1
    else:
        failed+=1

print("Passed = ", passed)
print("Failed = ", failed)
