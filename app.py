from flask import Flask, escape, request, render_template
import pickle

vec=pickle.load(open("vector_i.pkl","rb"))



model=pickle.load(open("finalize_model.pkl","rb"))

app = Flask(__name__)  # creating the Flask class object


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Prediction')
def prediction():
    if request.method =="POST":
        news=request.form['news']
        print(news)

        return render_template("prediction.html", prediction_text="News headline id ->{}".format(prediction))

    else:
        return render_template("prediction.html")








if __name__ == '__main__':
    app.run()
