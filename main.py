from mapper import mapper as MP
from knight import Knight as NT


def ask_for():
    positions = str(input('Beginning , Destination (Comma seperated)\n:::: ')).strip().split(',')

    #Make tuple from input      --> beg_pos = (a,1)
    beg_pos = tuple( l for l in positions[0].strip())
    des_pos = tuple( l for l in positions[1].strip())
    #string to number --> beg_pos = (a,1) ==> (1,1)
    beg_pos = (MP(beg_pos[0]),int(beg_pos[1]))
    des_pos = (MP(des_pos[0]),int(des_pos[1]))

    return beg_pos,des_pos

if __name__ == "__main__":
    #Input
    beg,des = ask_for()
    #check Path
    moves = NT(beg,des).iterate()
    #moves as string 
    _moves = MP(str(beg[0]))+str(beg[1])
    for move in moves:
        #moves = move1 --> move2 --> move3 -----> moven
        _moves = _moves+' --> '+ MP(str(move[0]))+str(move[1])
    print(_moves)
    