from distutils.core import setup
try:
    import py2exe
except ImportError:
    pass

setup(
    name = 'liveusb-creator',
    version = '2.7',
    packages = ['liveusb', 'liveusb/urlgrabber'],
    scripts = ['liveusb-creator'], 
    license = 'GNU General Public License (GPL)',
    url = 'https://fedorahosted.org/liveusb-creator',
    description = 'This tool installs a LiveCD ISO on to a USB stick',
    long_description = 'The liveusb-creator is a cross-platform tool for easily installing live operating systems on to USB flash drives',
    platforms = ['any'], 
    maintainer = 'Luke Macken',
    maintainer_email = 'lmacken@redhat.com',
    windows = [
        {
            "script" : "liveusb-creator",
            "icon_resources" : [(0, "data/fedora.ico")],
        }
    ],
    options={
        "py2exe" : {
            "includes" : ["sip", "PyQt4._qt"],
            'bundle_files': 1,
        }
    }, 
    zipfile=None,
    data_files = [
        "LICENSE.txt",
        ("tools", [
            "tools/dd.exe",
            "tools/syslinux.exe",
            "tools/7z.exe",
            "tools/7z.dll",
            "tools/7zCon.sfx",
            "tools/7-Zip-License.txt",
        ])
    ]
)
