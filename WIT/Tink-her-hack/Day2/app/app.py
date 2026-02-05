from flask import Flask,render_template,request
import random
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def team_generator():
    generated_name=''
    if request.method=='POST':
        color=request.form.get('user_color')
        animal=request.form.get('user_animal')
        if color and animal:
            generated_name=f"THE {color.capitalize()}{animal.capitalize()}s"
    return render_template('team.html',final_name=generated_name)
if __name__=='__main__':
    app.run(debug=True) 