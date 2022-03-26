#shiraz yeshayahu 209086768
#A
def read_line(n, file):
    try:
        type(file)==str
        fhand = open(file)
            
        try: 
            type(n)==int
            count = 0                       
            for line in fhand:
                line = line.rstrip()
                count = count + 1
                if count == n:
                    return str(line)
                    break
            if count < n:
                return ("line " + str(n) + " doesn't exist")
        except:
                return "invalid input detected"
            
    except:
        return "file not found"
    

#B
import re

def longest_words(file): 
    try:
        type(file) == str
        handle = open(file) 
        dic = dict()
        for line in handle:
            res_line = re.sub(r'\W+|_', ' ', line) #Removes special characters that are not letters from a line
            words = res_line.split()
            for word in words:
                dic[word] =  dic.get(word,0) + 1
        
        #Inserting all the keys from dic into a new list we created by name key_list
        key_list = list(dic.keys())   
        key_list.sort(key=len, reverse=True) #key=len: Order by size from smallest to largest
                                   #reverse=True: Makes the order to be from the big to the small    
        return(list( key_list[:5]))
    except:
        return "file not found” and return an empty list."
