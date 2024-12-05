import gtpyhop
import test_harness as th
import ast
import math
the_domain = gtpyhop.Domain(__package__)

print('-----------------------------------------------------------------------')
print(f"Created '{gtpyhop.current_domain}'. To run the examples, type this:")
print(f'{__name__}.main()')

# states and rigid relations
rigid = gtpyhop.State('rigid relations')
rigid.types = {
    'taxi': ['t1'],
    'person': ['p1', 'p2', 'p3'],
    'dropoff_area': ['d1', 'd2', 'd3'],
    'bush': []
}

state = gtpyhop.State('state')
state.loc = {'t1': (0,0), 
                'p1': (2,2), 'p2': (4,4), 'p3': (6,6), 
                'd1': (9,8), 'd2': (3,5), 'd3': (6,3)

}

###############################################################################

# helper functions

def is_a(variable,type):
    return variable in rigid.types[type]

# def determine_order_of_moves():


###############################################################################

# Actions:
def drive(state, taxi, to):
    x, y = to
    if is_a(taxi, 'taxi'):
        if is_a(to, 'bush'):
            print(f"Cannot move to bush space")
            return False
        if x in range(0,10) and y in range(0,10):
            delta_x = abs(state.loc[taxi][0] - x)
            delta_y = abs(state.loc[taxi][1] - y)
            if delta_x + delta_y == 1:
                state.loc[taxi] = (x, y)
                return state
            elif delta_x + delta_y == 0:
                print("Taxi is already in this position")
                return False
            print(f"Failed to execute drive to {to}")
            return False
    print(f"{taxi} is not a taxi")
    return False

def pickup(state, taxi, passenger):
    if is_a(taxi, 'taxi') and is_a(passenger, 'person'):
        if state.loc[taxi] == state.loc[passenger]:
            state.loc[passenger] = taxi
            return state
        else:
            print("Taxi and passenger are not in the same space")
            return False
    print(f"{taxi} is not a taxi or {passenger} is not a person")
    return False

def dropoff(state, taxi, passenger, dropoff_area):
    if is_a(taxi, 'taxi') and is_a(passenger, 'person') and is_a(dropoff_area, 'dropoff_area'):
        if state.loc[taxi] == state.loc[dropoff_area]:
            state.loc[passenger] = dropoff_area
            return state
        else:
            print("Taxi is not a dropoff location")
    print(f"{taxi} is not a taxi or {passenger} is not a person or {dropoff_area} is not a dropoff area")
    return False
        
gtpyhop.declare_actions(drive, pickup, dropoff)

###############################################################################

# Methods
# This is the naive navigate approach, given taxi and location, it will move toward that point
# Note: Only works when there are no bushes
def navigate(state, taxi, l):
    movements = []
    if(is_a(l, 'person')):
        l = state.loc[l]
    
    if is_a(taxi, 'taxi') and l[0] in range(0,10) and l[1] in range(0,10):
        x,y = state.loc[taxi]
        while (x,y) != l:
            if x < l[0]:
                x += 1
                movements.append(('drive', taxi, (x,y)))
            elif x > l[0]:
                x -= 1
                movements.append(('drive', taxi, (x,y)))
            elif y < l[1]:
                y += 1
                movements.append(('drive', taxi, (x,y)))
            elif y > l[1]:
                y -= 1
                movements.append(('drive', taxi, (x,y)))
            else:
                print("NAVIGATE FAILED")
                break   
    else:
        print("NAVIGATE FAIL") 
    if movements:     
        return movements

def no_pickup(state, taxi, passenger):
    if state.loc[passenger] == taxi:
        return []

def only_pickup(state, taxi, passenger):
    l = state.loc[passenger]
    if is_a(taxi, 'taxi') and l[0] in range(0,10) and l[1] in range(0,10) and is_a(passenger, 'person'):
        if l == state.loc[taxi]:
            return [('pickup', taxi, passenger)]
    
