# Custom functions

import os
import json

def IsNum( value ):
    return ( type( value ) == str and value.isdigit() ) or ( isinstance( value, ( int, float ) ) )

def IsBool( value ):
    if value in [1, True]:
        return True
    elif value in [0, False]:
        return False
    else:
        raise ValueError( "Input must be 1, 0, True or False" )
    
def SaveData( filename, data ):
    path = f"./{filename}"
    with open( path, "w" ) as info:
        json.dump( data, info )

def LoadData( filename ):
    path = f"./{filename}"
    if os.path.isfile( path ):
        with open( path, "r" ) as info:
            if os.stat( path ).st_size == 0:
                info = []
            else:
                info = json.load( info )
            return info
    else:
        return []