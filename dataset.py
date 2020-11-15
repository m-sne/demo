import pandas as pd
import os


class Dataset:

    def __init__(self, root):
        self.root = root
        self.df = pd.read_csv(os.path.join(root, 'annotations', 'normalize.csv'))

    def __getitem__(self, idx):
        song_id = self.df['song_id'].iloc[idx]
        file_name = os.path.join(self.root, 'audio', '{}.mp3'.format(str(song_id)))
        song_file = open(file_name, 'rb')
        return song_file.read()

    def __len__(self):
        return 1000
