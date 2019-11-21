import sys
from setuptools import setup

UTM_VERSION = '0.7.3'

def _version():
    """Returns major and minor interpreter version."""
    return "{}{}".format(sys.version_info[0], sys.version_info[1])

def _platform():
    """Returns platform signature for wheels."""
    if sys.platform.startswith('linux'):
        return 'manylinux1'
    elif sys.platform.startswith('darwin'):
        return 'darwin'
    raise ValueError("Platform not supported: {}".format(sys.platform))

# Note: no more 'm' abiflag since Python 3.8.0
WHEEL_SIGNATURE = 'cp{0}-cp{0}{2}-{1}_x86_64'.format(_version(), _platform(), sys.abiflags)

setup(
    name='tm-python',
    version=UTM_VERSION,
    author="Bernhard Arnold",
    author_email="bernhard.arnold@cern.ch",
    description="""Meta package providing Python bindings for tmTable, tmGrammar and tmEventSetup""",
    install_requires=[
        'tm-table @ https://github.com/cms-l1-globaltrigger/tm-table/releases/download/{0}/tm_table-{0}-{1}.whl'.format(UTM_VERSION, WHEEL_SIGNATURE),
        'tm-grammar @ https://github.com/cms-l1-globaltrigger/tm-grammar/releases/download/{0}/tm_grammar-{0}-{1}.whl'.format(UTM_VERSION, WHEEL_SIGNATURE),
        'tm-eventsetup @ https://github.com/cms-l1-globaltrigger/tm-eventsetup/releases/download/{0}/tm_eventsetup-{0}-{1}.whl'.format(UTM_VERSION, WHEEL_SIGNATURE)
    ],
    license="GPLv3"
)
