# a  = 10

# b = 0
# print("hiii learning exception")
# print(a/b)

# print("after excution of a/b")


# try:
#     a = 10
#     b = 0
#     print(a/b)
# except:
#     print("can not divide with zeor")

# print("hii after exception hadling")
# print("hiii this is second line after writing code")

# try:
#     number = int(input("enter a number"))

#     print(10/number)
# except ValueError:
#     print("enter a valid number")
# except ZeroDivisionError:
#     print("you can not divide with zero")
# else:
#     print("all went well") #executed only when exception  ocurred
# finally:
#     print("i am in finally block")   # wheather exception occured or not it will excuted


# print("finishing")

age = int(input("enter your age"))

if age <18:
    raise ValueError("age must be above 18")
else:
    print("all good")
print("working or not")

