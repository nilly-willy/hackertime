# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        foodList = newFood.asList()
        foodDistances = [manhattanDistance(newPos, food) for food in foodList]
        if foodDistances:
            closestFood = min(foodDistances)
        else:
            closestFood = 1
        
        return successorGameState.getScore() + 1/closestFood

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """
    

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        def minimax(state, d, ag):
            if d == self.depth or state.getLegalActions(ag) == 0 or state.isWin() or state.isLose():            
                return self.evaluationFunction(state), None
            infinity = float("inf")
            neg_infinity = float("-inf")
            min_val = neg_infinity
            if ag == 0:
                for a in state.getLegalActions(ag):
                    v, act = minimax(state.generateSuccessor(ag, a), d, (ag + 1) % state.getNumAgents())
                    if v > min_val:
                        maxAG = a
                        min_val = v
            if min_val is not neg_infinity:
                return min_val, maxAG
            
            max_val = infinity
            if ag != 0:
                for a in state.getLegalActions(ag):
                    if ((ag + 1) % state.getNumAgents()) != 0:
                        v, act = minimax(state.generateSuccessor(ag, a), d, (ag + 1) % state.getNumAgents())
                    else:
                        v, act = minimax(state.generateSuccessor(ag, a), d + 1, (ag + 1) % state.getNumAgents())
                    if v < max_val:
                        minAG = a
                        max_val = v
            if max_val is not infinity:
                return max_val, minAG
        
        val, act =  minimax(gameState, 0, 0)
        return act
        #util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def alpha_beta(state, d, ag, A, B):
            if d == self.depth or state.getLegalActions(ag) == 0 or state.isWin() or state.isLose():            
                return self.evaluationFunction(state), None
            infinity = float("inf")
            neg_infinity = float("-inf")
            min_val = neg_infinity
            if ag == 0:
                for a in state.getLegalActions(ag):
                    v, act = alpha_beta(state.generateSuccessor(ag, a), d, (ag + 1) % state.getNumAgents(), A, B)
                    if v > min_val:
                        maxAG = a
                        min_val = v

                    if min_val > B:
                        return min_val, maxAG
                    A = max(A, min_val)  
            if min_val is not neg_infinity:
                return min_val, maxAG
            
            max_val = infinity
            if ag != 0:
                for a in state.getLegalActions(ag):
                    if ((ag + 1) % state.getNumAgents()) != 0:
                        v, act = alpha_beta(state.generateSuccessor(ag, a), d, (ag + 1) % state.getNumAgents(), A, B)
                    else:
                        v, act = alpha_beta(state.generateSuccessor(ag, a), d + 1, (ag + 1) % state.getNumAgents(), A, B)
                    if v < max_val:
                        minAG = a
                        max_val = v
                    if max_val < A:
                        return max_val, minAG
                    B = min(B, max_val)
            if max_val is not infinity:
                return max_val, minAG
        
        val, act =  alpha_beta(gameState, 0, 0, float("-inf"), float("inf"))
        return act
        #util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax(state, d, ag):
            if d == self.depth or state.getLegalActions(ag) == 0 or state.isWin() or state.isLose():            
                return self.evaluationFunction(state), None
            infinity = float("inf")
            neg_infinity = float("-inf")
            min_val = neg_infinity
            if ag == 0:
                for a in state.getLegalActions(ag):
                    v, act = expectimax(state.generateSuccessor(ag, a), d, (ag + 1) % state.getNumAgents())
                    if v > min_val:
                        maxAG = a
                        min_val = v
            if min_val is not neg_infinity:
                return min_val, maxAG
            
            count = 0
            max_val = 0

            if ag != 0:
                for a in state.getLegalActions(ag):
                    if ((ag + 1) % state.getNumAgents()) != 0:
                        v, act = expectimax(state.generateSuccessor(ag, a), d, (ag + 1) % state.getNumAgents())
                    else:
                        v, act = expectimax(state.generateSuccessor(ag, a), d + 1, (ag + 1) % state.getNumAgents())
                    minAG = a
                    count += 1
                    max_val += v
                    
            if max_val is not infinity:
                return max_val/count, minAG
        
        val, act =  expectimax(gameState, 0, 0)
        return act
        #util.raiseNotDefined()

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: I used a similar procedure to Q1 in regards to scoring food. I implemented similar logic for the power pellet
    but with a higher scoring for finding pellets. For the ghosts, i implemented a heavier penalty when close to a ghost and
    incentivized going after ghosts when they are in a scared state. Finally I added a penalty if there were still food and 
    power pellets left in the grid to push pacman to eat them.
    """
    # successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    score = currentGameState.getScore()

    foodList = newFood.asList()
    foodDistances = [manhattanDistance(newPos, food) for food in foodList]
    if foodDistances:
        closestFood = min(foodDistances)
    else:
        closestFood = 1
    
    score += 1/closestFood
    
    for i, ghost in enumerate(newGhostStates):
        ghostDistance = manhattanDistance(newPos, ghost.getPosition())
        if newScaredTimes[i] > 0: 
            score += 10 / (ghostDistance + 1)
        else:
            if ghostDistance < 2:
                score -= 1000
            else:
                score -= 1 / (ghostDistance + 1)

    powerPellets = currentGameState.getCapsules()
    if powerPellets:
        pelletDistances = [manhattanDistance(newPos, pellet) for pellet in powerPellets]
        if pelletDistances:
            closestPellet = min(pelletDistances)
        else:
            closestPellet = 1
        score += 1/(closestPellet + 1)


    foodPenalty = len(foodList)  
    pelletPenalty = 5 * len(powerPellets)  

    return score - foodPenalty - pelletPenalty
    

    
    

    
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
