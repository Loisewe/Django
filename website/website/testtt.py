path1='D:/htmltest .html'
cellnum1=30
cellvalue1=5

def Re_HTML(path,cellnum,cellvalue):
    a=[]
    with open(path,'r',encoding='utf-8',) as html:
        for line in html:
            # print(line)
            a.append(line)
    rowcounter=0
    cellcounter=0
    for i in range(len(a)):

        if '<tr>' in a[i]:
            rowcounter+=1
        if '<td>' in a[i] or '<th>' in a[i]:
            cellcounter+=1
            if cellcounter==cellnum:
                print('Было : ' + str((a[i])))
                a[i]='<td>' + str(cellvalue) + '</td>'
                print('Стало : ' + str((a[i])))

    with open(path,'w',encoding='utf-8',) as htmlw:
        for line in a:
            htmlw.writelines(line)

Re_HTML(path1,cellnum1,cellvalue1)
# print (rowcounter,cellcounter)
