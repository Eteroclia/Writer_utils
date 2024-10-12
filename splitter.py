import os,re

#open the master doc file and split it using the EOC (end of chapter) balise
f = open("master_doc.md", "r")
content = f.read()
chapters=content.split("EOC")
f.close()
#check how many split chapters exists
act_chap=len(os.listdir("./split_chapters"))

#for every chapter but the last
for chapter in chapters[:-1]:
    #remove the leading linejumps
    cleaned_chapter = "".join(re.findall(r"[\w\d ]+\n*", chapter))
    #if chapter is empty, jump it
    if(not len(cleaned_chapter)==0):
        
        #create the chapter file
        chap = open(f"./split_chapters/chapter_{act_chap+1}.md","w")
        act_chap+=1
        
        chap.write(cleaned_chapter)
        chap.close()

#clean the master_doc.md by writing only the last chapter
f = open("master_doc.md", "w")
f.write("".join(re.findall(r"[\w\d ]+\n*", chapters[-1])))
f.close()