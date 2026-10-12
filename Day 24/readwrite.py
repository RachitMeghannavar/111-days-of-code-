#Raeding
#First way
# file = open("text.txt","r")
# content = file.read()
# print(content)
# file.close()

#Second way
# with open("text.txt","r") as file:
#     content = file.read()
#     print(content)

#Writing
# #if writing to the existing file it will be over written
# with open("text.txt","w") as file:
#     file.write("Hello World \nHello python \nHello Rachit")

# if there is no file it will created in write mode
# with open("Rachit.txt" , "w") as file:
#     file.write("Hello World")

#Append
with open("Rachit.txt" , "a") as file:
    file.write("\nHello Rachit")