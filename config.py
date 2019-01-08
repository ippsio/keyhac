import sys
import os
import datetime

import pyauto
from keyhac import *


def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()

#    keymap_global['U-LAlt-Tab'] = 'U-A-Tab'
#    keymap_global['D-LAlt-Tab'] = 'D-A-Tab'


    keymap.replaceKey( 'RAlt', 235 )
#    keymap.replaceKey( 'LAlt', 235 )
#    keymap.replaceKey( 'LWin', 235 )
    keymap.defineModifier( 235, 'User0' )

    keymap_global['User0-Space'] = 'A-Tilde'

    keymap_global['User0-Tab' ] = 'W-Tab'

#    for any in ('', 'S-', 'C-', 'C-S-', 'A-', 'A-S-', 'A-C-', 'A-C-S-', 'W-', 'W-S-', 'W-C-', 'W-C-S-', 'W-A-', 'W-A-S-', 'W-A-C-', 'W-A-C-S-','RA-RC-','RS-'):
    for any in ('', 'S-', 'C-', 'C-S-', 'W-', 'W-S-', 'W-C-', 'W-C-S-','RA-RC-','RS-'):
        keymap_global[any + 'User0-h' ] = any + 'Left'
        keymap_global[any + 'User0-j' ] = any + 'Down'
        keymap_global[any + 'User0-k' ] = any + 'Up'
        keymap_global[any + 'User0-l' ] = any + 'Right'

        keymap_global[any + 'User0-a' ] = any + 'Home'	
        keymap_global[any + 'User0-e' ] = any + 'End'

        keymap_global[any + 'User0-b' ] = any + 'PageUp'
        keymap_global[any + 'User0-f' ] = any + 'PageDown'

        keymap_global[any + 'User0-d' ] = any + 'Delete'
