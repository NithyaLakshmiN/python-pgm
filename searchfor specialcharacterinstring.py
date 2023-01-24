import re

str = "Geeks4Geeks@#$&89%$435423423434"
regex = re.compile("[@#$&%!~]")

if regex.search(str) is None:
    print ("There are no special characters in the string")

else:
    print("There are special characters in the string")