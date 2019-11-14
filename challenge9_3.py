import csv

ll = []
ll.append(['Top Gun', 'Risky Business', 'Minority Report'])
ll.append(['Titanic', 'The Revenant', 'Inception'])
ll.append(['Training Day', 'Man on Fire', 'Flight'])

with open('tom.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter =',')
    for l in ll:
        w.writerow(l)

ll = []
ll.append(['トップガン', 'リスキービジネス', 'マイノリティー・リポート'])
ll.append(['タイタニック', 'レブナント', 'インセプション'])
ll.append(['トレーニング・デイ', 'マンオブファイヤ', 'フライト'])

with open('トム.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter =',')
    for l in ll:
        w.writerow(l)
        
