import pandas as pd
import xml.etree.cElementTree as et

print("Hello world!")
root=et.Element("dictionary")

#Sifat
excel_data = pd.read_excel('excel/sifat.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='ADJ', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='ADJ', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()


#Son
excel_data = pd.read_excel('excel/son.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='NUM', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='NUM', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()


#Fel
excel_data = pd.read_excel('excel/fel.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='VERB', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='VERB', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()



#Ravish
excel_data = pd.read_excel('excel/ravish.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='ADV', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='ADV', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()

#Ot
excel_data = pd.read_excel('excel/ot.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='NOUN', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].lower().strip()
    else:
        et.SubElement(root, "word", classId='NOUN', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).lower().strip()

#Yordamchi so`zlar
excel_data = pd.read_excel('excel/olmosh.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='PRON', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='PRON', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()


#Yordamchi so`zlar
excel_data = pd.read_excel('excel/yordamchi.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if (data['property'][i]=='K'):
        if '*' in data['word'][i]:
            et.SubElement(root, "word", classId='AUX', id=str(id), changeClass="*",
                          property="").text = str(data['word'][i])[:-1].strip()
        else:
            et.SubElement(root, "word", classId='AUX', id=str(id), changeClass="",
                          property="").text = str(data['word'][i]).strip()
    if (data['property'][i]=='M'):
        if '*' in data['word'][i]:
            et.SubElement(root, "word", classId='MOD', id=str(id), changeClass="*",
                          property="").text = str(data['word'][i])[:-1].strip()
        else:
            et.SubElement(root, "word", classId='MOD', id=str(id), changeClass="",
                          property="").text = str(data['word'][i]).strip()
    if (data['property'][i]=='B'):
        if '*' in data['word'][i]:
            et.SubElement(root, "word", classId='CONJ', id=str(id), changeClass="*",
                          property="").text = str(data['word'][i])[:-1].strip()
        else:
            et.SubElement(root, "word", classId='CONJ', id=str(id), changeClass="",
                          property="").text = str(data['word'][i]).strip()
    if (data['property'][i]=='Y'):
        if '*' in data['word'][i]:
            et.SubElement(root, "word", classId='PART', id=str(id), changeClass="*",
                          property="").text = str(data['word'][i])[:-1].strip()
        else:
            et.SubElement(root, "word", classId='PART', id=str(id), changeClass="",
                          property="").text = str(data['word'][i]).strip()
    if (data['property'][i]=='U'):
        if '*' in data['word'][i]:
            et.SubElement(root, "word", classId='INTJ', id=str(id), changeClass="*",
                          property="").text = str(data['word'][i])[:-1].strip()
        else:
            et.SubElement(root, "word", classId='INTJ', id=str(id), changeClass="",
                          property="").text = str(data['word'][i]).strip()
    if (data['property'][i]=='T'):
        if '*' in data['word'][i]:
            et.SubElement(root, "word", classId='IMIT', id=str(id), changeClass="*",
                          property="").text = str(data['word'][i])[:-1].strip()
        else:
            et.SubElement(root, "word", classId='IMIT', id=str(id), changeClass="",
                          property="").text = str(data['word'][i]).strip()


#faylga yozish
tree = et.ElementTree(root)
tree.write("word.xml", xml_declaration=True, encoding='utf-8')
print(id)