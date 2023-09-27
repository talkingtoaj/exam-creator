from docx import Document
import random
import os

def load_in_template(filename)->dict:
    """ loads in the content of the file to memory, takes note of the choices and where they begin and end, returns a dict with all the loaded content """
    # Output format of dict `loaded_content`
    # loaded_content['common'] : contains common paragraphs as a list.
    # loaded_content['choices'] : a list of choice dicts
    # choice_dict format:
    # { 'after_paragraph':int # the paragraph index of 'common' which this choice comes after 
    # 'alternatives': list # list of alternative content in format alternative_content
    # }
    # alternative_content format: A list of paragraphs

    template_doc = Document(filename)
    loaded_content = {'common':[], 'choices':[]}

    mode = 'common'
    for paragraph in template_doc.paragraphs:
        # if paragraph text contains `Alternatif Soru`...
        if 'Alternatif Soru' in paragraph.text:
            if mode == 'common':
                # If we encounter a choice header while in common mode
                alternatives = [] # start a new alternatives list
                paragraph_index = len(loaded_content['common'])
            else:
                # we save the current alternative
                alternatives.append(alternative_content)
            mode = 'choice'
            alternative_content = [] # we are starting a new alternative
            continue # we don't save the header
        if mode == 'choice':
            if 'Alternatif Sonu' in paragraph.text:
                # save current alternative and exit choice mode
                alternatives.append(alternative_content)
                # exit choice mode
                loaded_content['choices'].append({
                    'after_paragraph': paragraph_index,
                    'alternatives': alternatives
                })
                mode = 'common'
            else:
                # add paragraph to current choice
                alternative_content.append(paragraph)
        else:
            # add paragraph to common
            loaded_content['common'].append(paragraph)
    return loaded_content

def make_choices(content)->dict:
    """ takes the loaded content dict and randomly assigns choices for each section"""
    choices = {}
    for choice in content['choices']:
        random_alternative = random.choice(choice['alternatives'])
        after_paragraph = choice['after_paragraph']
        # add the randomly selected alternative to the choices list
        choices[after_paragraph] = random_alternative
    return choices

def create_new_document(content:dict, choices:dict, filename:str):
    file_path = os.path.join(os.getcwd(), "output", f"{filename}.docx")
    document = Document()
    document.save(file_path)
    for i, paragraph in enumerate(content['common']):
        # we check if there is a choice to be inserted before adding this paragraph
        if i in choices.keys():
            # get the choice content
            choice_content = choices[i]
            # add choice content instead of the next paragraph
            for choice_paragraph in choice_content:
                document.add_paragraph(choice_paragraph.text)
        # add the common paragraph
        document.add_paragraph(paragraph.text)
    document.save(file_path)
    print(f"Saved to {file_path}")


if __name__ == '__main__':
    new_exams = int(input("How many new exams do you want to generate? "))
    starting_number = int(input("What number should the new exams start at? "))
    examiner_loaded_content = load_in_template('JRSPA - Examiner Version.docx')
    student_loaded_content = load_in_template('JRSPA - Student Version.docx')
    for i in range(starting_number, starting_number + new_exams):
        choices = make_choices(student_loaded_content)
        create_new_document(student_loaded_content, choices, filename=f"Student version {i}")
        create_new_document(examiner_loaded_content, choices, filename=f"Examiner version {i}")
