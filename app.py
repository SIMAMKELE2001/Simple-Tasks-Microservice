from flask import Flask, request, jsonify
app =Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to the home page!"