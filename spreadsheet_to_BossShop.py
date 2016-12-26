#!/usr/bin/python
spreadsheet = open("ShopInformation-Sheet1.tsv", "r")
itemDictionary = open("items.txt", "r")
#Makes a minecraft ID list accessalble by the rest of the file
dict = {}
for line in itemDictionary:
	values = line.strip('\t\n\r').split("	")
	mainID = values[0]
	secondaryID = values[1]
	DisplayName = values[2]
	ID = values[3]
	dict[DisplayName] = str(mainID) + ":" + str(secondaryID)
itemDictionary.close()
shops = {}
spreadsheet.seek(0,0)
spreadsheet.readline()
#Makes a list of all of the shops
for line in spreadsheet:
	wordsList = line.strip('\t\n\r').split("	")
	shops[wordsList[0]] = 1
#Initializes Sell Shops
for name in shops.keys():
	temp = open("shops/" + str(name) + "Sell.yml", "w+")
	temp.write("shop:")
	print "Initialized file shops/" + str(name) + "Sell.yml"
	temp.close()
#Initializes Buy Shops
for name in shops.keys():
	temp = open("shops/" + str(name) + "Buy.yml", "w+")
	temp.write("shop:")
	print "Initialized file shops/" + str(name) + "Buy.yml"
	temp.close()


#Makes the buy and sell menus
shopType = "Sell"
shopInfo = open("shopInfo.txt", "r")
itemNum = 0
for i in ["1","2"]:	
	temp = open("shops/" + str(shopType) + "Shop.yml", "w+")
	temp.write("shop:")
	print "Initialized file shops/" + str(shopType) + "Shop.yml"
	temp.close()
	shopInfo.seek(0,0)
	for line in shopInfo:
		wordsList = line.strip('\t\n\r').split(",")
		temp = open("shops/" + str(shopType) + "Shop.yml", "r+")
		temp.seek(0,2)
		temp.write("\n  " + str(wordsList[0]) + ":")
		temp.write("\n    MenuItem:")
		temp.write("\n    - name:&4&1" + wordsList[0])
		temp.write("\n    - amount:1")
		temp.write("\n    - type:" + str(dict[wordsList[1]]))
		temp.write("\n    RewardType: Shop")
		temp.write("\n    Reward: " + str(wordsList[0] + shopType))
		temp.write("\n    PriceType: Free")
		temp.write("\n    Message: ''")
		temp.write("\n    ExtraPermission: ''")
		temp.write("\n    InventoryLocation: " + str(itemNum))
		print "Added " + str(wordsList[0] + shopType) + " to the " + str(shopType) + " shop menu"
		itemNum += 1
		temp.close()
	shopType = "Buy"
shopInfo.close()
#Makes all of the sell shops
spreadsheet.seek(0,0)
spreadsheet.readline()
itemNum = 0
lastGroup = "null"
for line in spreadsheet:
	wordsList = line.strip('\t\n\r').split("	")
	if lastGroup != wordsList[0]:
		itemNum = 0
	temp = open("shops/" + str(wordsList[0]) + "Sell.yml", "r+")
	temp.seek(0,2)
	temp.write("\n  " + str(wordsList[1]) + ":")
	temp.write("\n    MenuItem:")
	temp.write("\n    - lore:&4&1 Sell " + str(wordsList[2]) + " " + str(wordsList[1]) + "(s) for " + str(wordsList[3]) + "$")
	temp.write("\n    - name:&4&1" + wordsList[1])
	temp.write("\n    - amount:" + str(wordsList[2]))
	temp.write("\n    - type:" + str(dict[wordsList[1]]))
	temp.write("\n    RewardType: Money")
	temp.write("\n    Reward: " + str(wordsList[3]))
	temp.write("\n    PriceType: Item")
	temp.write("\n    Price:")
	temp.write("\n    - - amount:" + wordsList[2])
	temp.write("\n      - type:" + str(dict[wordsList[1]]))
	temp.write("\n    Message: ''")
	temp.write("\n    ExtraPermission: ''")
	temp.write("\n    InventoryLocation: " + str(itemNum))
	print "Added " + str(wordsList[1]) + " to the shop " + str(wordsList[0]) + "Sell"
	lastGroup = wordsList[0]
	temp.close()
	itemNum += 1
#Makes all of the buy shops
spreadsheet.seek(0,0)
spreadsheet.readline()
itemNum = 0
for line in spreadsheet:
	wordsList = line.strip('\t\n\r').split("	")
	if lastGroup != wordsList[0]:
		itemNum = 0
	temp = open("shops/" + str(wordsList[0]) + "Buy.yml", "r+")
	temp.seek(0,2)
	temp.write("\n  " + str(wordsList[1]) + ":")
	temp.write("\n    MenuItem:")
	temp.write("\n    - lore:&4&1 Purchase " + str(wordsList[2]) + " " + str(wordsList[1]) + "(s) for " + str(wordsList[3]) + "$")
	temp.write("\n    - name:&4&1" + wordsList[1])
	temp.write("\n    - amount:1")
	temp.write("\n    - type:" + str(dict[wordsList[1]]))
	temp.write("\n    RewardType: Item")
	temp.write("\n    Reward:")
	temp.write("\n    - - amount:" + wordsList[2])
	temp.write("\n      - type:" + str(dict[wordsList[1]]))
	temp.write("\n    PriceType: Money")
	temp.write("\n    Price: " + str(wordsList[3]))
	temp.write("\n    Message: ''")
	temp.write("\n    ExtraPermission: ''")
	temp.write("\n    InventoryLocation: " + str(itemNum))
	print "Added " + str(wordsList[1]) + " to the shop " + str(wordsList[0]) + "Buy"
	lastGroup = wordsList[0]
	temp.close()
	itemNum += 1
shopInfo = open("shopInfo.txt", "r")
shopType = "Sell"
#Finalizes all the shops
for i in ["1","2"]:
	shopInfo.seek(0,0)
	for line in shopInfo:
		wordsList = line.strip('\t\n\r').split(",")
		temp = open("shops/" + str(wordsList[0] + shopType) + ".yml", "r+")
		temp.seek(0,2)
		temp.write("\n  Back:")
		temp.write("\n    MenuItem:")
		temp.write("\n    - name:&4&lGo Back")
		temp.write("\n    - amount:1")
		temp.write("\n    - type:STAINED_GLASS_PANE")
		temp.write("\n    - durability:14")
		temp.write("\n    RewardType: Shop")
		temp.write("\n    Reward: ShopMenu")
		temp.write("\n    PriceType: Free")
		temp.write("\n    Message: ''")
		temp.write("\n    ExtraPermission: ''")
		temp.write("\n    InventoryLocation: 54")
		temp.write("\nShopName: " + str(wordsList[0] + shopType))
		temp.write("\nDisplayName: '&c&l" + wordsList[2] + "'")
		temp.write("\nsigns:")
		temp.write("\n  text: '[" + str(wordsList[0] + shopType) + "]'")
		temp.write("\n  NeedPermissionToCreateSign: true")
		temp.close()
	shopType = "Buy"
spreadsheet.close()