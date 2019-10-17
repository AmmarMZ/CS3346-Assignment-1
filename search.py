# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

        print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
  """

    "*** YOUR CODE HERE ***"

    # start by popping the initial node into the stack
    # DFS needs the following :
    # a stack, starting position, directions it can travel from one node to the next and a visited array
    
    startNode = problem.getStartState()
    stack = util.Stack()
    initialPath = []
    stack.push((startNode, initialPath))

    # used to keep track of what nodes were visited and
    nodesVisited = []

    # DFS ends when stack is empty
    while not stack.isEmpty():
        curNode, pathTaken = stack.pop()
        
        # once we find our goal node we can simply return the path we took
        if (problem.isGoalState(curNode)):
            return pathTaken
            
        if (curNode not in nodesVisited):
            # we set the node to visited
            nodesVisited.append(curNode)
            neighbors = problem.getSuccessors(curNode)
            # push all children/neighbors onto the stack
            for neighbor in neighbors:
                # get the cardinal direction from the neighbor using neighbor[1]
                tempPath = pathTaken + [neighbor[1]]
                # then push the new node to the stack along with the path traversed
                stack.push((neighbor[0], tempPath))



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # BFS is pretty much the same as DFS except we are using a queue instead of a stack
    # start by popping the initial node into the q
    startNode = problem.getStartState()
    q = util.Queue()
    initialPath = []
    q.push((startNode, initialPath))
    
    # used to keep track of what nodes were visited and
    nodesVisited = []

    while not q.isEmpty():
        curNode, pathTaken = q.pop()
        if(problem.isGoalState(curNode)):   
            return pathTaken
        
        if (curNode not in nodesVisited):
            nodesVisited.append(curNode)
            neighbors = problem.getSuccessors(curNode)
            for neighbor in neighbors:
                tempPath = pathTaken + [neighbor[1]]
                q.push((neighbor[0],tempPath))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    #UCS is just BFS with a priority queue vs a regular queue
    startNode = problem.getStartState()
    pQ = util.PriorityQueue()
    initialPath = []
    initialCost = 0
    pQ.update((startNode, initialPath, initialCost), 0)

    nodesVisited = []

    while not pQ.isEmpty():

        curNode, pathTaken, curCost = pQ.pop()
        if(problem.isGoalState(curNode)):
            return pathTaken
        
        if(curNode not in nodesVisited):
            nodesVisited.append(curNode)
            neighbors = problem.getSuccessors(curNode)
            for neighbor in neighbors:
                tempPath = pathTaken + [neighbor[1]]
                # calculate cost since we're using a pq instead of a queue
                tempCost = curCost + neighbor[2]
                pQ.update((neighbor[0], tempPath, tempCost), tempCost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    #A-Star search is just UCS with a heuristic that is used to calculate the cost instead of us using the actual cost

    startNode = problem.getStartState()
    pQ = util.PriorityQueue()
    initialPath = []
    initialCost = 0
    pQ.update((startNode, initialPath, initialCost), 0)

    nodesVisited = []

    while not pQ.isEmpty():

        curNode, pathTaken, curCost = pQ.pop()
        if(problem.isGoalState(curNode)):
            return pathTaken
        
        if(curNode not in nodesVisited):
            nodesVisited.append(curNode)
            neighbors = problem.getSuccessors(curNode)
            for neighbor in neighbors:
                tempPath = pathTaken + [neighbor[1]]
                tempCost = curCost + neighbor[2]
                # add heuristic here, otherwise code is same as UCS
                pQ.update((neighbor[0], tempPath, tempCost), tempCost + heuristic(neighbor[0], problem))

    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
