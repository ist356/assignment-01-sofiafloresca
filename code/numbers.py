'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''

even = []
odd = []
num_dict = {'odd': odd, 'even': even}
num = int(input("Enter an integer value: "))
while num != 0:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    num = int(input("Enter an integer value: "))
print(num_dict)

