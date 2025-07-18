import re
text="Hello my phone no is 123-456-7890"
pattern=r"\d{3}-\d{3}-\d{4}"

match =re.search(pattern,text)


if match:
    print(f"Found :{match.group()}")
    print(f"Position :{match.start()}-{match.end()}")
