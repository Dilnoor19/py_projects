a = int(input("Enter The Number : "))

try:
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")

except:
    print("INVALID STATEMENT !!")