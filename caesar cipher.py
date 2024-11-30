# task: caesar cipher
# plaintext - p 
# key - k

def caesar(p,k):
    encrypted = ""
    for char in p:
        if char.isalpha(): 
            shift = k % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted += new_char
        else:
            encrypted += char  
    return encrypted

# Example usage
print("***CAESAR'S CIPHER***")
plaintext = input("enter text that you want to cipher: ")
key = 3
ciphertext = caesar(plaintext, key)
print("Encrypted:", ciphertext)





