import madgraph.various.misc as misc

def remove_diag(diag):
    """force to have a top quark in the diagram
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
