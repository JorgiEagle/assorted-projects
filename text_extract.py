article = open("newsarticle.txt", 'r', encoding="utf8")
shortened = open('newsarticleshort.txt', 'w')

arrayoffile = article.read()
printing = 1
count = 0
need_to_new_line = 0
for i in arrayoffile:
    if i=='<' or i =='{':
        printing = 0
    if printing:
        shortened.write(i)
        count+=1
        if (count%80 == 0):
            if i!=' ':
                need_to_new_line = 1
            else:
                shortened.write("\n")
            
    if i=='>' or i=='}':
        printing = 1


article.close()
shortened.close()
