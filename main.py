# -*- coding: UTF-8 -*-
# game VARIABLE

import  random

class Game:
    name = ""
    throwsLeft = 0
    bonesCount = 0
    currentMove = 1
    
    curThrowScorecPC = 0
    curThrowScorePL = 0
    
    bones = []
    finalScoresTable = []
    
    replayKey = "r"
    backToMenuKey = "b"
    exiteKey = "x"
    
    maxThrows = 3
    maxBones = 3    
    
    #...logic...
    def setname(self,PlayerName):
        self.name = PlayerName
        
    def setThrowsCount(self,Count):
        self.throwsLeft = Count
        
    def setBonesCount(self,Count):
        self.bonesCount = Count
    
    def storeScores(self):
        self.finalScoresTable += [self.curThrowScoresPL , self.curThrowScoresPC]
    
    def setPLScores(self,scores):
        self.curThrowScoresPL = scores
    
    def setPCScores(self,scores):
        self.cutThrowScoresPC = scores
   
    def coinToss(self):
        self.currentMove = random.choice([-1.1])
    
    def throwBones(self):
        self.Bones = []
        for i in range(self.bonesCount):
            self.Bones. append(random.randint(0, 5))
   
    def showeBones(self):
        for i in self.Bones:
            
             print(self.bonesSprites[i] + "\n")
   
    def  setBoneSpace(self):
         space = random.randint (1,76)
         spaces = ""
         for i in range(space): space += " "
    if boneSide == 1 : return spaces + "###\n" + spaces + "#0#\n" + spaces + "###"
    elif boneSide == 2 :return  spaces + "0##\n" + spaces + "###\n" + spaces + "##0"
    elif boneSide == 3 : return spaces + "0##\n" + spaces + "#0#\n" + spaces + "##0"
    elif boneSide == 4 : return spaces + "0#0\n" + spaces + "###\n" + spaces + "0#0"
    elif boneSide == 5 : return spaces + "0#0\n" + spaces + "#0#\n" + spaces + "0#0"
    elif boneSide == 6 : return spaces + "000\n" + spaces + "###\n" + spaces + "000"
    
    def throw(self):
        if self.currentMove == 1:
            self.throwBones()
            self.setPCScores(sum(self.Bones))
        else: 
            self.sayPlayerTurn()
            self.throwBones ()
            self.setPLScores(sum(self.Bones))
        self.store.Score       
                        
    # ... interface ...
    def sayPlayerTurn(self):
        pass
    def showThrowScores(self):
        
    def showOverallScores (self):
        pass    
    def showResultTable(self):
        pass
    def showActionMenu (self):
        pass
             
#game = Game()

#game.setBonesCount(3)
#game.throwBones()
#game.showBones()            
                               
            
            
            
                 

        
        
        
                 
        
    
    
    
    