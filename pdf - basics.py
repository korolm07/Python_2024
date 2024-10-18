import PyPDF2
f = open ('Working_Business_Proposal.pdf','rb') # read binary - it is not simple text file
pdf_reader = PyPDF2.PdfReader(f)
print (len(pdf_reader.pages))
page_one = pdf_reader.pages [0]
page_one_text = page_one.extract_text ()
#print (page_one_text)
f.close ()

f = open ('Working_Business_Proposal.pdf','rb')  
pdf_reader = PyPDF2.PdfReader(f)
first_page = pdf_reader.pages [0]
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(first_page)
pdf_output = open ('Some_BrandNew_Doc.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close ()
pdf_output.close ()


f = open('Working_Business_Proposal.pdf','rb')
pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)
for p in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[0]
    pdf_text.append(page.extract_text())
print(pdf_text[0])



f = open ('Find_the_Phone_Number.pdf','rb') 
pdf_reader = PyPDF2.PdfReader(f)
all_text = ""
for page in pdf_reader.pages:
    page_text = page.extract_text()  
    all_text = all_text+' '+page_text 

a = re.findall(r'\d{3}........', all_text)
print (a)
a = re.search(r'\d{3}.\d{3}.\d{4}', all_text)
print (a.group())