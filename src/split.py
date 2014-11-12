#coding=cp936
__author__ = 'luocheng'
filepath = '/home/cluo/summer2014/word2vec/corpus/sessionmerge.txt'
fout = open('../result/longsessions.txt','w')
count = 0

def overlap(item1, item2):
    all = set()
    c1 = set()
    c2 = set()
    for c in item1:
        all.add(c)
        c1.add(c)
    for c in item2:
        all.add(c)
        c2.add(c)
    if len(all) - len(c1) - len(c2)<-2:
        return True
    else:
        return False
def checkOverlap(lt):
    for i in range(0,len(lt)-1,1):
        if overlap(lt[i],lt[i+1]) ==True:
            continue
        else:
            return False
    return True

for l in open(filepath):
    count +=1
    if count %10000==0:
        print count
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
        if len(set(qlist))>=3:
            try:
                writen = set()
                towrite = list()
                for item in qlist:
                    if item not in writen:
                        towrite.append(item.decode('cp936').encode('utf8'))
                        writen.add(item)
                    else:
                        pass

            except:
                pass
            if len(towrite) >=3 and checkOverlap(towrite) == True:
                fout.write(','.join(towrite)+'\n')
        else:
            pass
            # print 'short 2',len(qlist)
fout.close()

