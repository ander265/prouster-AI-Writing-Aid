from flask import Flask, render_template
import textgenerator



tg = textgenerator.TextGenerator('tg.h5','documents.h5')
print(tg.generate_text())
app = Flask(__name__)

@app.route('/')
def index():
    text = tg.generate_text()
    return render_template('website.html', neural_network_output=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=False)