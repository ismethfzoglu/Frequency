encoding = "utf-8-"
sentence =  "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

def frequency():
    words = dict()

    for i in sentence:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1

    for i, j  in words.items():
        print("{} : {} times mentioned in the sentence".format(i,j))



frequency()
