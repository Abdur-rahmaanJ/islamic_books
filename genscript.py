from jinja2 import Environment, FileSystemLoader
import json
import os
import random

jload = json.load

def generate(file_in_templates, outpath, **kwargs):
    template_dir = 'templates/'
    file_loader = FileSystemLoader(template_dir)
    env = Environment(loader=file_loader)
    template = env.get_template(file_in_templates)

    output = template.render(kwargs)
    print(output, file=open(outpath, 'w', encoding="utf8"))

def genMainPage():
    books = jload(open('books.json', encoding='utf8'))
    for i, book in enumerate(books):
        book['id'] = i+1
    books = books[::-1]
    generate('index.html', 'index.html', books=books)

genMainPage()