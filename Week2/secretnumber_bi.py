low = 0
high = 100
epsilon = 0.0
x = 50
print('Please think of a number between 0 & 100')
print'Is your secret number ' +  str(x)   + ' ? '
guess = raw_input('Enter "h" to indicate the guess is too high.  Enter "1" to indicate the guess is too low.  Enter "c" to indicate I guessed correctly: ')

while guess != 'c':
    if guess == 'h':
        high = x
        x = x - (round(high-low)/2)
        x = int(x)
        print 'Is your secret number ' +  str(x)   + ' ? :'
        guess = raw_input('Enter "h" to indicate the guess is too high.  Enter "1" to indicate the guess is too low.  Enter "c" to indicate I guessed correctly: ')
    elif guess == 'l':
        low = x
        x = (high-low)/2 + x
        print 'Is your secret number ' +  str(x)   + ' ? '
        guess = raw_input('Enter "h" to indicate the guess is too high.  Enter "1" to indicate the guess is too low.  Enter "c" to indicate I guessed correctly: ')
    else:
        print "You must choose correct character."
        print 'Is your secret number ' +  str(x)   + ' ? :'
        guess = raw_input('Enter "h" to indicate the guess is too high.  Enter "1" to indicate the guess is too low.  Enter "c" to indicate I guessed correctly: ')    
print 'Game over.  Your secret number was x' 
     



   

    
    


