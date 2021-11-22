class Knight:
    """"Knight works here"""

    def __init__(self,beg_pos,des_pos):
        self.MOVES = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
        self.BEG_POS = beg_pos
        self.DES_POS = des_pos
        self.VISITED_POS = [beg_pos]
        self.CURRENT_POS = [beg_pos]
        self.ALL_STEPS   = []
        self.CURRENT_STEP = {}
    
    def move(self,current_pos):
        moved_pos = []
        for _ in self.MOVES:
            temp_move = (current_pos[0]+_[0],current_pos[1]+_[1])
            #Check for possible move and where not visited
            if 1<=temp_move[0]<=8 and 1<=temp_move[1]<=8 and (not(temp_move in self.VISITED_POS)):
                moved_pos.append(temp_move)
                self.VISITED_POS.append(temp_move)
        return moved_pos

    def iterate(self):
        #Firts move
        self.CURRENT_POS = self.move(self.BEG_POS)
        self.CURRENT_STEP = {}
        #Adding move to steps
        for count in range(len(self.CURRENT_POS)):
            self.CURRENT_STEP[str(count)] = [self.CURRENT_POS[count]]
        self.ALL_STEPS.append(self.CURRENT_STEP)

        while not(self.DES_POS in self.VISITED_POS):
            temp_current_pos = []
            #Get Keys of dictionary
            key_of_cur_steps = list(self.CURRENT_STEP.keys())
            self.CURRENT_STEP= {}
            #counts use for make unique key to steps dict
            count_cur_pos_el = 0
            for current_pos_element in self.CURRENT_POS:
                #Move again
                new_move = self.move(current_pos_element)
                count_move = 0
                for _move in new_move:
                    temp_current_pos.append(_move)
                    #key of parent element
                    key_of_last_step = key_of_cur_steps[count_cur_pos_el]
                    #unique key
                    generated_key = str(key_of_last_step)+str(count_move)
                    #step = parentMove + childMove
                    self.CURRENT_STEP[generated_key] = self.ALL_STEPS[-1][key_of_last_step] + [_move]
                    count_move +=1
                count_cur_pos_el+=1
            self.CURRENT_POS = temp_current_pos
            #ALL MOVES      
            self.ALL_STEPS.append(self.CURRENT_STEP)
        #get values from dictionary
        for step in self.CURRENT_STEP.values():
            if  self.DES_POS in step:
                return step