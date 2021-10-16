def inputNumber(textForInput):
### inputNumber gets number and check is it int or float or not a number
    inputNum = input (textForInput)
    if inputNum.isnumeric():
        # print("toInt")
        inputNum = int(inputNum)
        return 0, inputNum
    elif inputNum.replace(",", ".", 1).replace(".", "", 1).isdigit():
        inputNum = float(inputNum.replace(",", ".", 1))
        # print("toFloat")
        return 0, inputNum
    else:
        #print("it is not a number")
        return 1
    



what = input("Operation (+, -, -a, %, *, /): ")
operationAsked = "" # nothing
if what == "+":
    operationAsked = "a+b"    
elif what == "-":
    operationAsked = "a-b"
elif what == "-a":
    operationAsked = "-a"
elif what == "%":
    operationAsked = "a%b"
elif what == "*":    
    operationAsked = "a*b"
elif what == "/":    
    operationAsked = "a/b"
else:
    print("Wrong operation")

countNumbersInput = 0
for x in operationAsked:
    if x in ["a", "b"]:
        countNumbersInput += 1
print (countNumbersInput)

a = 0
res = inputNumber("Input first number: ")
if res[0] == 0:
    a = res[1]
else: print("a is not a number, Finish him")

b = 0
if countNumbersInput > 1:
    resB = inputNumber("Input second number: ")
    if resB[0] == 0:
        b = resB[1]
    else: print("b is not a number, Finish him")


Vars = {}
operationExec = """res = {}""".format(operationAsked).replace("a", str(a)).replace("b", str(b))
exec(operationExec, Vars)

result = 0
result = Vars['res']
print ("result of operation is: {}".format(str(result)))
print ("end")

