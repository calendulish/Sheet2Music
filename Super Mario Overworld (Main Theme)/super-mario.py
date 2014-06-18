#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2014 Lara Maia <lara@craft.net.br>
#
#    This Program is free software: you can redistribute it and/or modify
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

tempo = 120

_intro = (
          [ 'E6:' , 1 ],
          [ 'E6;' , 1 ],
          [ 'E6;' , 1 ],
          [ 'C6'  , 1 ],
          [ 'E6:' , 1 ],
          [ 'G6'  , 2 ],
          [ ' '   , 2 ],
          [ 'G5'  , 2 ],
          [ ' '   , 2 ],
         )

_parte1 = (
           [ 'C6'  , 1 ],
           [ ' '   , 3 ],
           [ 'G5'  , 1 ],
           [ ' '   , 3 ],
           [ 'E5'  , 1 ],
           [ ' '   , 3 ],
           [ 'A5;' , 1 ],
           [ 'B5:' , 1 ],
           [ 'Bb5;', 1 ],
           [ 'A5:' , 1 ],

           [ 'G5'  , 1 ],
           [ 'E6;' , 1 ],
           [ 'G6;' , 1 ],
           [ 'A6:' , 1 ],
           [ 'F6'  , 1 ],
           [ 'G6;' , 1 ],
           [ 'D6:' , 1 ],
           [ 'C6;' , 1 ],
           [ 'D6;' , 1 ],
           [ 'B5'  , 1 ],
           [ ' '   , 2 ],
         )

_parte2a = (
            [ 'G6:' , 1 ],
            [ 'G6'  , 1 ],
            [ 'F6;' , 1 ],
            [ 'D#6:', 1 ],
            [ 'E6:' , 1 ],
            [ 'G#5' , 1 ],
            [ 'A5;' , 1 ],
            [ 'C6:' , 1 ],
            [ 'F5'  , 1 ],
            [ 'C6;' , 1 ],
            [ 'D6'  , 1 ],
            [ ' '   , 2 ],
           )

_parte2b = (
            [ 'G6;' , 1 ],
            [ 'Gb6' , 1 ],
            [ 'F6;' , 1 ],
            [ 'D#6:', 1 ],
            [ 'E6:' , 1 ],
            [ 'C7:' , 1 ],
            [ 'C7;' , 1 ],
            [ 'C7'  , 1 ],
            [ 'G5:' , 1 ],
            [ 'C5'  , 1 ],
            [ ' '   , 3 ],
           )

_parte2c = (
            [ 'C5:' , 1 ],
            [ 'Eb6' , 1 ],
            [ ' '   , 2 ],
            [ 'D6'  , 1 ],
            [ ' '   , 2 ],
            [ 'C6:' , 1 ],
            [ 'G5;' , 1 ],
            [ 'G5:' , 1 ],
            [ 'C5'  , 3 ],
            [ ' '   , 2 ],
           )

_parte3a = (
            [ 'C6;' , 1 ],
            [ 'C6:' , 1 ],
            [ 'C6:' , 1 ],
            [ 'C6'  , 1 ],
            [ 'D6:' , 1 ],
            [ 'E6'  , 1 ],
            [ 'C6:' , 1 ],
            [ 'A5'  , 1 ],
            [ 'G5'  , 1 ],
            [ ' '   , 3 ],
           )

_parte3b = (
            [ 'C6;' , 1 ],
            [ 'C6:' , 1 ],
            [ 'C6:' , 1 ],
            [ 'C6'  , 1 ],
            [ 'D6'  , 1 ],
            [ 'E6'  , 1 ],
            [ ' '   , 2 ],

            [ 'G5'  , 1 ],
            [ ' '   , 2 ],
            [ 'C5'  , 1 ],
            [ ' '   , 2 ],
            [ 'G4'  , 1 ],
            [ ' '   , 2 ],
           )

_parte3c = (
            [ 'E6;' , 1 ],
            [ 'E6:' , 1 ],
            [ 'E6:' , 1 ],
            [ 'C6'  , 1 ],
            [ 'E6:' , 1 ],
            [ 'G6'  , 1 ],
            [ ' '   , 3 ],
            [ 'G5'  , 1 ],
            [ ' '   , 2 ],
           )

_parte4a = (
            [ 'E6'  , 1 ],
            [ 'C6:' , 1 ],
            [ 'G5'  , 1 ],
            [ ' '   , 2 ],
            [ 'G#5:', 1 ],
            [ 'A5'  , 1 ],
            [ 'F6:' , 1 ],
            [ 'F6'  , 1 ],
            [ 'A5:' , 1 ],
           )

_parte4b = (
            [ 'B5'  , 2 ],
            [ 'A6;' , 1 ],
            [ 'A6;' , 1 ],
            [ 'A6;' , 1 ],
            [ 'G6;' , 1 ],
            [ 'F6;' , 1 ],
            [ 'E6;' , 1 ],
            [ 'C6:' , 1 ],
            [ 'A5'  , 1 ],
            [ 'G5'  , 1 ],
            [ ' '   , 2 ],
           )

_parte4c = (
            [ 'B6'  , 1 ],
            [ 'F6:' , 1 ],
            [ 'F6;' , 1 ],
            [ 'F6:' , 1 ],
            [ 'E6;' , 1 ],
            [ 'D6;' , 1 ],
            [ 'C6;' , 1 ],
            [ 'E5:' , 1 ],
            [ 'E5'  , 1 ],
            [ 'C5'  , 1 ],
            [ ' '   , 4 ],
           )

end = (
       [ 'C6'  , 1 ],
       [ ' '   , 3 ],
       [ 'G5'  , 1 ],
       [ ' '   , 3 ],
       [ 'E5'  , 1 ],
       [ ' '   , 3 ],
       [ 'A5'  , 2 ],
       [ 'B5'  , 2 ],
       [ 'A5'  , 2 ],
       [ 'Ab5' , 2 ],
       [ 'Bb5' , 2 ],
       [ 'Ab5' , 2 ],
       [ 'G5'  , 1 ],
       [ 'D5'  , 1 ],
       [ 'G5'  , 7 ],
      )

parte1 = _intro + (_parte1 * 2)
parte2 = _parte2a + _parte2b + _parte2a + _parte2c
parte3 = _parte3a + _parte3b + _parte3a + _parte3c
parte4 = (_parte1 * 2) + _parte4a + _parte4b + _parte4a + _parte4c

melody = parte1 +\
         parte2 +\
         parte2 +\
         parte3 +\
         parte4 +\
         parte4 +\
         parte3 +\
         parte4 +\
         end
