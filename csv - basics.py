import csv
data = open ('example.csv', encoding= 'utf-8')
csv_data = csv.reader (data)
data_lines = list (csv_data)
print (data_lines[0])
print (len (data_lines))

for line in data_lines [:5]:
    print (line)

print (data_lines[10][3])
all_emails = []
for line in data_lines [1:5]:
    all_emails.append(line[3])
print (all_emails)

file_to_output = open ("to_save_file.csv", mode = 'w', newline = '')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()

f = open ("to_save_file.csv", mode = 'a', newline = '') # a means I just want append to existing file 
csv_writer = csv.writer(f)
csv_writer.writerow (['1','2','3'])

data = open ('find_the_link.csv', encoding= 'utf-8')
csv_data = csv.reader (data)
data_lines = list (csv_data)
word = []
for line in data_lines:
    if line:  # Check if the line is not empty
        for item in line: 
            a = re.search(r'\D', item)  
            if a:
                word.append(a.group())
word = ''.join(word)
print (word.replace (' ', ''))