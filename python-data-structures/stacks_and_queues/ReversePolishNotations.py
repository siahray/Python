#Evaluate Reverse Polish Notation (RPN)

#infix expression: 2 + 1 * 3
#postfix expression: 2 1 + 3 *

#We will use a stack to evaluate the RPN expression. We will iterate through each token in the expression and perform the following steps:

#If the token is a number, we will push it onto the stack. 

# If the token is an operator, we will pop the top two numbers from the stack, perform the operation, and push the result back onto the stack.

#-------------------------------------------------------------------------------------------------------------------

# this runs in 0(n) time and 0(n) space 

def eval_rpn(tokens):
    stack = []
    
    for token in tokens:
        print(f"Processing token: '{token}'")
        
        if token == "+":
            b, a = stack.pop(), stack.pop()
            result = a + b
            print(f"  -> Evaluating: {a} + {b} = {result}")
            stack.append(result)
            
        elif token == "-":
            b, a = stack.pop(), stack.pop()
            result = a - b
            print(f"  -> Evaluating: {a} - {b} = {result}")
            stack.append(result)
            
        elif token == "*":
            b, a = stack.pop(), stack.pop()
            result = a * b
            print(f"  -> Evaluating: {a} * {b} = {result}")
            stack.append(result)
            
        elif token == "/":
            b, a = stack.pop(), stack.pop()
            result = int(a / b)
            print(f"  -> Evaluating: {a} / {b} = {result}")
            stack.append(result)
            
        else:
            stack.append(int(token))
            print(f"  -> Pushed {token} to stack")
            
        # Print the current state of the stack after every operation
        print(f"Current Stack: {stack}\n")
            
    return stack.pop()

# Define the variables and run the test
test_tokens = ["2", "1", "+", "3", "*"]

print(f"Starting evaluation of: {test_tokens}")
print("-" * 40)

result = eval_rpn(test_tokens)

print("-" * 40)
print(f"The final result is: {result}")