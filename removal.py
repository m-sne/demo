import pandas as pd
import os


# root = './data/deam'
# df = pd.read_csv(os.path.join(root, 'annotations', 'normalize.csv'))
# song_ids = df['song_id'].iloc[100:]
#
# for song_id in song_ids:
#     file_name = os.path.join(root, 'audio', '{}.mp3'.format(str(song_id)))
#
#     os.remove(file_name)


methods = ['m-sne', 'd-sne', 'dscmr', 'contrastive', 'cross-modal']

for method in methods:

    for i in range(101, 1500):
        file_name = os.path.join('./data/testers/{}'.format(method), '{}.jpg'.format(str(i)))
        os.remove(file_name)
