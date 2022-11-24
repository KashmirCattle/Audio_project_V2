import json

def initial_bst_add(kary_json_path, bst_json_path, General_transcript_json):
    complete_list = []
    conb_list = []

    # with open('The_wizard_man/comb.json', 'r') as f: #adds words in conb.json to "conb_list"  (sly combined words json)
    #     data = json.load(f)
    #     for item in data:
    #         conb_list.append(item)

    # def add_comb_word(word):

    #     dictt = {}
    #     dictt['word'] = word
    #     dictt['conb'] = True
    #     complete_list.append(dictt)


    with open(kary_json_path) as f: #find best for each wor in "love again"
        data = json.load(f)

        with open(General_transcript_json) as f:
            events = json.load(f)

            for item in data['result']:
                word = item['word']
                somelist = [x for x in events['result'] if not (x['word'] != word)] 
                    # print(item)
                if word in conb_list:
                    # add_comb_word(word)
                    input('ERROR')
                else:
                    try:
                        best = max(somelist, key=lambda ev: ev['conf'])
                        complete_list.append(best)
                    except:
                        complete_list.append('NULL_COULD_NOT_FIND: '+word)


    with open(bst_json_path, 'w') as f:  #BST json file
        json.dump(complete_list, f, indent=2)   