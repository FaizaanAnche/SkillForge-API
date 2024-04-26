from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('decision_tree_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Extracting features from the request
    student_ability = data['student_ability']
    curr_question_diff = data['curr_question_diff']
    ans_status = data['ans_status']
    
    # Making prediction using the loaded model
    next_question_diff = model.predict([[student_ability, curr_question_diff, ans_status]])
    
    # Returning the prediction as JSON response
    return jsonify({'next_question_diff': next_question_diff[0]})

if __name__ == '__main__':
    app.run(debug=True)
