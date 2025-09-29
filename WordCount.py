#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("gettysberg.txt", 'r')
  linecount = 0
  wordcount = 0
  lettercount = 0

  for line in textFile:
    linecount = linecount + 1 
    words = line.split()
    for w in words:
      wordcount = wordcount + 1
    lettercount = len(line)
    for c in line:
      lettercount = lettercount + 1

  print("Lines:", linecount)
  print("words:", wordcount)
  print("Characters:", lettercount)
  

if __name__ == '__main__':
  main()
