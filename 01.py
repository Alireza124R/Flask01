from flask import Flask, jsonify

main = Flask(__name__)
                                        
@main.route("/")
def sayhello():
    return jsonify ({"Name" : "Alireza",
                     "ID" : "Alireza124R" })

if __name__ == '__main__':
    main.run(debug=True)
