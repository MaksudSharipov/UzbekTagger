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
        et.SubElement(root,"word", classId='sifat', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='sifat', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()


#Son
excel_data = pd.read_excel('excel/son.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='son', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='son', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()


#Fel
excel_data = pd.read_excel('excel/fel.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='fel', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='fel', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()



#Ravish
excel_data = pd.read_excel('excel/ravish.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='ravish', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='ravish', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()

#Ot
excel_data = pd.read_excel('excel/ot.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='ot', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].lower().strip()
    else:
        et.SubElement(root, "word", classId='ot', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).lower().strip()

#Yordamchi so`zlar
excel_data = pd.read_excel('excel/olmosh.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='olmosh', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='olmosh', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()


#Yordamchi so`zlar
excel_data = pd.read_excel('excel/yordamchi.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='yordamchi soz', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='yordamchi soz', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()

#Oraliq so`zlar
excel_data = pd.read_excel('excel/oraliq.xlsx')
data = pd.DataFrame(excel_data, columns=['word', 'property'])
id=0
l=len(data)
for i in range(l):
    id=id+1
    if '*' in data['word'][i]:
        et.SubElement(root,"word", classId='oraliq soz', id=str(id), changeClass="*",
                      property=str(data['property'][i])).text=str(data['word'][i])[:-1].strip()
    else:
        et.SubElement(root, "word", classId='oraliq soz', id=str(id), changeClass="",
                      property=str(data['property'][i])).text = str(data['word'][i]).strip()

#faylga yozish
tree = et.ElementTree(root)
tree.write("word.xml", xml_declaration=True, encoding='utf-8')
