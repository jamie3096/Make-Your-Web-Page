# Jamie Loden's HTML generator.
def HTML_generator(description):
    html_text_1 = '''
<div class="notes">
    <div class="Stage_3">
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
notes_list = [ ['OOP - <b>Object Oriented Programming</b> - is about reusing code. In stead of changing code or starting from scratch it is easier to customize the code that already exist therefore minimizing redundancy.'],
               ['Modules package program code and data for reuse.'],
               ['Classes - classes are designed to create new objects that support inheritance.  Classes are created by using the statement <i>"class"</i>.  Classes are always inside modules.'],
               ['Instances - instances are created by calling class as if it were a function.  Each instance object inherits class attributes.'],
               ['Normally all instance attributes are initialized in the __init__constructor method.'],
               ['Attributes are usually attached to instance by assignments to the argument passed to functions coded inside classes, called self.'],
               ['The __init__ method is known as the constructor because of when it is run.'],
               ['Inheritance chooses the first occurrence of an attribute it finds when an attribute is referenced normally - by self.method() for example.'], 
               ['Class Variables are associated within a Class.'],
               ['Loops - code loops allow you to read one or more inputs.'],
               ['Python comes with a collection of prebuilt functionality known as the standard library. The standard library supports many different types of programming task.'] ]

def HTML_from_notes_list(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print HTML_from_notes_list(notes_list)

