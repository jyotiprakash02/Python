
'1. make a dictionary of word and its length pair by dictionary compression'

# sentence = 'hello world welcome to python hello hi world welcome to python'
# _sentence = sentence.split()
# print({word: len(word) for word in _sentence})

'2. make dictionary of letter and and its ascii value pair'

# word = 'abcdABCD'
# print({ele: ord(ele) for ele in word})

'3.make dictionary of country and dial-code'

# dial_code = [(86, 'china'), (91, 'india'), (1, 'united states')]
# print({ele2: ele1 for ele1, ele2 in dial_code})

'4. make a dictionary of cities and its population'

# cities =['Tokio','delhi','kolkata','mumbai']
# population=['1,38,000','2,00,000','8,00,152','5,25,858']
# print({ele1:ele2 for ele1,ele2 in zip(cities,population)})

'5.make a dictionary of building and its height in feet'

# buildings=['Burj Khalifa','Burj Al Arab','Dubai Frame','Jumeirah beach hotel','eiffel tower','Trump tower']
# heights_meters=[830,321,150,104,330,202]
# print({building:height_meter**3.28 for building,height_meter in zip(buildings,heights_meters)})

'6.make a dictionary of item and its price above then 200'

# price={'Acme':45.23,'Apple':612.78,'IBM':205.55}
# print({ele1:ele2 for ele1,ele2 in price.items() if ele2>200})


















