'''
2.2 Feladat
Adott egy függvény. Értelmezési tartománya: [-3; 4] intervallumon az egész számok halmaza. Hozzárendelési szabálya: y = 2x-3.
A program egy lista formájában tárolja az értelmezési tartomány elemeit. Listaelemek leképezésével állítsa elő, tárolja listában és írja ki az értékkészlet elemeit.

A listaelemek leképezése az értelemezési tartomány nemnegatív elemire korlátozódjon!!!
'''

ertektar = [i for i in range(-3, 4)]
y = [2*i-3 for i in ertektar if i >= 0]
print(y)