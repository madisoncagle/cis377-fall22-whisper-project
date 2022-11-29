import os
import random

recs = {}

for path, _, files in os.walk('./ravdess-song/'):
    for file in files:
        if file[12:14] == "01": # parse file name to get sentence
            txt = "Kids are talking by the door"
        else:
            txt = "Dogs are sitting by the door"
        
        recs[os.path.join(path, file).replace('\\', '/')] = txt

clips = []

for i in range(100):
    clips.append(random.choice(list(recs.items())))

test = [clip[1] for clip in clips]
print(test)