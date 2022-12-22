import service_to_uzbek_text

import datetime

def __double_words(a):
    a=list(a)
    verb=["edi", "ekan","emish"]
    l1=len(a)
    l2=len(verb)
    i=0
    while(i<l1-1):
        for j in range(l2):
            if(a[i+1]["word"]==verb[j]):
                b = True
                if((a[i]["root"]=="null") and (a[i+1]["root"]=="null")):
                    a[i]["root"] = a[i]["word"] + " " + a[i+1]["word"]
                elif(a[i]["root"]=="null"):
                    a[i]["root"] = a[i]["word"] + " " + a[i+1]["root"]
                elif (a[i+1]["root"] == "null"):
                    a[i]["root"] = a[i]["root"] + " " + a[i+1]["word"]
                else:
                    a[i]["root"] = a[i]["root"] + " " + a[i+1]["root"]

                a[i]["word"] = a[i]["word"] + " " + a[i+1]["word"]
                a[i]["pos"]="fel"
                print(a[i])
                a.pop(i+1)
                i=i-1
                l1=len(a)
        i=i+1

    return a

def __check_with_lar(root,affix):
    pass

def __check_with_affix(a):
    a=list(a)
    verb=['di','lan']
    noun=['lig','lik','vchi']


def tagger(tokens,root):

    a = []

    for token in tokens:
        a.append({'word': str(token), "pos": "null", "root": "null"})

    for i in range(len(a)):
        #x = datetime.datetime.now()
        #print(i," sozini teglash boshlandi: ",x.strftime("%H:%M:%S"))
        for dic in root:
            s = dic.text

            if ((dic.attrib["classId"] == "fel") and ("moq" in s[-3:])):
                s = str(dic.text[:-3])

            s=service_to_uzbek_text.word_normalizer(s)

            l = len(s)

            if ((s == a[i]["word"][:l])and(len(s)>1) or (s == a[i]["word"][:l])and(s =='u')):
                if (a[i]['root'] == "null"):
                    a[i]["pos"] = str(dic.attrib["classId"])
                    a[i]["root"] = s
                elif (l > len(a[i]["root"])):
                    a[i]["pos"] = str(dic.attrib["classId"])
                    a[i]["root"] = s

        #x = datetime.datetime.now()
        #print(i, " sozini teglash tugadi: ", x.strftime("%H:%M:%S"))
    a=__double_words(a)
    print(a)

    return a