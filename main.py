#coding=<'utf-8'>

# Variable
variables = {}

# Opens file
fileToOpen = input('File : ')
file = open(fileToOpen,mode='r')
lines = file.readlines()
print(lines)

# LEXER

# Lexer functions
def makeInt(content):
	if 
	else:
		varValue = int(content[3])
		varName = content[1]
		variables[varName] = varValue

def makeFloat(content):
	varValue = float(content[3])
	varName = content[1]
	variables[varName] = varValue

def makeStr(content):
	varValue = content[3]
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
	if '+' in content:
		operationIndex = content.index('/')
		nums = content[operationIndex].split('+')
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
	if '-' in content:
		operationIndex = content.index('/')
		nums = content[operationIndex].split('-')
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
	if '*' in content:
		operationIndex = content.index('*')
		nums = content[operationIndex].split('*')
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
	if '/' in content:
		operationIndex = content.index('/')
		nums = content[operationIndex].split('/')
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

# Lexer main loop
for i in range(len(lines)):
	if '§' in lines[i]:
		codeLineStr = lines[i].split('§')
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