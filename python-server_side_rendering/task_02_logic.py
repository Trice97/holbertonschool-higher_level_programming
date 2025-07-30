#!/usr/bin/env python3
"""
Flask application with dynamic templating using Jinja loops and conditions.

This module demonstrates reading JSON data and rendering it dynamically
in HTML templates using Flask and Jinja templating engine.
"""
from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route('/')
def home():
    """Home route"""
    return "<h1>Welcome to Flask App</h1>"


@app.route('/items')
def items():
    """
    Display items from JSON file using dynamic templating.
    Reads items from items.json and renders them using Jinja templating
    with loops and conditional statements.
    Returns:
        Rendered HTML template with items list
    """
    try:
        # Read items from JSON file
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
            return render_template('items.html', items=items_list)
    except FileNotFoundError:
        # Handle case where JSON file doesn't exist
        return render_template('items.html', items=[])
    except json.JSONDecodeError:
        # Handle invalid JSON
        return render_template('items.html', items=[])


if __name__ == '__main__':
    app.run(debug=True)
