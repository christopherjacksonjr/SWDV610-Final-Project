#Import statements,
from graphics import *
from groceryItem import GroceryItem

#Global variable declarations.
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
SHOPPING_CART_Y_AXIS = 450

#Function to build graphics window.
def buildWindow():
    window = GraphWin("Nutrtion Guide", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground("Black")
    
    return window

#Function to build input box for user entry.
def buildInputBox(window):
    inputBox = Entry(Point(350, 350), 12)
    inputBox.setSize(18)
    inputBox.setStyle("italic")
    inputBox.setTextColor("White")
    inputBox.draw(window)
    
    return inputBox

#Function to build user instructions.
def buildPromptText(window):
    promptText = Text(Point(350, 320), "Enter an item then press enter.")
    promptText.setTextColor("White")
    promptText.draw(window)
    
    return promptText

#Function to get text from user input box. 
def buildTextFromUserPoint(window):
    textFromUser = Text(Point(350, 380), "")
    textFromUser.setTextColor("White")
    textFromUser.draw(window)
    
    return textFromUser

#Function to build nutrition facts column title.
def buildNutritionFactsTitleText(window):
    nutritionTitleText = Text(Point(150, 420), "Nutrition Facts")
    nutritionTitleText.setTextColor("White")
    nutritionTitleText.draw(window)
    
#Function to build nutrition facts item name attribute text.   
def buildNutritionFactsItemNameText(window):
    nutritionFactsItemNameText = Text(Point(150, 450), "Item:")
    nutritionFactsItemNameText.setTextColor("White")
    nutritionFactsItemNameText.draw(window)
    
    return nutritionFactsItemNameText

#Function to build nutrition facts item grade attribute text.
def buildNutritionFactsItemGradeText(window):
    nutritionFactsItemGradeText = Text(Point(150, 470), "Item Grade:")
    nutritionFactsItemGradeText.setTextColor("White")
    nutritionFactsItemGradeText.draw(window)
    
    return nutritionFactsItemGradeText

#Function to build nutrition facts item serving size attribute text.
def buildNutritionFactsServingSizeText(window):
    nutritionFactsServingSizeText = Text(Point(150, 490), "Serving Size:")
    nutritionFactsServingSizeText.setTextColor("White")
    nutritionFactsServingSizeText.draw(window)
    
    return nutritionFactsServingSizeText

#Function to build nutrition facts item calories attribute text.
def buildNutritionFactsCaloriesText(window):
    nutritionFactsCaloriesText = Text(Point(150, 510), "Calories:")
    nutritionFactsCaloriesText.setTextColor("White")
    nutritionFactsCaloriesText.draw(window)
    
    return nutritionFactsCaloriesText

#Function to build nutrition facts item total fat attribute text.
def buildNutritionFactsTotalFatText(window):
    nutritionFactsTotalFatText = Text(Point(150, 530), "Total Fat:")
    nutritionFactsTotalFatText.setTextColor("White")
    nutritionFactsTotalFatText.draw(window)
    
    return nutritionFactsTotalFatText

#Function to build nutrition facts item cholesterol attribute text.
def buildNutritionFactsCholesterolText(window):
    nutritionFactsCholesterolText = Text(Point(150, 550), "Cholesterol:")
    nutritionFactsCholesterolText.setTextColor("White")
    nutritionFactsCholesterolText.draw(window)
    
    return nutritionFactsCholesterolText

#Function to build nutrition facts item sodium attribute text.
def buildNutritionFactsSodiumText(window):
    nutritionFactsSodiumText = Text(Point(150, 570), "Sodium:")
    nutritionFactsSodiumText.setTextColor("White")
    nutritionFactsSodiumText.draw(window)
    
    return nutritionFactsSodiumText
 
#Function to build nutrition facts item potassium attribute text. 
def buildNutritionFactsPotassiumText(window):
    nutritionFactsPotassiumText = Text(Point(150, 590), "Potassium:")
    nutritionFactsPotassiumText.setTextColor("White")
    nutritionFactsPotassiumText.draw(window)
    
    return nutritionFactsPotassiumText

#Function to build nutrition facts item carbohydrate attribute text.
def buildNutritionFactsTotalCarbohydrateText(window):
    nutritionFactsTotalCarbohydrateText = Text(Point(150, 610), "Total Carbohydrate:")
    nutritionFactsTotalCarbohydrateText.setTextColor("White")
    nutritionFactsTotalCarbohydrateText.draw(window)
    
    return nutritionFactsTotalCarbohydrateText

#Function to build nutrition facts item dietary fiber attribute text.
def buildNutritionFactsDietaryFiberText(window):
    nutritionFactsDietaryFiberText = Text(Point(150, 630), "Dietary Fiber:")
    nutritionFactsDietaryFiberText.setTextColor("White")
    nutritionFactsDietaryFiberText.draw(window)
    
    return nutritionFactsDietaryFiberText

#Function to build nutrition facts item sugar attribute text.
def buildNutritionFactsSugarText(window):
    nutritionFactsSugarText = Text(Point(150, 650), "Sugar:")
    nutritionFactsSugarText.setTextColor("White")
    nutritionFactsSugarText.draw(window)
    
    return nutritionFactsSugarText

#Function to build nutrition facts item protein attribute text.
def buildNutritionFactsProteinText(window):
    nutritionFactsProteinText = Text(Point(150, 670), "Protein:")
    nutritionFactsProteinText.setTextColor("White")
    nutritionFactsProteinText.draw(window)
    
    return nutritionFactsProteinText

#Function to build all nutrition facts text.
def buildNutritionText(window):
    nutritionFactsItemsText = []
    
    buildNutritionFactsTitleText(window)
    
    nutritionFactsItemNameText = buildNutritionFactsItemNameText(window)
    nutritionFactsItemsText.append(nutritionFactsItemNameText)
    
    nutritionFactsItemGradeText = buildNutritionFactsItemGradeText(window)
    nutritionFactsItemsText.append(nutritionFactsItemGradeText)
    
    nutritionFactsServingSizeText = buildNutritionFactsServingSizeText(window)
    nutritionFactsItemsText.append(nutritionFactsServingSizeText)
    
    nutritionFactsCaloriesText = buildNutritionFactsCaloriesText(window)
    nutritionFactsItemsText.append(nutritionFactsCaloriesText)
    
    nutritionFactsTotalFatText = buildNutritionFactsTotalFatText(window)
    nutritionFactsItemsText.append(nutritionFactsTotalFatText)
    
    nutritionFactsCholesterolText = buildNutritionFactsCholesterolText(window)
    nutritionFactsItemsText.append(nutritionFactsCholesterolText)
    
    nutritionFactsSodiumText = buildNutritionFactsSodiumText(window)
    nutritionFactsItemsText.append(nutritionFactsSodiumText)
    
    nutritionFactsPotassiumText = buildNutritionFactsPotassiumText(window)
    nutritionFactsItemsText.append(nutritionFactsPotassiumText)
    
    nutritionFactsTotalCarbohydrateText = buildNutritionFactsTotalCarbohydrateText(window)
    nutritionFactsItemsText.append(nutritionFactsTotalCarbohydrateText)
    
    nutritionFactsDietaryFiberText = buildNutritionFactsDietaryFiberText(window)
    nutritionFactsItemsText.append(nutritionFactsDietaryFiberText)
    
    nutritionFactsSugarText = buildNutritionFactsSugarText(window)
    nutritionFactsItemsText.append(nutritionFactsSugarText)
    
    nutritionFactsProteinText = buildNutritionFactsProteinText(window)
    nutritionFactsItemsText.append(nutritionFactsProteinText)
    
    return nutritionFactsItemsText

#Function to set nutrition facts using grocery item.
def setNutrtionFactsText(groceryItem, nutritionFactsItemsText):
    nutritionFactsItemsText[0].setText("Item: " + groceryItem.itemName)
    nutritionFactsItemsText[1].setText("Item Grade: " + str(groceryItem.itemGrade) + " g")
    nutritionFactsItemsText[2].setText("Serving Size: " + str(groceryItem.servingSize) + " g")
    nutritionFactsItemsText[3].setText("Calories: " + str(groceryItem.calories))
    nutritionFactsItemsText[4].setText("Total Fat: " + str(groceryItem.totalFat) + " g")
    nutritionFactsItemsText[5].setText("Cholesterol: " + str(groceryItem.cholesterol) + " mg")
    nutritionFactsItemsText[6].setText("Sodium: " + str(groceryItem.sodium) + " mg")
    nutritionFactsItemsText[7].setText("Potassium: " + str(groceryItem.potassium) + " g")
    nutritionFactsItemsText[8].setText("Total Carbohydrate: " + str(groceryItem.totalCarbohydrates) + " g")
    nutritionFactsItemsText[9].setText("Dietary Fiber: " + str(groceryItem.dietaryFiber) + " g")
    nutritionFactsItemsText[10].setText("Sugar: " + str(groceryItem.sugar) + " g")
    nutritionFactsItemsText[11].setText("Protein: " + str(groceryItem.protein) + " g")

#Function to build shopping cart title text.
def buildShoppingCartTitleText(window):
    shoppingCartTitleText = Text(Point(500, 420), "Shopping Cart")
    shoppingCartTitleText.setTextColor("White")
    shoppingCartTitleText.draw(window)

#Function to build shopping cart columns title text.
def buildShoppingCartColumnsTitleText(window):
    shoppingCartItemText = Text(Point(450, SHOPPING_CART_Y_AXIS), "Item")
    shoppingCartItemText.setTextColor("White")
    shoppingCartItemText.draw(window)
    
    shoppingCartGradeText = Text(Point(550, SHOPPING_CART_Y_AXIS), "Gade")
    shoppingCartGradeText.setTextColor("White")
    shoppingCartGradeText.draw(window)

#Function to build shopping cart total grade title text.
def buildShoppingCartTotalGradeTitleText(window):
    shoppingCartTotalGradeTitleText = Text(Point(520, 350), "Total Grade: ")
    shoppingCartTotalGradeTitleText.setSize(22)
    shoppingCartTotalGradeTitleText.setTextColor("White")
    shoppingCartTotalGradeTitleText.draw(window)

#Function to build shopping cart total grade text.
def buildShoppingCartTotalGradeText(window):
    shoppingCartTotalGradeText = Text(Point(610, 350), "0")
    shoppingCartTotalGradeText.setSize(22)
    shoppingCartTotalGradeText.setTextColor("White")
    shoppingCartTotalGradeText.draw(window)
    
    return shoppingCartTotalGradeText

#Function to update shopping cart total grade text.
def updateShoppingCartTotalGrade(shoppingCartTotalGradeText, itemsInShoppingCart):
    totalPercentage = 0
    
    for item in itemsInShoppingCart:
        totalPercentage += item.itemGrade
    
    totalGrade = '{:.1f}'.format((totalPercentage/len(itemsInShoppingCart)))
    
    shoppingCartTotalGradeText.setText(str(totalGrade))
    
    return totalGrade

#Function to add item to shopping cart.
def addItemToShoppingCart(window, groceryItem, numberOfItemsInCart, promptText):
    if(numberOfItemsInCart > 10):
        itemsExceededResponse(window, promptText)
    else:
        itemYAxis = SHOPPING_CART_Y_AXIS + (20 * numberOfItemsInCart)
        quantityYAxis = SHOPPING_CART_Y_AXIS + (20 * numberOfItemsInCart)
        gradeYAxis = SHOPPING_CART_Y_AXIS + (20 * numberOfItemsInCart)
        
        shoppingCartItemNameText = Text(Point(450, itemYAxis), groceryItem.itemName)
        shoppingCartItemNameText.setTextColor("White")
        shoppingCartItemNameText.draw(window)
        
        shoppingCartGradeText = Text(Point(550, gradeYAxis), str(groceryItem.itemGrade))
        shoppingCartGradeText.setTextColor("White")
        shoppingCartGradeText.draw(window)

#Function to build all shopping cart titles.
def buildShoppingCartTitles(window):
    buildShoppingCartTitleText(window)
    buildShoppingCartColumnsTitleText(window)
    buildShoppingCartTotalGradeTitleText(window)

#Function to build motivation text.
def buildMotivationText(window):
    motivationText = Text(Point(150, 350), "")
    motivationText.setSize(22)
    motivationText.setTextColor("White")
    motivationText.draw(window)
    
    return motivationText

#Function to update motivation text.
def updateMotivationText(motivationText, totalGrade):
    totalGradeNumber = float(totalGrade)
    
    if(totalGradeNumber >= 90.0):
        motivationText.setText("Excellent choices!")
    elif(totalGradeNumber < 90.0 and totalGradeNumber >= 80.0):
        motivationText.setText("Great job!")
    elif(totalGradeNumber < 80.0 and totalGradeNumber >= 70.0):
        motivationText.setText("Room for improvement.")
    elif(totalGradeNumber < 70.0 and totalGradeNumber >= 60.0):
        motivationText.setText("Revisit your choices.")
    elif(totalGradeNumber < 60.0 and totalGradeNumber >= 50.0):
        motivationText.setText("Bad decisions.")
    else:
        motivationText.setText("Do better next time.")
        
#Function to produce error when user tries to enter empty entry.
def emptyEntryResponse(window, promptText):
    promptText.setText("ERROR: Invalid entry. Enter an item then press enter.")
    promptText.setTextColor("Red")
    
#Function to produce message when unknown item entered.
def unknownEntryResponse(window, promptText):
    promptText.setText("Item entered not recognized - wildcard. Enter an item then press enter.")
    promptText.setTextColor("white")
    
def itemsExceededResponse(window, promptText):
    promptText.setText("Max number of shopping cart items reached.")
    promptText.setTextColor("white")

#Function to reset prompt text to user.
def resetPromptText(window, promptText):
    promptText.setText("Enter an item then press enter.")
    promptText.setTextColor("White")

#Function to reset user input box.
def resetInputBox(window, inputBox):
    inputBox.setText("")

#Function to reset text from user.
def resetTextFromUserPoint(window, textFromUser):
    textFromUser.setText("")

#Function to decide which item to populate details for.
def populateGroceryItemDetails(groceryItem, window, promptText):
    if(groceryItem.itemName == "orange"):
        populateOrangeItemDetails(groceryItem)
    elif(groceryItem.itemName == "apple"):
         populateAppleItemDetails(groceryItem)
    elif(groceryItem.itemName == "bread"):
         populateBreadItemDetails(groceryItem)
    elif(groceryItem.itemName == "milk"):
         populateMilkItemDetails(groceryItem)
    elif(groceryItem.itemName == "butter"):
         populateButterItemDetails(groceryItem)
    elif(groceryItem.itemName == "eggs"):
         populateEggsItemDetails(groceryItem)
    elif(groceryItem.itemName == "beer"):
         populateBeerItemDetails(groceryItem)
    elif(groceryItem.itemName == "wine"):
         populateWineItemDetails(groceryItem)
    elif(groceryItem.itemName == "chicken breast"):
         populateChickenBreastItemDetails(groceryItem)
    elif(groceryItem.itemName == "spinach"):
         populateSpinachItemDetails(groceryItem)
    elif(groceryItem.itemName == "kale"):
         populateKaleItemDetails(groceryItem)
    elif(groceryItem.itemName == "soda"):
         populateSodaItemDetails(groceryItem)
    elif(groceryItem.itemName == "juice"):
         populateJuiceItemDetails(groceryItem)
    elif(groceryItem.itemName == "water"):
         populateWaterItemDetails(groceryItem)
    elif(groceryItem.itemName == "cheese"):
         populateCheeseItemDetails(groceryItem)
    else:
        unknownEntryResponse(window, promptText)
        populateWildCarItemDetails(groceryItem)

#Function to populate items for oranges.
def populateOrangeItemDetails(groceryItem):
    groceryItem.itemGrade = 100
    groceryItem.foodGroup = "Produce"
    groceryItem.servingSize = 96
    groceryItem.calories = 45
    groceryItem.totalFat = 0.1
    groceryItem.cholesterol = 0
    groceryItem.sodium = 0
    groceryItem.potassium = 174
    groceryItem.totalCarbohydrates = 11
    groceryItem.dietaryFiber = 2.3
    groceryItem.sugar = 9
    groceryItem.protein = 0.9

#Function to populate items for apples.
def populateAppleItemDetails(groceryItem):
    groceryItem.itemGrade = 100
    groceryItem.foodGroup = "Produce"
    groceryItem.servingSize = 182
    groceryItem.calories = 95
    groceryItem.totalFat = 0.3
    groceryItem.cholesterol = 0
    groceryItem.sodium = 2
    groceryItem.potassium = 195
    groceryItem.totalCarbohydrates = 25
    groceryItem.dietaryFiber = 4.4
    groceryItem.sugar = 19
    groceryItem.protein = 0.5

#Function to populate items for bread.
def populateBreadItemDetails(groceryItem):
    groceryItem.itemGrade = 60
    groceryItem.foodGroup = "Grain"
    groceryItem.servingSize = 182
    groceryItem.calories = 95
    groceryItem.totalFat = 0.3
    groceryItem.cholesterol = 0
    groceryItem.sodium = 2
    groceryItem.potassium = 195
    groceryItem.totalCarbohydrates = 25
    groceryItem.dietaryFiber = 4.4
    groceryItem.sugar = 19
    groceryItem.protein = 0.5
    
#Function to populate items for milk.
def populateMilkItemDetails(groceryItem):
    groceryItem.itemGrade = 70
    groceryItem.foodGroup = "Dairy"
    groceryItem.servingSize = 244
    groceryItem.calories = 103
    groceryItem.totalFat = 2.4
    groceryItem.cholesterol = 12
    groceryItem.sodium = 107
    groceryItem.potassium = 366
    groceryItem.totalCarbohydrates = 12
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 13
    groceryItem.protein = 8
    
#Function to populate items for butter.
def populateButterItemDetails(groceryItem):
    groceryItem.itemGrade = 50
    groceryItem.foodGroup = "Dairy"
    groceryItem.servingSize = 14.2
    groceryItem.calories = 102
    groceryItem.totalFat = 12
    groceryItem.cholesterol = 31
    groceryItem.sodium = 2
    groceryItem.potassium = 3
    groceryItem.totalCarbohydrates = 0
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 0
    groceryItem.protein = 0.1
    
#Function to populate items for eggs.
def populateEggsItemDetails(groceryItem):
    groceryItem.itemGrade = 80
    groceryItem.foodGroup = "Dairy"
    groceryItem.servingSize = 50
    groceryItem.calories = 78
    groceryItem.totalFat = 5
    groceryItem.cholesterol = 187
    groceryItem.sodium = 62
    groceryItem.potassium = 63
    groceryItem.totalCarbohydrates = 0.6
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 0
    groceryItem.protein = 6
    
#Function to populate items for beer.
def populateBeerItemDetails(groceryItem):
    groceryItem.itemGrade = 0
    groceryItem.foodGroup = "Alcohol"
    groceryItem.servingSize = 356
    groceryItem.calories = 154
    groceryItem.totalFat = 0
    groceryItem.cholesterol = 0
    groceryItem.sodium = 14
    groceryItem.potassium = 96
    groceryItem.totalCarbohydrates = 13
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 0
    groceryItem.protein = 1.6
    
#Function to populate items for wine.
def populateWineItemDetails(groceryItem):
    groceryItem.itemGrade = 0
    groceryItem.foodGroup = "Alcohol"
    groceryItem.servingSize = 148
    groceryItem.calories = 123
    groceryItem.totalFat = 0
    groceryItem.cholesterol = 0
    groceryItem.sodium = 7
    groceryItem.potassium = 147
    groceryItem.totalCarbohydrates = 4
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 1.2
    groceryItem.protein = 0.1
    
#Function to populate items for chicken breast.
def populateChickenBreastItemDetails(groceryItem):
    groceryItem.itemGrade = 90
    groceryItem.foodGroup = "Poultry"
    groceryItem.servingSize = 140
    groceryItem.calories = 335
    groceryItem.totalFat = 19
    groceryItem.cholesterol = 123
    groceryItem.sodium = 115
    groceryItem.potassium = 312
    groceryItem.totalCarbohydrates = 0
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 0
    groceryItem.protein = 38
    
#Function to populate items for spinach.
def populateSpinachItemDetails(groceryItem):
    groceryItem.itemGrade = 100
    groceryItem.foodGroup = "Produce"
    groceryItem.servingSize = 100
    groceryItem.calories = 23
    groceryItem.totalFat = 0
    groceryItem.cholesterol = 0
    groceryItem.sodium = 25
    groceryItem.potassium = 558
    groceryItem.totalCarbohydrates = 1
    groceryItem.dietaryFiber = 1
    groceryItem.sugar = 0
    groceryItem.protein = 2.9
    
#Function to populate items for kale.
def populateKaleItemDetails(groceryItem):
    groceryItem.itemGrade = 100
    groceryItem.foodGroup = "Produce"
    groceryItem.servingSize = 67
    groceryItem.calories = 33
    groceryItem.totalFat = 0.6
    groceryItem.cholesterol = 0
    groceryItem.sodium = 25
    groceryItem.potassium = 329
    groceryItem.totalCarbohydrates = 6
    groceryItem.dietaryFiber = 2.6
    groceryItem.sugar = 1.6
    groceryItem.protein = 2.9
    
#Function to populate items for soda.
def populateSodaItemDetails(groceryItem):
    groceryItem.itemGrade = 0
    groceryItem.foodGroup = "Junk Food"
    groceryItem.servingSize = 368
    groceryItem.calories = 150
    groceryItem.totalFat = 0
    groceryItem.cholesterol = 0
    groceryItem.sodium = 15
    groceryItem.potassium = 11
    groceryItem.totalCarbohydrates = 39
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 39
    groceryItem.protein = 0
    
#Function to populate items for juice.
def populateJuiceItemDetails(groceryItem):
    groceryItem.itemGrade = 0
    groceryItem.foodGroup = "Junk Food"
    groceryItem.servingSize = 249
    groceryItem.calories = 136
    groceryItem.totalFat = 0
    groceryItem.cholesterol = 0
    groceryItem.sodium = 5
    groceryItem.potassium = 105
    groceryItem.totalCarbohydrates = 33
    groceryItem.dietaryFiber = 0.5
    groceryItem.sugar = 23
    groceryItem.protein = 0.5
    
#Function to populate items for water.
def populateWaterItemDetails(groceryItem):
    groceryItem.itemGrade = 100
    groceryItem.foodGroup = "Water"
    groceryItem.servingSize = 237
    groceryItem.calories = 0
    groceryItem.totalFat = 0
    groceryItem.cholesterol = 0
    groceryItem.sodium = 12
    groceryItem.potassium = 0
    groceryItem.totalCarbohydrates = 0
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 0
    groceryItem.protein = 0
    
#Function to populate items for cheese.
def populateCheeseItemDetails(groceryItem):
    groceryItem.itemGrade = 40
    groceryItem.foodGroup = "Dairy"
    groceryItem.servingSize = 28
    groceryItem.calories = 113
    groceryItem.totalFat = 9
    groceryItem.cholesterol = 29
    groceryItem.sodium = 174
    groceryItem.potassium = 27
    groceryItem.totalCarbohydrates = 0.4
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 0.1
    groceryItem.protein = 7
    
#Function to populate items for juice.
def populateWildCarItemDetails(groceryItem):
    groceryItem.itemGrade = 100
    groceryItem.foodGroup = "Unknown"
    groceryItem.servingSize = 0
    groceryItem.calories = 0
    groceryItem.totalFat = 0
    groceryItem.cholesterol = 0
    groceryItem.sodium = 0
    groceryItem.potassium = 0
    groceryItem.totalCarbohydrates = 0
    groceryItem.dietaryFiber = 0
    groceryItem.sugar = 0
    groceryItem.protein = 0
    
def displayHeadline(window):
    headlineText = Text(Point(355, 100), "Nutrition\nGuide")
    headlineText.setTextColor("White")
    headlineText.setSize(36)
    headlineText.draw(window)

#Defining main function.
def main():
    #Calling functions to build UI before user begins entry.
    window = buildWindow()

    inputBox = buildInputBox(window)

    promptText = buildPromptText(window)

    textFromUser = buildTextFromUserPoint(window)
    
    nutritionFactsItemsText = buildNutritionText(window)
    
    buildShoppingCartTitles(window)
    
    shoppingCartTotalGradeText = buildShoppingCartTotalGradeText(window)
    
    motivationText = buildMotivationText(window)
    
    displayHeadline(window)
    
    numberOfItemsInCart = 0
    
    #Creating a queue of entry items and a queue of groceryItems in shopping cart.
    queueOfItems = []
    itemsInShoppingCart = []

    #While loop that allows continous input from user.
    while True:
        #Defines key that will determine when the user entered enter to grab text from input box.
        key = window.checkKey()
        
        if key == "Return":
            #Defind variable for user input and check if it's empty or if the user entered exit.
            entry = inputBox.getText()
            
            if(entry == "" or entry == " "):
                emptyEntryResponse(window, promptText)
                resetTextFromUserPoint(window, textFromUser)
            elif(entry == "exit"):
                window.close()
            else:
                #If it's not empty check if the entry is already in the list or not.
                if(entry in queueOfItems):
                    #Item is in the list so update quantity and reset text.
                    groceryItem.quantity += 1
                    setNutrtionFactsText(groceryItem, nutritionFactsItemsText)
                    resetPromptText(window, promptText)
                    resetInputBox(window, inputBox)
                    textFromUser.setText(entry + " added to cart.")
                else:
                    #New item so create grocery item, add to shopping cart, compute total grade, and reset text.
                    numberOfItemsInCart += 1
                    groceryItem = GroceryItem(entry)
                    itemsInShoppingCart.append(groceryItem)
                    populateGroceryItemDetails(groceryItem, window, promptText)
                    setNutrtionFactsText(groceryItem, nutritionFactsItemsText)
                    addItemToShoppingCart(window, groceryItem, numberOfItemsInCart, promptText)
                    totalGrade = updateShoppingCartTotalGrade(shoppingCartTotalGradeText, itemsInShoppingCart)
                    updateMotivationText(motivationText, totalGrade)
                    resetPromptText(window, promptText)
                    resetInputBox(window, inputBox)
                    textFromUser.setText(entry + " added to cart.")
                    queueOfItems.append(entry)
    
    window.close()

#Calling main function.
main()