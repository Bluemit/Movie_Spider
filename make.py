
fout=open('3.txt','w')
i=1
j=1
strs='http://www.cbooo.cn/boxOffice/getWeekInfoData?sdate=2015-'
while i<10:
    j=1
    while j<10:
        strs='http://www.cbooo.cn/boxOffice/getWeekInfoData?sdate=2015-'
        strs=strs + '0'+str(i)+'-0'+str(j)
        fout.write(strs+'\n')
        j+=1
    while j<=31:
        strs='http://www.cbooo.cn/boxOffice/getWeekInfoData?sdate=2015-'
        strs=strs + '0'+str(i)+'-'+str(j)
        fout.write(strs+'\n')
        j+=1
    i+=1
while i<=12:
    j=1
    while j<10:
        strs='http://www.cbooo.cn/boxOffice/getWeekInfoData?sdate=2015-'
        strs=strs +str(i)+'-0'+str(j)
        fout.write(strs+'\n')
        j+=1
    while j<=31:
        strs='http://www.cbooo.cn/boxOffice/getWeekInfoData?sdate=2015-'
        strs=strs + str(i)+'-'+str(j)
        fout.write(strs+'\n')
        j+=1
    i+=1
