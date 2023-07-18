import os
def Newfolder():
    folder=r'C:\Users\hi\newkwli'
    list_of_files=os.listdir(folder)
    li_csv=['.csv','.pdf','.xlxs','.jpg']
    li_m=['.mp3','.mp4','.mpeg4','.wmv','.3gp','.webm']
    li1=[]
    li2=[]
    for i in list_of_files:
        for j in range(len(li_csv)):
            if i.endswith(li_csv[j]):
                li1.append(i)
        for k in range(len(li_m)):
            if i.endswith(li_m[k]):
                li2.append(i)
        
new=Newfolder()
    print(li1)
    print(li2)