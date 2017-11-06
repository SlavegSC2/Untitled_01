from functions import keywords
keywords_dict = keywords(0.003)

wrds =[]
for items in keywords_dict:
    lst=[]
    theme = items[0]
    lst.append(theme)
    lst.append(keywords_dict.get(items))
    wrds.append(lst)

diction = {}
for list in wrds:
    for word in list[1]:
        new_diction = {word[0]:word[0]}
        diction.update(new_diction)
