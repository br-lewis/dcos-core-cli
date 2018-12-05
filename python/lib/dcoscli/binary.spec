# -*- mode: python -*-

block_cipher = None


a = Analysis(['dcoscli/main.py'],
             pathex=[os.path.dirname(os.getcwd()),
                     os.getcwd()],
             datas=[('dcoscli/data/help/*','dcoscli/data/help'),
                    ('../dcos/dcos/data/config-schema/*', 'dcos/data/config-schema'),
                    ('../dcos/dcos/data/marathon/*', 'dcos/data/marathon')],
             binaries=None,
             hiddenimports=['_cffi_backend'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)


pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher)


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='dcos',
          debug=False,
          strip=False,
          upx=True,
          console=True)