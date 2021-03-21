#coding=<"utf-8">
from sys import argv
debug = False

# Variable
variables = {}

# Opens file
if len(argv) > 1:
	fileToOpen = argv[1]
	file = open(fileToOpen,mode="r")
	lines = file.readlines()
	if debug == True:print(lines)

# LEXER

# Lexer functions
def makeInt(content):
	if content[3] == "MATH":
		mathOutput = content.copy()
		del mathOutput[:3]
		content[3] = makeMath(mathOutput)
		varValue = int(content[3])
		varName = content[1]
		variables[varName] = varValue
	elif content[3] == "INPUT":
		output = content.copy()
		del output[:3]
		content[3] = xenonInput(output)
		varValue = int(content[3])
		varName = content[1]
		variables[varName] = varValue
	else:
		varValue = int(content[3])
		varName = content[1]
		variables[varName] = varValue

def makeFloat(content):
	if content[3] == "MATH":
		mathOutput = content.copy()
		del mathOutput[:3]
		content[3] = makeMath(mathOutput)
		varValue = float(content[3])
		varName = content[1]
		variables[varName] = varValue
	elif content[3] == "INPUT":
		output = content.copy()
		del output[:3]
		content[3] = xenonInput(output)
		varValue = float(content[3])
		varName = content[1]
		variables[varName] = varValue
	else:
		varValue = float(content[3])
		varName = content[1]
		variables[varName] = varValue

def makeStr(content):
	if content[3] == "MATH":
		mathOutput = content.copy()
		del mathOutput[:3]
		content[3] = makeMath(mathOutput)
		varValue = str(content[3])
		varName = content[1]
		variables[varName] = varValue
	elif content[3] == "INPUT":
		output = content.copy()
		del output[:3]
		content[3] = xenonInput(output)
		varValue = str(content[3])
		varName = content[1]
		variables[varName] = varValue
	else:
		varValue = str(content[3])
		varName = content[1]
		variables[varName] = varValue

def makeBool(content):
	if content[3].lower() == "true":
		varValue = True
	elif content[3].lower() == "false":
		varValue = False
	varName = content[1]
	variables[varName] = varValue

def addition(content):
	if "+" in content[1]:
		nums = content[1].split("+")
		if debug == True:print(nums)
		keys = list(variables.keys())
		for i in range(len(nums)):
			if nums[i] in keys:
				nums[i] = variables[nums[i]]
			elif nums[i] != int:
				nums[i] = int(nums[i])
		result = nums[0]
		for i in range(len(nums)-1):
			result += nums[i+1]
		return result
	else:
		return "failure"

def substraction(content):
	if "-" in content[1]:
		nums = content[1].split("-")
		if debug == True:print(nums)
		keys = list(variables.keys())
		for i in range(len(nums)):
			if nums[i] in keys:
				nums[i] = variables[nums[i]]
			elif nums[i] != int:
				nums[i] = int(nums[i])
		result = nums[0]
		for i in range(len(nums)-1):
			result -= nums[i+1]
		return result
	else:
		return "failure"

def multiplication(content):
	if "*" in content[1]:
		nums = content[1].split("*")
		if debug == True:print(nums)
		keys = list(variables.keys())
		for i in range(len(nums)):
			if nums[i] in keys:
				nums[i] = variables[nums[i]]
			elif nums[i] != int:
				nums[i] = int(nums[i])
		result = nums[0]
		for i in range(len(nums)-1):
			result *= nums[i+1]
		return result
	else:
		return "failure"

def division(content):
	if "/" in content[1]:
		nums = content[1].split("/")
		if debug == True:print(nums)
		keys = list(variables.keys())
		for i in range(len(nums)):
			if nums[i] in keys:
				nums[i] = variables[nums[i]]
			elif nums[i] != int:
				nums[i] = int(nums[i])
		result = nums[0]
		for i in range(len(nums)-1):
			result /= nums[i+1]
		return result
	else:
		return "failure"

def makeMath(content):
	result = addition(content)
	if result == "failure":
		result = substraction(content)
		if result == "failure":
			result = multiplication(content)
			if result == "failure":
				result = division(content)
	return result

def xenonPrint(content):
	keys = list(variables.keys())
	output = ""
	if content[1] == "MATH":
		mathOutput = content.copy()
		del mathOutput[:1]
		content[1] = makeMath(mathOutput)
		output = content[1]
	elif "#" in content[1]:
		stringInput = content[1].split("#")
		for i in range(len(keys)):
			for x in range(len(stringInput)):
				if keys[i] == stringInput[x]:
					stringInput[x] = variables[keys[i]]
		for i in range(len(stringInput)):
			output += stringInput[i]
	else:
		for i in range(len(keys)):
			if keys[i] == content[1]:
				content[1] = variables[keys[i]]
		output = content[1]
	print(output)

def xenonInput(content):
	stringInput = content[1:]
	output = ""
	for i in range(len(stringInput)):
		output += str(stringInput[i])
	result = input(output)
	return result

def xenonIf(content):
	keys = list(variables.keys())
	for i in range(len(content)):
		for x in range(len(keys)):
			if content[i] == keys[x]:
				content[i] = variables[keys[x]]
	if content[2] == "==":
		if content[1] == content[3]:
			result = True
		else:
			result = False
	elif content[2] == "!=":
		if content[1] != content[3]:
			result = True
		else:
			result = False
	if result == True:
		return 0
	else:
		return 1

# Lexer main loop
ifIfCondition = 0
for i in range(len(lines)):
	if "<<" in lines[i]:
		codeLineStr = lines[i].split("<<")
		if "\n" in codeLineStr:
			lineReturnIndex = codeLineStr.index("\n")
			del codeLineStr[lineReturnIndex]
		codeLine = codeLineStr[0].split(" ")
		while "" in codeLine:
			spaceIndex = codeLine.index("")
			del codeLine[spaceIndex]
		codeLineStr2 = codeLineStr[1:]
		for i in range(len(codeLineStr2)):
			codeLine.append(codeLineStr2[i])
		if debug == True:print(codeLine)
	else:
		codeLine = lines[i].split(" ")
		codeLine[-1] = codeLine[-1].rstrip("\n")
		if debug == True:print(codeLine)
	if "\t" in codeLine[0]:
		codeLine[0] = codeLine[0].strip("\t")
	if ifIfCondition == 0:
		if codeLine[0] == "INT":
			makeInt(codeLine)
			if debug == True:print(variables)
		elif codeLine[0] == "FLOAT":
			makeFloat(codeLine)
			if debug == True:print(variables)
		elif codeLine[0] == "STR":
			makeStr(codeLine)
			if debug == True:print(variables)
		elif codeLine[0] == "BOOL":
			makeBool(codeLine)
			if debug == True:print(variables)
		elif codeLine[0] == "MATH":
			if debug == True:print(makeMath(codeLine))
		elif codeLine[0] == "PRINT":
			xenonPrint(codeLine)
	if codeLine[0] == "IF":
		ifIfCondition = xenonIf(codeLine)
	elif codeLine[0] == "ELIF":
		if ifIfCondition == 1:
			ifIfCondition = 0
			ifIfCondition = xenonIf(codeLine)
		elif ifIfCondition == 0:
			ifIfCondition = 2
	elif codeLine[0] == "ELSE":
		if ifIfCondition == 1:
			ifIfCondition = 0
		else:
			ifIfCondition = 1
	elif codeLine[0] == "END":
		ifIfCondition = 0
	if debug == True:print("ifIfCondition:",ifIfCondition)