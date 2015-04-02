""" Yang Hu, yhx189"""
from collections import deque

def twoToTheN(n):
	if n==0:
		return 1
	if n==1:	
		return 2
	else:
		if n%2==0:
			tmp = twoToTheN(n/2) 
			return tmp * tmp
		else:	
			tmp = twoToTheN((n-1)/2)
			return 2*tmp*tmp
def mean(L):
	sum = 0
	for it in L:
		sum += it
	return sum / float(len(L))

		
def median(L):
	L.sort()
	if len(L)%2 == 0:
		return (L[len(L)/2] + L[len(L)/2-1])/float(2)
	else:
		return L[(len(L)-1)/2]



def bfs(tree,elem):
	q = deque()
	q.append(tree)
	while len(q) != 0:
		cur = q.popleft()
		if isinstance(cur,int):
			cur_ele = cur
		else:
			cur_ele = cur[0]
		print cur_ele
		if isinstance(cur, list):
			for it in cur[1:]:
				if isinstance(it, int):
					if it == elem:
						return True
				if isinstance(it,list):
					if it[0] == elem:
						print it[0]
						return True
					q.append(it)
	return False

def dfs(tree,elem):
	stack = []
	myTree = tree
	stack.append(tree)
	while len(stack) != 0:
		cur = stack.pop()
		
		if isinstance(cur, int):
			cur_ele = cur
		else:
			cur_ele = cur[0]
		print cur_ele
		if cur_ele == elem:
			return True
		else:
			if isinstance(cur, list):
				for it in cur[1:]:
					stack.append(it)
	return False			
		
class TTTBoard():
	def __init__(self):
		self.data = ['*']*9
	def __str__(self):
		return ' '.join(self.data[0:3]) + '\n' + ' '.join(self.data[3:6]) + '\n' + ' '.join(self.data[6:9]) + '\n'
	def makeMove(self, player, pos):
		if self.data[pos] != '*':
			return False
		else:
			self.data[pos] = player
			return True
			
	def hasWon(self, player):
		data = self.data
		if data[0] == player and data[1] == player and data[2] == player:
			return True
		elif data[3] == player and data[4] == player and data[5] == player:
			return True
		elif data[6] == player and data[7] == player and data[8] == player:
			return True
		elif data[0] == player and data[3] == player and data[6] == player:
			return True
		elif data[1] == player and data[4] == player and data[7] == player:
			return True
		elif data[2] == player and data[5] == player and data[8] == player:
			return True
		elif data[0] == player and data[4] == player and data[8] == player:
			return True
		elif data[2] == player and data[4] == player and data[6] == player:
			return True
		else:
			return False
	def gameOver(self):	
		if hasWon(self,'X') == True:
			return True
		elif hasWon(self, 'O') == True:
			return True
		elif cnt(self) == 0:
			return True	
		else:
			return False
	def cnt(self):
		num = 0
		for it in self.data:
			if it == '*':
				num = num + 1
		return num
			
	def clear(self):
		self.data = ['*'] * 9
# Programming Assignment 1 Tests
# This file includes a set of tests to make sure that your code behaves as
#    expected. These tests are not at all intended to be exhaustive. You
#    should design more tests for your code in addition to these. 

print "\nProblem 1: \n"
        
print "twoToTheN test case #1: " + str(twoToTheN(3) == 8)
print "twoToTheN test case #2: " + str(twoToTheN(0) == 1)
print "twoToTheN test case #3: " + str(twoToTheN(10) == 1024)
    
print "\nProblem 2: \n"

x = [5,1,2,3,1] 
y = [5,1,2,3,1,4]
print "mean test case #1: " + str(mean(x) == float(12)/float(5))
print "mean test case #2: " + str(mean(y) == float(16)/float(6))
print "median test case #1: " + str(median(x) == 2)
print "median test case #2: " + str(median(y) == 2.5)

print "\nProblem 3: \n"

myTree = [4, [10, [33], [2]], [3], [14, [12]], [1]]
print "bfs test case #1: " + str(bfs(myTree, 1) == True)
print "bfs test case #2: " + str(bfs(myTree, 7) == False)
print "dfs test case #1: " + str(dfs(myTree, 1) == True)
print "dfs test case #2: " + str(dfs(myTree, 7) == False)

print "\nProblem 4: \n"
            
myB = TTTBoard()
print myB
myB.makeMove("X", 8)
myB.makeMove("O", 7)
myB.makeMove("X", 5)
myB.makeMove("O", 6)
myB.makeMove("X", 2)
print myB

print "tic tac toe test case #1: " + str(myB.hasWon("X") == True)
print "tic tac toe test case #2: " + str(myB.hasWon("O") == False)
