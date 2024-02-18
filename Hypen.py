user_string = input("Enter a hypen-separaeted sequence of words :")
words = [word for word in user_string.split("-")]
words.sort()
print(words)
temp=""
for i in words:
    temp+=i
    if len(temp)>0:
        temp+="-"
print(temp[0:-1:1])
