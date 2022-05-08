from flask import Flask, request
import json

app = Flask(__name__)

#route to test with post method
@app.route('/test', methods=['Post'])

#to return JSON object
def processJSON():
    string_to_cut = request.json['string_to_cut']
    return_string = stringCut(string_to_cut)
    json_return = {"return_string": return_string}
    return json.dumps(json_return)

#to return string with every thrid letter
def stringCut(string):
    count = 0
    result = []
    for letter in string:
        count += 1
        if count == 3:
            result.append(letter)
            count = 0
    return "".join(result)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
