with open("air.txt", 'r') as file:
    news = file.read()
    news = news.replace("\n", "").replace(",", "").replace(".", "").replace(' ','')
    marks = list(news)
   
    
def get_dict(marks):
    dict_1 = {}
 
    for mark in marks:
        if mark in dict_1:
            dict_1[mark] = dict_1[mark] + 1
        else:
            dict_1[mark] = 1
    return dict_1


dict_1 = get_dict(marks)
maximum = max(dict_1.values())
dict_2 = {k:v for k, v in dict_1.items() if v == maximum}
print(dict_1)    
print(dict_2)

