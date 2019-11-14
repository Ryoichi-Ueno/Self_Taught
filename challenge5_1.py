fa = ['Kygo', 'Alan Walker', 'Avicii', 'David Guetta', 'Steve Aoki', 'Marshmello']
fp = []
fp.append(['厳島神社',(34.296086, 132.319826)])
fp.append(['島根ワイナリー', (35.395793, 132.711177)])
me = {}
me['身長'] = 179.5
me['体重'] = 62
me['出身'] = '神戸市'
me['生年月日'] = '1972.05.30'
me['性別'] = 'Male'

data = input('知りたい情報を入力してください >')
if data in me:
    print(me[data])
else:
    print('その情報は登録されていません')
    
kygo = ['Stole The Show', 'Firestone', 'Born to be yours', "It Ain't me"]
alan_walker = ['The Spectore', 'Ignite', 'Faded', 'Alone', 'Sing Me To Sleep']
avicii = ['Weiting For Love', 'True Believer', 'City Lights', "Can't Catch Me", 'The Days']
david_guetta = ['Flame', 'Like I Do', '2U', 'Mad Love', 'Your Love']
steve_aoki = ['Neon Future', 'Afroki', 'Boneless', 'The Power Of Now', "Home We'll Go"]
marshmello = ['FRIENDS', 'Happier', 'OCEAN']
fml = [kygo, alan_walker, avicii, david_guetta, steve_aoki, marshmello]

mdb = dict(zip(fa, fml))
