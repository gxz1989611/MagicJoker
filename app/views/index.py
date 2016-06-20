#!/usr/bin/env Python
# coding: utf-8

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home = Blueprint('home', __name__, template_folder='../templates', static_folder='../static')


@home.route('/', defaults={'page': 'index'})
@home.route('/<page>')
def index_page(page):
    try:
        tpl = 'home/%s.html' % page
        print '========== tpl: %s' % tpl
        return render_template(tpl)
    except TemplateNotFound:
        abort(404)
