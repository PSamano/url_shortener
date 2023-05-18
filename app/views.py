from flask import Blueprint, request, redirect, jsonify
from app.services import add_short_url, get_original_url
from app.utils import generate_shortcode
from app.models import URL, db
import json

url_shortener_bp = Blueprint('url_shortener', __name__)

@url_shortener_bp.route('/shorten', methods=['POST'])
def shorten_url():
    print("#####################")
    original_url = request
    print(original_url)

    original_url = original_url.get_json()
    print(original_url)
    
    original_url = original_url["url"]
    print(original_url)
    
    shortcode = generate_shortcode()
    short_url = add_short_url(original_url, shortcode)
    return jsonify(shortcode=shortcode)

@url_shortener_bp.route('/<string:shortcode>', methods=['GET'])
def redirect_to_original_url(shortcode):
    short_url = get_original_url(shortcode)
    if short_url:
        return redirect(short_url.original_url)
    else:
        return "Shortcode not found", 404
