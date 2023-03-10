import service_to_uzbek_text

class pos:
    def __double_words(a):

        a = list(a)
        verb = ["edi", "ekan", "emish"]
        l1 = len(a)
        l2 = len(verb)
        i = 0
        while (i < l1 - 1):
            for j in range(l2):
                if (a[i + 1]["word"] == verb[j]):
                    b = True
                    if ((a[i]["root"] == "null") and (a[i + 1]["root"] == "null")):
                        a[i]["root"] = a[i]["word"] + " " + a[i + 1]["word"]
                    elif (a[i]["root"] == "null"):
                        a[i]["root"] = a[i]["word"] + " " + a[i + 1]["root"]
                    elif (a[i + 1]["root"] == "null"):
                        a[i]["root"] = a[i]["root"] + " " + a[i + 1]["word"]
                    else:
                        a[i]["root"] = a[i]["root"] + " " + a[i + 1]["root"]

                    a[i]["word"] = a[i]["word"] + " " + a[i + 1]["word"]
                    a[i]["pos"] = "VERB"
                    print(a[i])
                    a.pop(i + 1)
                    i = i - 1
                    l1 = len(a)
            i = i + 1

        return a

    def __check_with_affix(a):
        #a = list(a)
        verb = ['di', 'lan','lash','lashtir','lantir','lantirdi']
        noun = ['lig', 'lik', 'vchi']
        for v in verb:
            if (v in a["affix"]):
                if (a['pos'] == 'VERB'):
                    break
                else:
                    a['pos'] = 'VERB'
                    return a
        for v in noun:
            if (v in a["affix"]):
                if (a['pos'] == 'NOUN'):
                    break
                else:
                    a['pos'] = 'NOUN'
        return a

    def __tag_word(a, root):

        if (str(a['word']).isdigit()):
            a['pos'] = 'NUM'
            a['root'] = a['word']
            return a

        a = dict(a)
        for dic in root:
            s = dic.text
            if ((dic.attrib["classId"] == "VERB") and ("moq" in s[-3:])):
                s = str(dic.text[:-3])
            s = service_to_uzbek_text.word_normalizer(s)

            l = len(s)
            if ((s == a["word"][:l].lower()) and (len(s) > 1) or (s == a["word"][:l].lower()) and (s == 'u')):
                if (a['root'] == "null"):
                    a["pos"] = str(dic.attrib["classId"])
                    a["root"] = s
                    a["affix"] = a["word"][l:]
                elif (l > len(a["root"])):
                    a["pos"] = str(dic.attrib["classId"])
                    a["root"] = s
                    a["affix"] = a["word"][l:]
        return a

#    import xml.etree.ElementTree as et
#    tree = et.parse('word.xml')
#    root = tree.getroot()

    def __check_with_lar(a, root):
        if(len(a['affix'])==0):
            return a

        if (str(a['root'])[-2:] == 'la') and (str(a['affix'])[0] == 'r'):
            b = {'word': a['root'][:-1], 'pos': "null", 'root': 'null', 'affix': 'null'}
            b = pos.__tag_word(b, root)
            if not (b['root'] == 'null'):
                a['pos'] = b['pos']
                a['root'] = b['root']
                a['affix'] = b['affix'] + 'a' + a['affix']
        return a

    # print(__check_with_lar({'word':'vakillari','pos':'fel','root':'vakilla', 'affix':'ri'},root))

    def tagger(tokens, root):

        a = []

        for token in tokens:
            a.append({'word': str(token), "pos": "null", "root": "null", "affix": "null"})

        for i in range(len(a)):
            a[i] = pos.__tag_word(a[i], root)
            a[i]=pos.__check_with_lar(a[i],root)
            a[i]=pos.__check_with_affix(a[i])
        a = pos.__double_words(a)
        #print(a)

        return a
