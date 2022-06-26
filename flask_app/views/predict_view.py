from flask import Blueprint, url_for
import pickle
from flask import render_template, request
from sklearn.ensemble import RandomForestClassifier

# from forms import MaterialsForm
from werkzeug.utils import redirect

bp = Blueprint('test', __name__, url_prefix='/predict')
model = pickle.load(open('airpollution.pkl', 'rb'))

#데이터 예측 처리
@bp.route('/predict', methods=['POST'])
def home():
    # form  = MaterialsForm()
    if request.method == 'POST':
        data1 = float(request.form['a'])
        data2 = float(request.form['b'])
        data3 = float(request.form['c'])
        data4 = float(request.form['d'])
        data5 = float(request.form['e'])
        data6 = float(request.form['f'])
        pred = model.predict([[data1, data2, data3, data4, data5, data6]])
        return render_template('after.html', data=pred) 

    else:
        return redirect(url_for('index.html'))
