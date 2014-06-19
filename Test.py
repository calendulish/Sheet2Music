#!/usr/bin/env python
#
#    Copyright (C) 2014 Lara Maia <lara@craft.net.br>
#
#    This file is part of Sheet2RPiMusic.
#
#    Sheet2RPiMusic is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    http://www.gnu.org/licenses/gpl.html
#

import sys
import RPiMusic

pMusic = RPiMusic.Melody()

try:
    music = str(sys.argv[2]+'.melody').replace('/', '')

    if sys.argv[1] == 'buzzer':
        pMusic.buzzerPlay(music)
    elif sys.argv[1] == 'speaker':
        pMusic.spkPlay(music)
    elif sys.argv[1] == 'led':
        pMusic.ledPlay(music)

    pMusic.end()
except ImportError as e:
    print('Melody {} not found'.format(str(e)[17:-1]))
