from flask import Flask, render_template, request 
import numpy as np 
from sklearn.linear_model import LinearRegression 
 
app = Flask(__name__) 
X_train = np.array([[1], [2], [3], [4], [5], [10]]) 
y_train = np.array([50, 60, 65, 75, 80, 98]) 
model = LinearRegression() 
model.fit(X_train, y_train) 
 
@app.route('/', methods=['GET', 'POST']) 
def dashboard(): 
    result = "Enter hours..." 
    if request.method == 'POST': 
        hours = float(request.form['hours']) 
        pred = model.predict([[hours]]) 
        result = f"Expected Score: {round(pred[0], 2)}%" 
    return render_template('dashboard.html', result=result)
if __name__ == '__main__': 
    app.run(debug=True) 