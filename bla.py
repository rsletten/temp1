import re

#pattern = r'^(?=.*\brequired1\b)(?=.*\brequired2\b)(?=.*\brequired3\b)(?=.*(\bextra\b)?(?!.*\bextra\b)).*$'
#pattern = r'^(?=.*\brequired1\b)(?=.*\brequired2\b)(?=.*\brequired3\b)(?=(?:.*\bextra\b)*).*$'
#pattern = r'^(?=.*\brequired1\b)(?=.*\brequired2\b)(?=.*\brequired3\b)(?=(?:.*\b\w+\b)*).*$'
pattern = r'^(?=.*\bvar1=\w+\b)(?=.*\bvar2=\w+\b)(?=.*\bvar3=\w+\b)(?=(?:.*\b\w+=\w+\b)*).*$'



texts = [
#    "required1 required2 required3 extra",
#    "required2 required3 required1 extra",
#    "extra required3 required1 required2 extra1",
#    "required3 required1 required2",
#    "extra required3 required2",
#    "extra"
    "var1=value1 var2=value2 var3=value3 var4=value4",
    "var3=value1 var4=value4 var1=value2 var2=value3",
    "var2=value2 var3=value3 var1=value1",
    "var3=value1 var1=value2 var2=value2",
    "var5=value5 var1=val1 var4=val4 var3=val3 var2=val2",
    "var5=value5 var6_bla=bla var1=val1 var4=val4 var3=val3 var2=val2",
    "var1=var4"
]

for text in texts:
    output = re.match(pattern, text)
    print(output)
