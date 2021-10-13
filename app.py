import easyocr                                      #the library responsible for OCR 


image_path = 'download.png'                         # reading the image path 
reader = easyocr.Reader(['en'], gpu = False)        # choosing the English language and telling the programe that we are not using GPU 
result = reader.readtext(image_path, detail = 0)    # reading the text and removing the location details 
data = ' '.join(result)                             # collecting all th words in One string           
print(' '.join(result))
text_file = open("extracted_data.txt", "w")         # creating a text file in the same directory 
n = text_file.write(data)                           # writing the data in this file 
text_file.close()                                   # closing the file 
print(n)