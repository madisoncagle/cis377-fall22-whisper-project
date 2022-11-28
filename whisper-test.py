import os
import random

recs = {}

for path, _, files in os.walk('./darpa-timit/data/TEST/'):
    for file in files:
        if str(file).endswith(".wav"):
            f = open(os.path.join(path, file).replace('\\', '/').replace('WAV.wav', 'TXT'))
            txt = f.readline()
            recs[os.path.join(path, file).replace('\\', '/')] = txt[8:-1]

clips = []

for i in range(100):
    clips.append(random.choice(list(recs.items())))

test = [clips[i][1] for i in range(len(clips))]