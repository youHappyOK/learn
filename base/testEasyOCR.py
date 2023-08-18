import easyocr

# this needs to run only once to load the model into memory
reader = easyocr.Reader(['ch_sim', 'en'])
result = reader.readtext('截图.png')
print(result)
