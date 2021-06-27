from art import logo
import replit  #for Clean()
print(logo)

num_1=float(input('Whats your first number? '))
operator=input('\n+ add\n- substrac\n* multiplay\n/ divide\nSelect a operator: ')
operator_list=['+','-','*','/']
num_2=float(input('Whats your second number? '))
result=''
keep_calculating=True  #Flag
sum_total=''

while keep_calculating:
    def calculator(num_1,num_2):
        if operator == '+':
            sum_total= num_1+num_2
            return (f'{num_1} + {num_2} = {sum_total}')
        elif operator == '-':
            sum_total= num_1-num_2
            return (f'{num_1} - {num_2} = {sum_total}')    
        elif operator == '*':
            sum_total= num_1*num_2
            return (f'{num_1} * {num_2} = {sum_total}')      
        elif operator == '/':
            sum_total= num_1/num_2
            return (f'{num_1} / {num_2} = {sum_total}')  
calculator(num_1,num_2)
