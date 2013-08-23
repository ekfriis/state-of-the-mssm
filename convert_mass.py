'''

Shell out to Feynhiggs to convert a MSSM H+ mass to a A0 mass

'''

import subprocess
import tempfile

FEYNHIGGS_EXEC = "FeynHiggs-2.9.5/x86_64-Darwin/bin/FeynHiggs"
FEYNHIGGS_SCENARIO = "FeynHiggs-2.9.5/example/LHBMS/mhmax.in"


def convert_mass_tb(m_hp, tan_beta):
    """ Returns the A0 mass corresponding to an H+ mass and tanB point """
    with open(FEYNHIGGS_SCENARIO, 'r') as scenario:
        # this is stupid but you can't use stdin.
        with tempfile.NamedTemporaryFile() as tmpfile:
            for line in scenario:
                # replace default tangent beta
                if line.startswith('TB'):
                    line = 'TB %f\n' % tan_beta
                # setup model using mH+, we want A0
                if line.startswith('MA0'):
                    line = "MHp %f\n" % m_hp
                tmpfile.write(line)
            tmpfile.flush()

            proc = subprocess.Popen(
                [FEYNHIGGS_EXEC, tmpfile.name], stdout=subprocess.PIPE)

            stdout, _ = proc.communicate()

            for line in stdout.split('\n'):
                if line.startswith('| MA0'):
                    return float(line.split('=')[1])
    return None


if __name__ == "__main__":
    print convert_mass_tb(90, 30)
