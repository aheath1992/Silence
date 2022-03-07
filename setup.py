#/usr/bin/env python3

from distutils.core import setup

name = 'silence'

setup(name='silence',
      version='1.0',
      description='Text based RPG game',
      author='Andrew Heath',
      author_email='aheath1992@gmail.com',
      license='GPLv2+',
      scripts=['bin/silence'],
      data_files=[
          ('share/man/man1', ['man/en/silence.1']),
          ('share/licenses/silence', ['LICENSE'])
      ],
      packages=['silence', 'silence.interface', 'silence.interface.data',
          'silence.battle', 'silence.battle.data', 'silence.combat_entity', 
          'silence.combat_entity.data', 'silence.player', 'silence.player.data',
          'silence.rooms'],
      package_data={'': ['data.json']},
      include_package_data=True
     )
