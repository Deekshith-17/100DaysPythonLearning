def ispalindrome(word):
    for i in range(0,int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            return False
        return True
S=(input("Enter a name:"))
String=ispalindrome(S)
if (String):
    print("It is Palindrome")
else:
    print("It is Not a Palindrome")
    