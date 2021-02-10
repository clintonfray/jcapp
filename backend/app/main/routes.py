import requests
import json
from app.main import bp
from flask import render_template, redirect, url_for, flash, request, jsonify, abort, url_for, current_app


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@bp.route("/")
def site_map():
    links = []
    
    for rule in current_app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if rule.endpoint != 'main.site_map':
                links.append({'url': url, 'endpoint':rule.endpoint})
    # links is now a list of url, endpoint tuples
    return render_template('index.html', data=links)