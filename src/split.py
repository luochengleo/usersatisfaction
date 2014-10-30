#coding=cp936
__author__ = 'luocheng'
filepath = '/home/cluo/summer2014/word2vec/corpus/sessionmerge.txt'
fout = open('../result/longsessions.txt','w')
count = 0
for l in open(filepath):
    count +=1
    if count >= 1000000:
        break
    segs = l.strip().split(' ')
    if len(segs)<5:
        # print 'short 1',len(segs)
        continue
    else:
        qlist = list()
        for s in segs:
            if 'P@' in s:
                qlist.append(s.replace('P@',''))
        if len(set(qlist))>5:
            try:
                writen = set()
                for item in qlist:
                    if item not in writen:
                        fout.write(item.decode('cp936').encode('utf8') + ' ')
                        writen.add(item)
                    else:
                        pass
            except:
                pass
        else:
            pass
            # print 'short 2',len(qlist)
fout.close()