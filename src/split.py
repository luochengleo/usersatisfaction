#coding=cp936
__author__ = 'luocheng'
filepath = '/home/cluo/summer2014/word2vec/corpus/sessionmerge.txt'
fout = open('../result/longsessions.txt','w')
for l in open(filepath).readlines()[0:1000000]:
    segs = l.strip(' ')
    if len(segs)<5:
        continue
    else:
        qlist = list()
        for s in segs:
            if 'P@' in s:
                qlist.append(s.replace('P@',''))
        if len(qlist)>5:
            fout.write(' '.join([item.decode('cp936').encode('utf8') for item in qlist])+'\n')
fout.close()