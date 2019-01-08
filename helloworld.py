# This is hello world from function. This is only function definition. The code will not be executed until the function is called.
def printFunction():
	print('hello from function')
	
def secondFunction():
	print('second function printing')

# -------- What is below this line is similar to main() function in c
# The following code is equivaled to:
# int main() {
#	printf("Hello world");
#  printFunction();
#  secondFunction();
# }
#
# first line of execution.
print ('Hello world')
# second line of execution. This will be called after the first line prints hello workd.
printFunction()
secondFunction()