# # Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# # Coding:
# # if the word contains atleast 3 characters, remove the first letter and append it at the end
# #   now append three random characters at the starting and the end
# # else:
# #   simply reverse the string

# # Decoding:
# # if the word contains less than 3 characters, reverse it
# # else:
# #   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# # Your program should ask whether you want to code or decode





  


user_input=input("Enter a message- ")
demand_=int(input("""Enter 1 for coding 
Enter 2 for decoding."""))
if demand_==1:
    coding=True
elif demand_==2:
    coding=False
else:
    raise ValueError("Please enter either 1 or 2")
#logic starts 
if coding:
    new_message=[]
    words=user_input.split(" ")
    for input in words:
        if (len(input)>=3):
            newword="abc"+input[1:]+input[0]+"xyz"
            new_message.append(newword)
        else:
            newword=input[::-1]
            new_message.append(newword)
    print(" ".join(new_message))
else:
    new_message=[]
    words=user_input.split(" ")
    for input in words:
        if len(input)<=3:
            newword=input[::-1]
            new_message.append(newword)
        else:
            newword=input[-4]+input[3:-4]
            new_message.append(newword)
    print(" ".join(new_message))









