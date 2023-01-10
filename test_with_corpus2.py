import my_path
import xml.etree.ElementTree as et
import pos_tagger
import service_to_uzbek_text



def run():
    entrs = my_path.read_text_files_name_from_dir("corpus")

    tree = et.parse('word.xml')
    root = tree.getroot()

    for entr in entrs:

        print(entr)
        a = open("corpus/" + entr, 'r', encoding='utf8')
        text = a.read()
        a.close()

        tagged_text=""

        sentences=service_to_uzbek_text.sent_tokenizer(text)
        print(sentences)

        for sent in sentences:
            punk=sent[-1]
            tagged_sent=""
            tokens = service_to_uzbek_text.word_tokenizer(sent)
            tagged_list=pos_tagger.pos.tagger(tokens,root)
            print(tagged_list)
            for i in range(len(tagged_list)):

                tagged_sent=tagged_sent+' '+tagged_list[i]['word']+'/'+tagged_list[i]['pos']
            tagged_sent=tagged_sent+' '+punk+'/PUNCT\n'
            tagged_text=tagged_text+tagged_sent
            print(tagged_sent)
        my_path.create_and_write_to_text_files("result", entr, tagged_text)


run()

