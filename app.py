from flask import Flask, request, jsonify

app = Flask(__name__)

# Example "database"
users = {
    "test@example.com": "123456"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email in users and users[email] == password:
        return jsonify({"status": "success", "message": "Login successful"})
    else:
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)