OneFruit="Pineapple" 
for letters in OneFruit:   #for variable in sequence: that;s the sequence.
    print(letters)      
#if for the sequence veriable of the code has one string, 
# it will print all the letters consider each of them as a single value
Basket=["Banana", "water melon", "orange", "Mango"]
for fruits in Basket:      
    print(fruits)
#if for the sequence veriable of the code has Multiple strings set, 
# it will print all the strings consider each of them as a single value
for NumberOnly in range (0,18,3):  
#range(start, end before, step) it will start print from 0 end before 18 which is 15
    if NumberOnly == 5: #as step is 3, it will never touch 5 so it won't break
        break
    if NumberOnly ==6: #it will skip number 6 bcz of continue statement
        continue
    if NumberOnly >= 12: #it will break before the value 12. 12 won't print
        break
    print (NumberOnly) 
