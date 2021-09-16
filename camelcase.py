import re


def main():
    to_check = True
    while  to_check:
        sentence = str(input("Enter a sentence use only letters "))

        # from automate the boring stuff book
        # and from # from https://www.guru99.com/python-regular-expressions-complete-tutorial.html
        check = re.match(r'[\d\W]', sentence)
    
        if check: 
            to_check = False
            
        return sentence
        

    

def camel_case(sentence): 
    if sentence == '':
        return ''
    
    sentence = sentence.lower()
    listWords = []
    
    split = sentence.split(' ')
    
    no_line = []
    for word in split:
        length = len(word)
        x = word[0].upper()
        listWords.append(x + word[1:length])
        
    # from https://www.delftstack.com/howto/python/python-remove-newline-from-string/
    for x in listWords:
        no_line.append(x.replace("\\n", ""))
    
    #to_check = False
    # from https://www.geeksforgeeks.org/python-string-join-method/
    words = "".join(no_line)
   # https://www.geeksforgeeks.org/filter-in-python/
    
   
    return words  

def main():
    to_check = True
    while  to_check:
        sentence = str(input("Enter a sentence use only letters "))

        # from automate the boring stuff book
        # and from # from https://www.guru99.com/python-regular-expressions-complete-tutorial.html
        check = re.match(r'[\d\W]', sentence)
    
        if not check: 
            
            to_check = False
            
       # return sentence 
        end_sentence = camel_case(sentence)
        print(end_sentence) 

if __name__ == '__main__':
    main()
        


