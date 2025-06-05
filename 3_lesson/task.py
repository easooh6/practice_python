import easyocr

reader = easyocr.Reader(['de'])
result = reader.readtext('images/de.png', detail=0)

print(result)