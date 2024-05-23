import sys
from setuptools import setup

UTM_VERSION = '0.13.0'
BASE_URL = 'https://github.com/cms-l1-globaltrigger'

def _version():
    """Returns major and minor interpreter version."""
    return '{}{}'.format(sys.version_info[0], sys.version_info[1])

def _platform():
    """Returns platform signature for wheels."""
    if sys.platform.startswith('linux'):
        return 'manylinux_2_17_x86_64.manylinux2014_x86_64'
    elif sys.platform.startswith('darwin'):
        return 'macosx_10_15_x86_64'
    raise ValueError("Platform not supported: {}".format(sys.platform))

def _signature():
    # Note: no more 'm' abiflag since Python 3.8
    return 'cp{0}-cp{0}{1}-{2}'.format(_version(), sys.abiflags, _platform())

def _wheel_name(name, version):
    basename = name.replace('-', '_')
    return '{0}-{1}-{2}.whl'.format(basename, version, _signature())

def _require(name, version):
    filename = _wheel_name(name, version)
    return '{0} @ {1}/{0}/releases/download/{2}/{3}'.format(name, BASE_URL, version, filename)

install_requires = []

try:
    from tmTable import __version__
    assert __version__ == UTM_VERSION
except (ModuleNotFoundError, ImportError, AssertionError):
    install_requires.append(_require('tm-table', UTM_VERSION))

try:
    from tmGrammar import __version__
    assert __version__ == UTM_VERSION
except (ModuleNotFoundError, ImportError, AssertionError):
    install_requires.append(_require('tm-grammar', UTM_VERSION))

try:
    from tmEventSetup import __version__
    assert __version__ == UTM_VERSION
except (ModuleNotFoundError, ImportError, AssertionError):
    install_requires.append(_require('tm-eventsetup', UTM_VERSION))

setup(
    version=UTM_VERSION,
    install_requires=install_requires,
)
