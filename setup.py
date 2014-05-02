from distutils.core import setup

setup(name='editproto',
      version='0.1',
      author='Sharif Olorin',
      author_email='sio@tesser.org',
      requires=[
          'wxpython',
          'protobuf'
          ],
      packages=['editproto', 'editproto.gui'],
      scripts=['bin/editproto'],
      )
