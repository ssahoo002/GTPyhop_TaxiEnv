import gtpyhop
# domain_name = __name__
# the_domain = gtpyhop.Domain(domain_name)

def drive(s, to):
    if to[0] in range (0,10) and to[1] in range(0,10):
        delta_x = s.taxi[0] - to[0]
        delta_y = s.taxi[0] - to[1]
        if delta_x + delta_y == 1:
            s.taxi[0] = to[0]
            s.taxi[1] = to[1]
            return 
        elif delta_x + delta_y == 0:
            return "Taxi is already in this position"
        return False

# def pickup(state, taxi, passenger):
#     if state.taxi
gtpyhop.declare_actions(drive)

# def drive(state, taxi, _to, _from):
#     if state['taxi']['pos'] == _to and _to not in state['bushes']:
#         return state
#     if _to in state['bushes']:
#         raise ValueError("Cannot drive into a bush")
#     if state['taxi']['pos'] == _from and _to not in state['bushes']:
#         state['taxi']['pos'] = _to
#     return state

# def pick_up(state, taxi, passenger):
#     if state['taxi']['pos'] == state['passengers'][passenger]['pos']:
#         state['taxi']['passengers'].append(passenger)
#         state['passengers'][passenger]['pos'] = None
#     return state

# def drop_off(state, taxi, passenger, location):
#     if passenger in state['taxi']['passengers']:
#         state['taxi']['passengers'].remove(passenger)
#         state['passengers'][passenger]['pos'] = location
#     return state


