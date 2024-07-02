import os
import sys
currentDir = os.path.dirname(os.path.abspath(__file__))
utilsDir = os.path.join(currentDir, '../utils/')
sys.path.append(utilsDir)
import selectedText 


print(selectedText.readText())
