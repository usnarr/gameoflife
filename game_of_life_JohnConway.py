dane=open('gra.txt','r').readlines()
for i in range(len(dane)):
    dane[i]=list(dane[i].rstrip())


def ewolucja(a,b):
    b=int(b)
    kopia=[]
    for i in a:
        kopia.append(i.copy())
    # print(kopia)
    for i in range(b):
        for w in range(12):
            for j in range(20):
                licznikzywych = 0

                if a[(w - 1) % 12][(j - 1) % 20] == 'X':
                    licznikzywych += 1
                if a[(w - 1) % 12][j % 20] == 'X':
                    licznikzywych += 1
                if a[(w - 1) % 12][(j + 1) % 20] == 'X':
                    licznikzywych += 1
                if a[w % 12][(j - 1) % 20] == 'X':
                    licznikzywych += 1
                if a[w % 12][(j + 1) % 20] == 'X':
                    licznikzywych += 1
                if a[(w + 1) % 12][(j - 1) % 20] == 'X':
                    licznikzywych += 1
                if a[(w + 1) % 12][j % 20] == 'X':
                    licznikzywych += 1
                if a[(w + 1) % 12][(j + 1) % 20] == 'X':
                    licznikzywych += 1


                if licznikzywych==3 and a[w][j]==".":
                    kopia[w][j]="X"
                if licznikzywych==3 or licznikzywych==2 and a[w][j]=="X":
                    kopia[w][j]="X"
                else:kopia[w][j]='.'
        for i in range(len(kopia)):
            a[i]=kopia[i].copy()
    return a

plansza=[i.copy() for i in dane]
plansza1=[i.copy() for i in dane]
 print(*i)



for i in range(1,100):
    plansza = [i.copy() for i in dane]
    plansza1 = [i.copy() for i in dane]

    plansza=ewolucja(plansza,i)
    plansza1=ewolucja(plansza1,i+1)
    if plansza==plansza1:
        print(i+2)
        break

piec0=(ewolucja([i.copy() for i in dane],50))
piec1=(ewolucja([i.copy() for i in dane],51))

for i in piec0:
    print(*i)
print()
for i in piec1:
    print(*i)