def move_and_pickup(state, taxi, passenger):
    l = state.loc[passenger]
    plan = []
    if is_a(taxi, 'taxi') and l[0] in range(0,10) and l[1] in range(0,10) and is_a(passenger, 'person'):
        x = navigate(state, taxi, l)
        if x:
            plan.extend(x)
        plan.append(('pickup', taxi, passenger))
        return plan

def no_dropoff(state, taxi, passenger, l):
    if state.loc[passenger] == l:
        return []
    
def only_dropoff(state, taxi, passenger, l):
    l = state.loc[l]
    if is_a(taxi, 'taxi') and l[0] in range(0,10) and l[1] in range(0,10) and is_a(passenger, 'person'):
        return [('dropoff', taxi, passenger, l)]

def move_and_dropoff(state, taxi, passenger, d):
    l = state.loc[d]
    plan = []
    if is_a(taxi, 'taxi') and l[0] in range(0,10) and l[1] in range(0,10) and is_a(passenger, 'person'):
        x = navigate(state, taxi, l)
        if x:
            plan.extend(navigate(state, taxi, l))
        plan.append(('dropoff', taxi, passenger, d))
        return plan


gtpyhop.declare_task_methods('passenger_pickup', no_pickup, only_pickup, move_and_pickup)
gtpyhop.declare_task_methods('passenger_dropoff', no_dropoff, only_dropoff, move_and_dropoff)


###############################################################################

# Commands
def c_drive(state, taxi, to):
    x, y = to
    if is_a(taxi, 'taxi'):
        if is_a(to, 'bush'):
            print(f"Cannot move to bush space")
            return False
        if x in range(0,10) and y in range(0,10):
            delta_x = abs(state.loc[taxi][0] - x)
            delta_y = abs(state.loc[taxi][1] - y)
            if delta_x + delta_y == 1:
                state.loc[taxi] = (x, y)
                return state
            elif delta_x + delta_y == 0:
                print("Taxi is already in this position")
                return False
            print(f"Failed to execute drive to {to}")
            return False
    print(f"{taxi} is not a taxi")
    return False

def c_pickup(state, taxi, passenger):
    if is_a(taxi, 'taxi') and is_a(passenger, 'person'):
        if state.loc[taxi] == state.loc[passenger]:
            state.loc[passenger] = taxi
            return state
        else:
            print("Taxi and passenger are not in the same space")
            return False
    print(f"{taxi} is not a taxi or {passenger} is not a person")
    return False

def c_dropoff(state, taxi, passenger, dropoff_area):
    if is_a(taxi, 'taxi') and is_a(passenger, 'person') and is_a(dropoff_area, 'dropoff_area'):
        if state.loc[taxi] == state.loc[dropoff_area]:
            state.loc[passenger] = dropoff_area
            return state
        else:
            print("Taxi is not a dropoff location")
    print(f"{taxi} is not a taxi or {passenger} is not a person or {dropoff_area} is not a dropoff area")
    return False

gtpyhop.declare_commands(c_drive, c_pickup, c_dropoff)


###############################################################################

print('-----------------------------------------------------------------------')
# print(f"Created the domain '{domain_name}'. To run the examples, type this:")
# print(f"{domain_name}.main()")

def main(do_pauses=True):
    """
    Run various examples.
    main() will pause occasionally to let you examine the output.
    main(False) will run straight through to the end, without stopping.
    """

    # If we've changed to some other domain, this will change us back.
    gtpyhop.current_domain = the_domain
    gtpyhop.print_domain()

    state1 = state.copy()

    state1.display(heading='\nInitial state is')

    th.pause(do_pauses)

    gtpyhop.verbose = 3
    print(state1.loc['p1'])
    result = gtpyhop.find_plan(state1,[('passenger_pickup','t1','p1'), ('passenger_dropoff', 't1', 'p1', 'd1')])
    # result = gtpyhop.find_plan(state1,[('passenger_pickup','t1','p1')])
    print("=======MY RESULTS=======")
    # print(state1.loc['t1'])
    # print(state1.loc['p1'])
    # print(navigate(state1, 't1', 'p1'))
    # print("COND:", is_a('t1', 'taxi'))
    # print(result)

if __name__ == "__main__":
    main()