#functions: search, findall, finditer
text = "the agent phone num is 11-22-333, another phone: 12344"
import re
pattern = 'phone'
a = re.search (pattern,text)
print (a)
pattern1 = 'wrong text'
b = re.search (pattern1, text)
print (b)
print (a.span())
print (a.start())
print (a.end())
allmatches = re.findall ('phone', text)
print (len(allmatches))

for match in re.finditer('phone',text):
    print (match.span())
for match in re.finditer('phone',text):
    print (match.group()) # retursn actual peace of match

d = re.search (r'\d\d-\d\d-\d\d\d', text) # r means to tell Python we use \ for reg expressions, not smth else
print (d)

e = re.search (r'\d{2}-\d{2}-\d{3}', text) # {} quantifier
print (f"this is group: {e.group()}")

phone_pattern = re.compile (r'(\d{2})-(\d{2})-(\d{3})') 
results = re.search (phone_pattern, text)
print (results.group (2)) #compile helps to take specific part of info, for ex. number and its city code  

#Or operator |
t = re.search (r"cat|dog", "the cat is here")
print (t)
k = re.findall (r"...at", "the cats in the hat sat at the table")  # if to add . it will print actual letter before at, = wild card
print (k)

re.findall (r"^\d", '1 is the num') #string I search starts from num. Whole string, so for "the nume 1 is the first" - wil not work
# dollar sign means end with

phrase = "there are 3 num 34 inside 5 inside sentence"
pattern = r'[^\d]+'  # 	Returns a match for any character EXCEPT ^d, + connects all letters together
g = re.findall (pattern, phrase)
print (g)

test_phrase = "this is a string! But it has punctuation... how to remove it??"
k = re.findall (r"\w+", test_phrase)
clean = " ".join(k)
print (clean)

text = 'only find the hypen-words in this sentence. But you dont know how long-ish they are. hahah-'
z = re.findall (r'[\w]+-[\w+]', text)  #[] clean way to combine groups, easier to read and later can be used as groups 
print (z)

text1 = 'hello, would you like catfish?'
text2 = 'hello, would you like catnap?'
text3 = 'hello, would you like caterpillar?'
j = re.search(r'cat(fish|nap)', text1)
print (j)
