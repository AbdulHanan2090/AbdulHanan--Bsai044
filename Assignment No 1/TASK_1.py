class Task1:
    def __init__(self,states,inputs,string_in,final_state):
        self.states=states
        self.inputs=inputs
        self.string_in=string_in
        self.final_state=final_state
        self.in_=False
        self.state=0
        for i in self.string_in:
            if i in self.inputs:
                self.in_=True
            else:
                self.in_=False
                print("This word is invalid For Over language-->",i)
    def starting(self):
        if self.in_ == True:
            for i in self.string_in:
                i=int(i)
                if self.state == 0:
                    print(f"---{i}--->Q0")
                    self.state=self.Q0(i)
                elif self.state == 1:
                    print(f"---{i}--->Q1")
                    self.state=self.Q1(i)
                elif self.state == 2:
                    print(f"---{i}--->Q2")
                    self.state=self.Q2(i)
                elif self.state == 3:
                    print(f"---{i}--->Q3")
                    self.state=self.Q3(i)
            if self.state == 0:
                print("Valide")
            else :
                print("Invalid") 
        else:
            pass
    def Q0(self,word):
        if word == 0:
            return 1
        if word == 1:
            return 3
    def Q1(self,word):
        if word == 0:
            return 0
        if word == 1:
            return 2
    def Q2(self,word):
        if word == 0:
            return 3
        if word == 1:
            return 1
    def Q3(self,word):
        if word == 0:
            return 2
        if word == 1:
            return 0
states=['Q0','Q1','Q2','Q3']
inputs=['0','1']
string_in=input("Enter Your input String: ")
final_state='q0'
obj=Task1(states,inputs,string_in,final_state)
obj.starting()