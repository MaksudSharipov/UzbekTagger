import my_path
import xml.etree.ElementTree as et
import pos_tagger
import service_to_uzbek_text
import datetime

def run():
    entrs = my_path.read_text_files_name_from_dir("text")

    x = datetime.datetime.now()
    print("xml o`qib boshlandi: ", x.strftime("%H:%M:%S"))
    tree = et.parse('word.xml')
    root = tree.getroot()
    x = datetime.datetime.now()
    print("tugadi: ", x.strftime("%H:%M:%S"))

    for entr in entrs:
        x = datetime.datetime.now()
        print(entr, " file teglab boshlandi", x.strftime("%H:%M:%S"))

        # print(entr)
        a = open("text/" + entr, 'r', encoding='utf8')
        text = a.read()
        a.close()

        x = datetime.datetime.now()
        print("tokenlash boshlandi: ", x.strftime("%H:%M:%S"))


        tokens = service_to_uzbek_text.word_tokenizer(text)

        x = datetime.datetime.now()
        print("tokenlash tugadi: ", x.strftime("%H:%M:%S"))

        x = datetime.datetime.now()
        print("teglash boshlandi: ", x.strftime("%H:%M:%S"))

        a = pos_tagger.tagger(tokens, root)

        x = datetime.datetime.now()
        print("teglash tugadi: ", x.strftime("%H:%M:%S"))

        # print(type(a))
        for raw in a:
            # print(type(raw))
            text = text + "\n" + str(raw)

        x = datetime.datetime.now()
        print("natijani faylga yozish boshlandi: ", x.strftime("%H:%M:%S"))

        # text="\n".join(tuple(a))
        my_path.create_and_write_to_text_files("result", entr, text)

        x = datetime.datetime.now()
        print("yozish tugadi: ", x.strftime("%H:%M:%S"))

def analysis():
    entrs = my_path.read_text_files_name_from_dir("corpus")
    mylist=[]
    for entr in entrs:

        #print(entr)
        a = open("corpus/" + entr, 'r', encoding='utf8')
        text = a.read()
        a.close()

        tokens = service_to_uzbek_text.word_tokenizer(text)
        sent=service_to_uzbek_text.sent_tokenizer(text)
        mylist.append({'file':entr,'sent':len(sent),'token':len(tokens)})
    print(mylist)
    text=""
    for raw in mylist:

        text =text+ str(raw['file'][:-4])+' '+str(raw['sent'])+' '+str(raw['token'])+"\n"
    f = open("analysis_corpus", 'w', encoding='utf8')
    f.write(text)


#analysis()

