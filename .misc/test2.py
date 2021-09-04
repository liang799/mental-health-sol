  while len(query)!=0:
  #  testdict = {
  #    "Mindfull1": "Hacks1",
  #    "Mindfull2" : "Hacks2",
  #    "Mindfull3" : "Hacks3"
  #  }
  #  diction = open('links.txt', 'w')
  #  diction.write(str(testdict))
  #  diction.close()

    details={'Name' : "Alice", 
            'Age' : 21, 
            'Degree' : "Bachelor Cse", 
            'University' : "Northeastern Univ"} 
      
    with open("links.txt", 'w') as f:  
        for key, value in details.items():  
            f.write('%s:%s\n' % (key, value))
        f.close()
  
    yesString =''
    file = open('links.txt', 'r')
    for line in file:
      position = line.find(':')
      yesString = line[position+1:]
      print(yesString)
    
    query = ''

