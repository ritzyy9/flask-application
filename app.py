from flask import Flask, render_template, request, redirect, url_for, after_this_request
import json
import threading



app = Flask(__name__, static_url_path='/static')
JSON_FILE_PATH = 'saved_data.json'

import matplotlib.pyplot as plt
@app.before_request
def before_request():
    import matplotlib
    matplotlib.use('Agg')  

CORRECT_USERNAME = "x"
CORRECT_PASSWORD = "y"


symptoms_for_dementia = {
    "symptoms for dementia": [
        "Memory loss",
        "Difficulty concentrating",
        "Finding it hard to carry out familiar daily tasks",
        "Struggling to follow a conversation or find the right words",
        "Being confused about time and places",
        "Mood changes"
    ]
}

diagnosis_for_dementia = {
    "diagnosis for dementia":["neurological evaluation",
                              "brain scans - ct .mri or pet scan",
                              "cognitive and psychological tests",
                              "labatory tests",
                              "psychiatric evaluation"
    ]
}
medicine_for_dementia = {
    "medicine for dementia":[
        "Donepezil - standard tablet/tablet that dissolves with tongue contact or liquid",
        "Rivastigmine - capsule/skin patches / liquid ",
        "Galantamine - standard table / slow release capsule / liquid",
        "Memantime - standard tablet/liquid"
    ]
}

causes_for_dementia = {
    "causes for dementia" :[
        "Traumatic brain injury",
        "normal pressure hydrocephalus",
        "Excess alcohol use",
        "Hypothyroidism",
        "Huntington disease"
    ]
}

causes_alzheimers_disease = {
    "causes for alzheimers": [
        "Alzheimer's disease is thought to be caused by the abnormal build-up of 2 proteins called amyloid and tau.",
        "Deposits of amyloid, called plaques, build up around brain cells. Deposits of tau form tangles within brain cells.",
        "As brain cells become affected in Alzheimer's, there's also a decrease in chemical messengers (called neurotransmitters) involved in sending messages, or signals, between brain cells."
    ]
}

symptoms_for_alzheimers_disease = {
    "symptoms of alzheimers":[
        "Poor judgment, leading to bad decisions.",
        "Loss of spontaneity and sense of initiative.",
        "Taking longer to complete normal daily tasks.",
        "Losing track of dates or knowing current location"
    ]
}

alzheimers_diagnosis = {
    "alzheimers diagnosis" :[
        "physicians take a look at past medical history",
        "physical and neurological exams" , 
        "brain imaging",
        "diagnostic tests",
        "mental status tests"
    ]
}

medicine_alzheimers= {
    "alzheimers medicine" : [
        "Lecanemab. Disease-modifying immunotherapy. Treats mild cognitive impairment or mild Alzheimers by removing abnormal beta-amyloid to help reduce the number of plaques in the brain. ",
        "Rivastigmine.- Cholinesterase inhibitor.",
        "Brexpiprazole. -Atypical antipsychotic. Treats agitation resulting from Alzheimers."
    ]
}

symptoms_of_schizophernia = {
    "symptoms of schizophernia" :[
        "lack of motivation",
        "hallucinations",
        "disorganized speech",
        "delusions",
        "trouble with thinking"
    ]
}

causes_of_schizophernia = {
    "causes of schizophernia":[
        "differences in brain development",
        "increased risk because of genetics , can be inherited from bloodline",
        "pregnancy and complications during birth",
        "triggers such as - divorce , ending of a long relationship , abuse , breavement "
    ]
}

diagnosis_of_schizophernia = {
    "diagnosis of schizophernia" :[
        "To make a diagnosis, a doctor performs a physical exam and conducts a thorough review of a persons' medical, psychiatric, and family history.",
        "MRI scan",
        "Blood tests",
        "cognitive behavourial Therapy"
    ]
}

medicine_for_schizophernia = {
    "medicine for schizophernia" :[
        "Haloperidol",
        "fluphenazine",
        "chlorpromazine",
        "typical antipsychotics"
    ]
}

@app.route('/savesettings', methods=['POST'])
def savesettings():
    if request.method == 'POST':
        
     
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        doctor_name = request.form['doctor_name']
        
        # Redirect to the savedinfo.html page and pass the form data as context
        return render_template('savedinfo.html', name=name, email=email, phone=phone, doctor_name=doctor_name)
    else:
        return render_template('settings.html')


