import random
rn_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','y','z']
rn_numbers=['0','1','2','3','4','5','6','7','8','9']
rn_symbols=['!','@','#','$','%','&','*','(',')','+']




print("welcome to the pypassword generaor!")
letters=int(input("how many letters would you like in your password?"))
print(letters )
symbols=int(input("how many symbols would you like?"))
print(symbols)
numbers=int(input("how many numbers would you like?"))

password_lst=[]
for char in range(0,letters):
    password_lst+=random.choice(rn_letters)
for char in range(0,symbols):
    password_lst+= random.choice(rn_symbols)
for char in range(0,numbers):
    password_lst+=random.choice(rn_numbers)
print(password_lst)
random.shuffle(password_lst) ## shuffle function to shuffle the list elements
print(password_lst)
password=""
for char in password_lst:
    password+=char
print(f"your password is:-{password}")