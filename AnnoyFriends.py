import xaut
from time import sleep
k = xaut.keyboard()
sleep(10) # Time to get ready.. 

n=100
## Prints Hello there n times on the chatbox/ messenger.. 
## Annoyance level : Low

for i in range(n):
	k.type("Hello there!!")
	k.type("{Return}")

