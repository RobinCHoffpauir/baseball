# -*- coding: utf-8 -*-


"""
<h1>MLBAM's usage policy:</h1>
The accounts, descriptions, data and presentation in the referring page (the "Materials") are proprietary content of MLB Advanced Media, L.P ("MLBAM").
Only individual, non-commercial, non-bulk use of the Materials is permitted and any other use of the Materials is prohibited without prior written authorization from MLBAM.
Authorized users of the Materials are prohibited from using the Materials in any commercial manner other than as expressly authorized by MLBAM.
"""
import mlbgame as mlb


games = pd.DataFrame()
for y in range(2010,2021):
    for a in range(4,10):
        for n in range(30):
            for d in mlb.day(y,a,n):
                games=games.append(d.__dict__, ignore_index=True)

