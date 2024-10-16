from PIL import Image
mask = Image.open ('mask.png') # this loads the image into Python as an Image object.
words_matrix = Image.open ('word_matrix.png')
print (mask.size)
print (words_matrix.size)
new_mask = mask.resize((1015,559))
new_mask.putalpha(200)
words_matrix.paste(new_mask,(0,0), new_mask) 
words_matrix.show ()
