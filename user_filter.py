import madgraph.various.misc as misc

def remove_diag(diag):
    """force to have two s-channel W decaying into a specific way. 
       Designed for interference studies where decay chain are not allowed
       This is designed for keeping the following diagram generate p p > j j w- w-, w- > e- ve~ 
       from the following syntax:  p p > j j e- ve~ e- ve~
"""

    found_top = False
    for vertex in diag['vertices']:
        if vertex.get('id') == 0: #special final vertex
            continue

        for idx, leg in enumerate(list(vertex['legs'])):
            if abs(leg['id']) == 6:
                found_top = True
                break

    return not found_top
