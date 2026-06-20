"""
Simple Flask service for the CD final project.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Root endpoint returning a welcome message."""
    return jsonify(message="Welcome to the CD Final Project"), 200


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify(status="OK"), 200


def add_numbers(a, b):
    """Simple helper function used to demonstrate unit testing."""
    return a + b
