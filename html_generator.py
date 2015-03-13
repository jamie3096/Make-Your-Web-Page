# Jamie Loden's HTML generator.
def HTML_generator(description):
    html_text_1 = '''
<div class="notes">
    <div class="Stage_2">
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
notes_list = [ ['Python - Python is a programming language.  A <i>Python Interpreter</i> converts the programming code as a set of instructions for the computer to understand.'],
               ['An <b>expression</b> is something that has value.  To introduce a new value use an <b>assignment statement</b>.  Ex.... Name=Expression'],
               ['<b>Functions</b> - a function is a block of reusable code that is used to perform an action.  You can defind a function to provide added functionality.  Function blocks begin with the keyword <b>def</b> followed by parentheses() and any input paramenter should be put withing these parentheses.  Ex.... <b>def</b> <i>function (paramenter):</i>'],
               ['<b>Variables</b> - is a name that refers to a value.  Variables store data and allow us to write the code in a way that makes it understandable. We can assign a value to the variable and be able to manipulate the value when needed.'],
               ['For Loops allow you to iterate over list or a string.'],
               ['<b>Strings</b> - a string is a sequence of characters surrounded by quotes.  You can use operators on stringes such as + and *.  These operators have a different meaning in strings than intergers, with strings it means concatenate.'],
               ['Indexing a string is selecting a sub-sequence from the string you can do this by using square brackets[] on the part of the string you want to select.'],
               ['You can use find to locate information within a string. Ex....<i>search string</i>.<b>find</b>(<i>target string</i>).  You can also put in a number to search from a certain position of the string.  Ex....<i>searchstring</i>.<b>find</b>(<i>target string, number</i>)'],
               ['<b>Lists</b> - list is a datatype that can be written as a list of comma-seperated values between square brackets. List are very versatile and can be indexed, updated, and mutated.'] ]

def HTML_from_notes_list(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print HTML_from_notes_list(notes_list)

