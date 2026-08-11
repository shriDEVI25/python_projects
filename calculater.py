num1=float(input())
num2=float(input())

op=input("enter operator(+,-,*,/,%,^,//):")

if op=="+":
    print("result:",num1+num2)
elif op == "-":
    print("result:",num1-num2)
elif op == "*":
    print("result:",num1*num2)
elif op == "/":
    print("result:",num1/num2)
elif op == "%":
    print("result:",num1%num2)
elif op == "^":
    print("result:",num1^num2)
elif op == "//":
    print("result:",num1//num2)
else:
    print("invalid opearator")