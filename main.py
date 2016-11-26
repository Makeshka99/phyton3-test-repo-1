# -*- coding: UTF-8 -*-
# game VARIABLE

import  random

class Game:
    name = ""
    throwsLeft = 0
    bonesCount = 0
    firstMove = 1
    
    curThrowScorecPC = 0
    curThrowScorePL = 0
    
    bones = []
    finalScoresTable = []
    
    replayKey = "r"
    backToMenuKey = "b"
    exiteKey = "x"
    
    maxThrows = 3
    maxBones = 3    
    
    bonesSprites = ["###\n#0#\#n###" , "0##\n###\n##0" , "0##\n#0#\n##0" , "0#0\n###\n0#0" , "0#0\n#0#\n0#0" ,"0#0\0#0\0#0" ]
    bone1 = "###\n#0#\#n###";
    bone2 = "0##\n###\n##0"
    bone3 = "0##\n#0#\n##0"
    bone4 = "0#0\n###\n0#0"
    bone5 = "0#0\n#0#\n0#0"
    bone6 = "0#0\0#0\0#0"
    
    def setname(self,PlayerName):
        self.name = PlayerName
        
    def setThrowsCount(self,Count):
        self.throwsLeft = Count
        
    def setBonesCount(self,Count):
        self.bonesCount = Count
    
    def storeScores(self):
        self.finalScoresTable + = [self.curThrowScoresPL , self.curThrowScoresPC]
    
    def setPLScores(self,scores):
        self.curThrowScoresPL = scores
    
    def setPCScores(self,scores):
        self.cutThrowScoresPC = scores
   
    def coinToss(self):
        self.currentMove = random.choice([-1.1])
    
    def throwBones(self):
        self.Bones = []
        for i in range(self.bonesCount - 1):
            self.Bones. append (random.randint(1, 6))
   
    def showeBones(self):
        for i in self.Bones:
            print(i)
            print
            print(self.bonesSprites[self.Bones[i]])
            
game = Game()

game.setBonesCount(3)
game.throwBones()
game.showBones()            
                               
            
            
            
                 

        
        
        
                 
        
    
    
    
    