from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    #welcome page with a title 
    return "Genshin Impact Wishing Simulator"
    

@app.route('/ten', methods = ['GET', 'POST'])
def ten():
    #choices are 0 - 9 because its only measuring for out of 10 wishes
    choices = [0,1,2,3,4,5,6,7,8,9]
    #getting wich of the chosen choices the user picked
    if request.method == 'GET':
        return render_template('ten.html', choices = choices)
    
    if request.method == 'POST':
        #the amount of pity is the one the user selected
        pity = request.form['selected']
        return ten_wishes(int(pity))
    

def ten_wishes(pity: int) -> int:
    #i wanted to view the probability like a fraction
    #like there is 1 four star item guaranteed for every ten wishes, so i viewed it as 1/10
    #but for every previous wish, the pity gets higher
    #so the amount of pity would get taken out of the 10 so the probability would increase
    #then multiply by 100 so it can be represented by a number
    prob = (1/(10-pity))*100
    #returns string so the user can read their probabilty 
    return 'The probabilty of pulling a 4 star is a ' + str(prob) + '%' + ' chance!'

@app.route('/fifty', methods = ['GET', 'POST'])
def fifty():
    #for the user to say if they won or lost their last 50/50
    choices = ['won', 'lost']
    
    #gets the choice that the user picked
    if request.method == 'GET':
        return render_template('fifty.html', choices = choices)

    if request.method == 'POST':
        #the outcome is whatever the user selected
        outcome = request.form['selected']
        return fifty_fifty(str(outcome))
    
def fifty_fifty(outcome:str) -> str:
    #first lets see what woul happen if the user won their last 50/50
    if outcome == 'won':
        #think of it like flipping a coin with two heads
        #the probabilty of getting the same outcome twice is half of what it would have been
        #since it was a 1/2 chance before, you multiply 1/2 by itself to get a quarter
        return 'you have a 25% chance of winning your next 50/50'
    #outcome if the user lost
    if outcome == 'lost':
    #imagine four possible out comes
    #one where the user wins both
    #one where the user loses both
    #the other two, the user wins one and loses the other
    #the other two are 2/4 of the possible outcomes
    #so its a 50% chance 
        return 'you have a 50% chance of winning your next 50/50'



if __name__ == "__main__":
    print('wish value: ' + str(ten_wishes(5)))
    app.run(debug=True)