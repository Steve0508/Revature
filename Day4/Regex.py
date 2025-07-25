import re
text= "Hello World"
pattern = r"Hello"


match =re.match(pattern,text)

if match:
    print("Match found at beginning")
else:
    print("No match at beginning")

    ######################

    #match entire string
text="123"
pattern=r"\d+"

if re.fullmatch(pattern,text):
    print("Entire string matches pattern")

        #############
text="Contact me at john@email.com or jane@example.org"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails=re.findall(pattern,text)
print(emails)


#replace matches
text="the data is 2023-12-25"
pattern=r"(\d{4})-(\d{2})-(\d{2})"
replacement= r"\2/\3/\1"

next_text=re.sub(pattern,replacement,text)
print(next_text)


#split string by pattern

text="apple,banana;orange:grape"
pattern=r"[,;:]"


parts=re.split(pattern,text)
print(parts)