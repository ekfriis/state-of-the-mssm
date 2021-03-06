# Latest CMS MSSM HTT results

# From HCP2012 PAS HIG-12-050
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/Hig12050TWiki

label = "CMS H#tau#tau 17/fb"

_raw_data = '''
| 90 | 3.25 | 5.18 | 7.19 | 8.91 | 10.6 | 5.45 |
| 130 | 3 | 3.84 | 4.94 | 5.74 | 6.89 | 5.05 |
| 140 | 3.54 | 4.46 | 5.23 | 5.79 | 6.77 | 5.4 |
| 200 | 5.01 | 5.69 | 6.91 | 8.3 | 9.44 | 4.88 |
| 250 | 5.99 | 7.7 | 9.26 | 11.1 | 12.7 | 5.3 |
| 300 | 8.3 | 10.5 | 12.4 | 14.4 | 16.6 | 7.68 |
| 350 | 10.8 | 13.5 |16.1 | 18.7 |21 |10.4 |
| 400 | 12.9 | 16.3 | 19.1 | 22.2 | 24.6 | 13.7 |
| 450 | 16 | 19.4 | 23 | 26.2 | 29.4 | 17.3 |
| 500 | 18.7 | 23 | 26.9 | 31.1 | 35.8 | 20.8 |
| 600 | 24.8 | 30.3 | 36.4 | 41.7 | 47.4 | 29.7 |
| 700 | 32.2 | 39.8 | 47.8 | 55.9 | 63.4 | 39.3 |
| 800 | 40.8 | 51 | 61.4 | 74 | 98.3 | 48.6 |
'''

limit = []

for line in _raw_data.split('\n'):
    line = line.replace('|', ' ').strip()
    if not line:
        continue
    fields = [float(x) for x in line.split(' ') if x != '']
    limit.append((fields[0], fields[-1]))

# add some non-visible points to prevent rendering errors of the fill.

limit.append((limit[-1][0], limit[-1][1] + 50))
limit.append((limit[0][0] - 10, limit[-1][1]))
