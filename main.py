#coding=<'utf-8'>
from sys import argv

# Variable
variables = {}

# Opens file
if len(argv) > 1:
	fileToOpen = argv[1]
	file = open(fileToOpen,mode='r')
	lines = file.readlines()
	print(lines)

# LEXER

# Lexer functions
def makeInt(content):
	if content[3] == 'MATH':
		mathOutput = content.copy()
		del mathOutput[:3]
		content[3] = makeMath(mathOutput)
		varValue = int(content[3])
		varName = content[1]
		variables[varName] = varValue
	elif content[3] == 'INPUT':
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
	if content[3] == 'MATH':
		mathOutput = content.copy()
		del mathOutput[:3]
		content[3] = makeMath(mathOutput)
		varValue = float(content[3])
		varName = content[1]
		variables[varName] = varValue
	elif content[3] == 'INPUT':
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
	if content[3] == 'MATH':
		mathOutput = content.copy()
		del mathOutput[:3]
		content[3] = makeMath(mathOutput)
		varValue = str(content[3])
		varName = content[1]
		variables[varName] = varValue
	elif content[3] == 'INPUT':
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
	if content[3].lower() == 'true':
		varValue = True
	elif content[3].lower() == 'false':
		varValue = False
	varName = content[1]
	variables[varName] = varValue

def addition(content):
	if '+' in content[1]:
		nums = content[1].split('+')
		print(nums)
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
		return 'failure'

def substraction(content):
	if '-' in content[1]:
		nums = content[1].split('-')
		print(nums)
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
		return 'failure'

def multiplication(content):
	if '*' in content[1]:
		nums = content[1].split('*')
		print(nums)
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
		return 'failure'

def division(content):
	if '/' in content[1]:
		nums = content[1].split('/')
		print(nums)
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
		return 'failure'

def makeMath(content):
	result = addition(content)
	if result == 'failure':
		result = substraction(content)
		if result == 'failure':
			result = multiplication(content)
			if result == 'failure':
				result = division(content)
	return result

def xenonPrint(content):
	keys = list(variables.keys())
	for i in range(len(keys)):
		if keys[i] == content[1]:
			content[1] = variables[keys[i]]
	if content[1] == 'MATH':
		mathOutput = content.copy()
		del mathOutput[:1]
		content[1] = makeMath(mathOutput)
	stringInput = content[1:]
	output = ''
	for i in range(len(stringInput)):
		output += str(stringInput[i])
	print(output)

def xenonInput(content):
	stringInput = content[1:]
	output = ''
	for i in range(len(stringInput)):
		output += str(stringInput[i])
	result = input(output)
	return result

# Lexer main loop
for i in range(len(lines)):
	if '§' in lines[i]:
		codeLineStr = lines[i].split('§')
		if '\n' in codeLineStr:
			lineReturnIndex = codeLineStr.index('\n')
			del codeLineStr[lineReturnIndex]
		codeLine = codeLineStr[0].split(' ')
		while '' in codeLine:
			spaceIndex = codeLine.index('')
			del codeLine[spaceIndex]
		codeLine.append(codeLineStr[1])
		print(codeLine)
	else:
		codeLine = lines[i].split(' ')
		codeLine[-1] = codeLine[-1].rstrip('\n')
		print(codeLine)
	if codeLine[0] == 'INT':
		makeInt(codeLine)
		print(variables)
	elif codeLine[0] == 'FLOAT':
		makeFloat(codeLine)
		print(variables)
	elif codeLine[0] == 'STR':
		makeStr(codeLine)
		print(variables)
	elif codeLine[0] == 'BOOL':
		makeBool(codeLine)
		print(variables)
	elif codeLine[0] == 'MATH':
		print(makeMath(codeLine))
	elif codeLine[0] == 'PRINT':
		xenonPrint(codeLine)