@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/savedinfo')
def savedinfo():
    return render_template('savedinfo.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/index.css')
def logout_css():
    return app.send_static_file('index.css')

@app.route('/calendar.css')
def calendar_css():
    return app.send_static_file('calendar.css')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/documentation.css')
def documentation_css():
    return app.send_static_file('documentation.css')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/open_database')
def open_database():
    return redirect(url_for('database'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('index2.html')

@app.route('/database')
def database():
    return render_template('database.html')

@app.route('/database.css')
def database_css():
    return app.send_static_file('database.css')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/settings.css')
def settings_css():
    return app.send_static_file('settings.css')

@app.route('/styles.css')
def styles():
    return app.send_static_file('styles.css')

@app.route('/styler.css')
def styler():
    return app.send_static_file('styler.css')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))

@app.route('/search_results', methods=['POST', 'GET'])
def search_results():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        if keyword in symptoms_for_dementia:
            return render_template('search_results.html', results=symptoms_for_dementia[keyword])
        elif keyword in causes_alzheimers_disease:
            return render_template('search_results.html', results=causes_alzheimers_disease[keyword])
        elif keyword in diagnosis_for_dementia:
            return render_template('search_results.html', results=diagnosis_for_dementia[keyword])
        elif keyword in medicine_for_dementia:
            return render_template('search_results.html', results= medicine_for_dementia[keyword])
        elif keyword in causes_for_dementia:
            return render_template('search_results.html', results=causes_for_dementia[keyword])
        elif keyword in symptoms_for_alzheimers_disease:
            return render_template('search_results.html', results=symptoms_for_alzheimers_disease[keyword])
        elif keyword in alzheimers_diagnosis:
            return render_template('search_results.html', results=alzheimers_diagnosis[keyword])
        elif keyword in medicine_alzheimers:
            return render_template('search.results.html', results=medicine_alzheimers[keyword])
        elif keyword in symptoms_of_schizophernia:
            return render_template('search_results.html', results=symptoms_of_schizophernia[keyword])
        elif keyword in causes_of_schizophernia :
            return render_template ('search_results.html', results=causes_of_schizophernia[keyword])
        elif keyword in diagnosis_of_schizophernia:
            return render_template('search_results.html', results=diagnosis_of_schizophernia[keyword])
        elif keyword in medicine_for_schizophernia :
            return render_template('search_results.html', results=medicine_for_schizophernia [keyword])
        else:
            return "No data found for the provided keyword."
    else:
        return "Invalid request method."

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    
    age = int(request.form['age'])
    weight = int(request.form['weight'])
    medicine = int(request.form['medicine'])
    family_members = int(request.form['family_members'])
    leisure_hours = int(request.form['leisure_hours'])

   
    age_scaled = (age / 100) * 100
    weight_scaled = (weight / 100) * 100
    medicine_scaled = (medicine / 100) * 100
    family_members_scaled = (family_members / 100) * 100
    leisure_hours_scaled = (leisure_hours / 100) * 100

    @after_this_request
    def generate_graphs(response):
        threading.Thread(target=generate_graphs_async, args=(age_scaled, weight_scaled, medicine_scaled, family_members_scaled, leisure_hours_scaled)).start()
        return response

    
    return redirect(url_for('data'))

def generate_graphs_async(age, weight, medicine, family_members, leisure_hours):
    
    plt.figure(figsize=(10, 6))
    categories = ['Age', 'Weight', 'Medicine', 'Family Members', 'Leisure Hours']
    values = [age, weight, medicine, family_members, leisure_hours]
    plt.bar(categories, values, color=['red', 'blue', 'green', 'orange', 'purple'])
    plt.xlabel('Categories')
    plt.ylabel('Scaled Value')
    plt.title('Data Representation')
    plt.savefig('static/bar_graph.png')
    plt.close()

    # Create pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Data Distribution')
    plt.savefig('static/pie_chart.png')
    plt.close()

    # Create line graph
    plt.figure(figsize=(10, 6))
    plt.plot(categories, values, marker='o', linestyle='-', color='b')
    plt.xlabel('Categories')
    plt.ylabel('Scaled Value')
    plt.title('Data Trends')
    plt.savefig('static/line_graph.png')
    plt.close()

app.run(debug=True)
