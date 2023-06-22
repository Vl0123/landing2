from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    email = request.form['email']
    country_code = request.form['country_code']
    phone = request.form['phone']
    location = request.form['location']
    ip_address = request.remote_addr

    # Здесь вы можете выполнить дополнительные действия с полученными данными
    # Например, отправить их в MPC или выполнить другие операции

    # Пример вывода полученных данных в консоль
    print('Имя:', f_name)
    print('Фамилия:', l_name)
    print('Email:', email)
    print('Country Code:', country_code)
    print('Phone:', phone)
    print('Локация:', location)
    print('IP Address:', ip_address)

    url = "https://tr.pafnet.tech/api/signup/procform"

    payload = {
        "ai": "2958116",
        "ci": "1",
        "gi": "108",
        "userip": ip_address,
        "firstname": "Gnanapiasam",
        "lastname": "Johnsasdhan",
        "email": "tesfaf321@gmail.com",
        "password": "Aa12345!",
        "phone": "4407012259886",
        "so": "funnelname",
        "sub": "FreeParam",
        "MPC_1": f_name + " " + l_name,
        "MPC_2": country_code+phone,
        "MPC_3": email,
        "MPC_4": "Гражданство " + location,
        "MPC_5": "Binance",
        "MPC_6": "None",
        "MPC_7": "None",
        "MPC_8": "None",
        "MPC_9": "None",
        "MPC_10": "None"
    }

    headers = {
        'x-trackbox-username': 'ILLIAWEB',
        'x-trackbox-password': 'xjkkgnjTUTY23',
        'x-api-key': '2643889w34df345676ssdas323tgc738',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print(response.text)

    return render_template("thanks.html")

if __name__ == '__main__':
    app.run()
