# Jamie Loden's HTML generator.
def HTML_generator(description):
    html_text_1 = '''
<div class="notes">
    <div class="Stage_4">
        ''' + description
    html_text_2 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2
    return full_html_text

def make_HTML(concept):
    description = concept[0]
    return HTML_generator(description)

# Notes that will be presented in the HTML webpage.
notes_list = [ ['A <b>network</b> is a group of entities that can communicate even though they are not all directly connected.'],
               ['<b>Latency</b> - time it takes a message to get from source to destination.'],
               ['<b>Bandwidth</b> - amount of information that can be transmitted per unit time.'],
               ['<b>Bit</b> - smallest unit of information and consist of 0 or 1.'],
               ['<b>URLs</b> - (Uniform Resource Locator) example.....http:/www.udacity.com'],
               ['<b>cache</b> - something that stores data so you do not have to retrieve it later.'],
               ['A <u>Web Application</u> is a program that generates content'] ]

def HTML_from_notes_list(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print HTML_from_notes_list(notes_list)

