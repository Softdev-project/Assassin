from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')

# Route that will process the AJAX request, sum up two
# integer numbers (defaulted to zero) and return the
# result as a proper JSON response (Content-Type, etc.)

@app.route('/target')
def target():
    #Recieves lat and lng
    mylat = request.args.get('mylat', 0, type=int)
    mylng = request.args.get('mylng', 0, type=int)
    #You can add to mongo here
    
    return jsonify(result=mylat + mylng)#optional if you want to return data
    print mylat
    print mylng
    
if __name__ == '__main__':
    app.debug = True
    app.run(host = "127.0.0.1", port = 8000)
