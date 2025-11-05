from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/square', methods=['GET', 'POST'])
def squarenumber():
    if request.method == 'POST':
        num = request.form.get('num')
    elif request.method == 'GET':
         num = request.args.get('num')

    square = None
    error = None

    if num:  # If something is entered
        try:
            square = int(num) ** 2
        except ValueError:
            error = "Invalid input. Please enter a valid number."

    # Render the same template with variables
    return render_template('squarenum.html', num=num, square=square, error=error)
    
if __name__ == '__main__':
    app.run(debug=True)