from flask import Blueprint, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

bp = Blueprint('predict', __name__, url_prefix='/predict')
model = pickle.load(open('flask_app/model/model.pkl', 'rb'))


@bp.route('/', methods=['POST','GET'])
def pred():
    if request.method == 'POST':
               
        arr = [{"id": request.form["id"],
            "amount_tsh": request.form["amount_tsh"],
            "construction_year": request.form["construction_year"],
            "extraction_type": request.form["extraction_type"],
            "source_type": request.form["source_type"],
            "waterpoint_type": request.form["waterpoint_type"],
            "management": request.form["management"],
            "payment_type": request.form["payment_type"],
            "quality": request.form["quality"],
            "quantity": request.form["quantity"],
            "populaion": request.form["populaion"],
            "public_meeting": request.form["public_meeting"]}]


        # data1 = request.form["id"]
        # data2 = request.form["amount_tsh"]
        # data3 = request.form["construction_year"]
        # data4 = request.form["extraction_type"]
        # data5 = request.form["source_type"]
        # data6 = request.form["waterpoint_type"]
        # data7 = request.form["management"]
        # data8 = request.form["payment_type"]
        # data9 = request.form["quality"]
        # data10 = request.form["quantity"]
        # data11 = request.form["populaion"]
        # data12 = request.form["public_meeting"]
        # arr = np.array([[data1, data2, data3, data4,
        #                 data5, data6, data7, data8,
        #                 data9, data10, data11, data12]])
        X_test = pd.DataFrame(arr)
        # x = request.form
        # for key, value in x.items:
        #     X_test[key] = value
        prediction = model.predict(X_test)
        
    return render_template('predict.html', data = prediction)