alphabet = "abcdefghijklmnopqrstuvwxyz"
done = False


def encrypt():    
    plaintext = input ('Enter message ')
    cipher = '' 
    key = input ('Enter Key: ')
    key = int (key)
    for c in plaintext:
        if c in alphabet:
            cipher += alphabet [(alphabet.index(c)-key)%(len(alphabet))]
    print ('Your encrypted messege is ' + cipher)
   

def decrypt():
        plaintext = input ('Enter message for decryption ')
        key = 1
        decrypt = ''
        key = input ('Enter Key: ')
        key = int (key)        
        for c in plaintext:
            if c in alphabet:
                decrypt += alphabet [(alphabet.index(c)+key)%(len(alphabet))]
        print ('Your decrypted message is: ' + decrypt)
        


while not done:
    print ("\nWelcome to the Encryption Machine.\nPlease select an option from the list below.\nA. Encrypt.\nB. Decrypt.\nc. Quit.")
    choice = input(": ")
    
    if choice.lower() == "a":
        try: 
            encrypt()
        except:
            print ("Invalid Key")
            continue
        
    elif choice.lower() == "b":
        try: 
            decrypt()   
        except:
            print ("Invalid Key")
            continue
        
    elif choice.lower() == "c":
        done = True 