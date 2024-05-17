import re
txt="The train in spain"
x=re.findall("in",txt)
print(len(x))