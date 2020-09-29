# function to check string is
# palindrome or not
    # function to check string is
# palindrome or not
def ispalindrome(str):
    if len(str)<1:
        return True
    else:
        if str[0]==str[-1]:
            return ispalindrome(str[1:-1])
        else:
            return False
# main function
s=input("Please enter a string")
answer=ispalindrome(s)
if(answer==True):
    print("yes")
else:
    print("no")







# main function
s=input("Please enter a string")
answer=ispalindrome(s)
if(answer==True):
    print("yes")
else:
    print("no")
