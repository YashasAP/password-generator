import random
import string

print('Welcome to Password Generator!')

# asking user to input password length
length = int(input('Enter password length: '))  

# define data  
lower = string.ascii_lowercase   #'abcdefghijklmnopqrstuvwxyz'
upper = string.ascii_uppercase   #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = string.digits              #'0123456789'
symbols = string.punctuation     #'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# combine data
all = lower + upper + num + symbols

# use random  #sample() -->sample methods returns a list whith a randomely selection of specified number of items  
temp = random.sample(all,length)   

# create password   #list-->string 
password = "".join(temp)

# print password
print(password)