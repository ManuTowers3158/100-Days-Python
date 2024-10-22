# This script checks if a given string is a palindrome (reads the same forward and backward) by comparing characters in reverse.
# The second function uses recursion to determine if the word is a palindrome.

print("*************Palindromos***************")
palindromo = input("Jefe Maestro ponga aqui su palindromo\n>>> ").lower().strip().replace(" ", "")  # Get input, remove spaces, and convert to lowercase
print(palindromo)

array1 = []  # Initialize an empty list for the original word
array2 = []  # Initialize an empty list for the reversed word

# Populate array1 with each character from the input string
for i in palindromo:
    array1.append(i)
print(array1)  # Debugging print to check array1

length_pal = len(palindromo)  # Get the length of the palindrome
length_aux = length_pal - 1   # Initialize a helper variable to reverse the array

# Populate array2 with the characters of array1 in reverse order
for i in range(length_pal):
    array2.append(array1[length_aux])  # Add characters in reverse
    length_aux = length_aux - 1
print(array2)  # Debugging print to check array2 (reversed string)

# Check if the original and reversed arrays are the same
flag = True  # Initialize a flag for palindrome check
for i in range(length_pal):
    if array1[i] != array2[i]:  # If any characters don't match, it's not a palindrome
        flag = False

# Output the result
if flag == True:
    print("Jefe esto en efecto es un palindromo")  # The input is a palindrome
else:
    print("Jefe esto no es un palindromo")  # The input is not a palindrome

# Alternative solution using recursion to check palindrome
def palindrome(word):
    if len(word) <= 1:  # Base case: if the word is 1 character or empty, it's a palindrome
        return True
    if word[0] != word[-1]:  # Check if the first and last characters are different
        return False  # If different, it's not a palindrome
    return palindrome(word[1:-1])  # Recursively check the inner substring
