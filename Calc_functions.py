def InputNumber(textForInput):
### inputNumber gets number and check is it int or float or not a number
### returning number: 0=correct\1=incorrect, 
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
        return 1, 0
    
def ExecOperation(operationAsked, a, b):
### ExecutOperation
    Vars = {}
    operationExec = """res = {}""".format(operationAsked).replace("a", str(a)).replace("b", str(b))
    exec(operationExec, Vars)
    return 0, Vars['res']


def CheckOperation(operationInput):
    if operationInput == "+":
        return 0, "a+b"    
    elif operationInput == "-":
        return 0, "a-b"
    elif operationInput == "-a":
        return 0, "-a"
    elif operationInput == "%":
        return 0, "a%b"
    elif operationInput == "*":    
        return 0, "a*b"
    elif operationInput == "/":    
        return 0, "a/b"
    else:
        return 1, 0

def MainWorkflow():
### Later it would be main in module
    chooseOperation = input("Operation (+, -, -a, %, *, /): ")
    operationAsked = "" # nothing
    checkOperationValid, operationAsked = CheckOperation(chooseOperation)
    if checkOperationValid == 1:
        print("Wrong operation")
        return
    countNumbersInput = 0
    for x in operationAsked:
        if x in ["a", "b"]:
            countNumbersInput += 1
    print (countNumbersInput)
    a = 0
    res = 0
    checkNumberValid = 0
    checkNumberValid, res = InputNumber("Input first number: ")
    if checkNumberValid == 0:
        a = res
    else:
        print("a is not a number, Finish him")
        return 1, 0
    b = 0
    res = 0
    checkNumberValid = 0
    if countNumbersInput > 1:
        checkNumberValid, res = InputNumber("Input second number: ")
        if checkNumberValid == 0:
            b = res
        else:
            print("b is not a number, Finish him")
            return 1, 0
    checkOperationValid = 0
    checkOperationValid, result = ExecOperation(operationAsked, a, b)
    if checkOperationValid == 1:
        print("Wrong operation")
        return 1, 0
    print ("result of operation is: {}".format(str(result)))
    print ("end")
    return 0, result

MainWorkflow()
