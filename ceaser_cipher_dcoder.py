def encryption():

    letters = ['_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.','!']

   
    cypher = input("type cypher text: ")
    #key = int(input("Enter Key: "))
    #result = ''
    
    for key in range(0,29):
        
        result = ''
        for i in cypher:

            if i in letters:
                indx = letters.index(i)
                new_indx = (indx - key) % 29
                new_letter = letters[new_indx]
                result += new_letter
            else:
                pass

        print(result)
    
    #print(f"Your decrypted message is: {result}")

encryption()

