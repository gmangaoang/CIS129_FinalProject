#Gregorio Mangaoang
#5 May 2025
#This program allows the user to input a pc part and the cost of it. The program then compares it to the avarage price found online for that part. It will output the avgerage price, how much the user got it for and the percentage of the money gained or lost if the item was bought.

'''

Import files that has data on pc parts and their average price online

Global Variables
prompt = 'Enter your PC part: '
price_prompt = 'How much did you get it for? '
user_price = 0
avg_price = 0
difference = 0


FUNCTION Main Function()

    Get USER PC item
    prompt = get_part(prompt, user_price)
    Printing the Output
    calculate(prompt, user_price)
    
end FUNCTION
    
FUNCTION calculate(PROMPT, USER_PRICE)

    prompt, avg_price = find_in_files(prompt, avg_price)
    difference = user_price - avg_price
    
    percentage = calculate the percentage of the increase or decrease of the user_price to the avg_price
    IF the price is over the avg_price
        print(difference, percentage)
        let the user know they're over paying for their item
    end IF
    ELIF the price is under the avg_price
        print(difference, percentage)
        let the user know their making a good choice
    end ELIF
    
end FUNCTION


FUNCTIION get_part(prompt, user_price)

    prompt = get_USER_PART(prompt)
    prompt = get_USER_PRICE(prompt)
    
end FUNCTION


FUNCTION get_USER_PART(prompt)

    prompt = input(prompt)
    WHILE find_in_files(prompt)
        print 'Item not FOUND!!!'
        repeat question
    end WHILE
    RETURN prompt
    
end FUNCTION

FUNCTION find_in_files(prompt, avg_price)
    
    Opening the file in reading
    Look for PC part in file imported and the avgerage price it has
    IF item is found THEN
        RETURN prompt , avg_price
    end IF
    ELIF the item is not found THEN 
        Print the ERROR
        RETURN false
    end ELIF

end FUNCTION

FUNCTION get_USER_PRICE(prompt)
    WHILE true DO
        TRY
            prompt = float(input(prompt))
            RETURN prompt
        end TRY
        EXCEPT ValueError
            print 'NOT Readable : Must be a valid Number' 
        end EXCEPT
    end WHILE
end FUNCTION

'''