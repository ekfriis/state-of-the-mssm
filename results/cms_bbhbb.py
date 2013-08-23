# CMS bbHbb result
# HIG-12-033
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/Hig12033TWiki

#---+++ MSSM Higgs boson limit table:
#%$tan \beta$% (%$m_h^{max}$% scenario at %$\mu=+200GeV$% )
#|  *Mass [GeV]*  |  *Observed limit *  |  *Expected limit*  |

raw_data_plus_200 = '''
|    90  |  21.8  |  28.2  |
|  100  |  17.7  |  28.2  |
|  120  |  20.5  |  25.7  |
|  130  |  21.9  |  24.8  |
|  140  |  21.2  |  25.1  |
|  160  |  19.5  |  23.2  |
|  180  |  27.8  |  23.5  |
|  200  |  21.6  |  22.2  |
|  250  |  32.6  |  29.1  |
|  300  |  42.2  |  35.7  |
|  350  |  35.5  |  44.0  |
'''


#---+++ MSSM Higgs boson limit table:
# %$tan \beta$% (%$m_h^{max}$% scenario at %$\mu=-200GeV$% )
#|  *Mass [GeV]*  |  *Observed limit *  |  *Expected limit*  |
raw_data_minus_200 = '''
 |   90    |  18.7  |  23.4  |
 |   100  |  15.7  |  23.5  |
 |   120  |  18.1  |  22.0  |
 |   130  |  19.1  |  21.2  |
 |   140  |  18.4  |  21.3  |
 |   160  |  17.0  |  19.8  |
 |   180  |  23.0  |  19.9  |
 |   200  |  18.5  |  19.0  |
 |   250  |  26.1  |  23.7  |
 |   300  |  31.8  |  27.9  |
 |   350  |  28.0  |  33.0  |
'''

label = "CMS bHbb 4.8/fb"

limit = []

for line in raw_data_minus_200.split('\n'):
    if not line:
        continue
    line = line.replace('|', ' ').strip()
    fields = [float(x) for x in line.split(' ') if x != '']
    limit.append((fields[0], fields[1]))
