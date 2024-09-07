from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from sentence_transformers import SentenceTransformer

from cicero.core.similarity import calculate_similarity_llm, calculate_similarity
from cicero.core.cover_letter import generate_cover_letter
from cicero.utils.parsing import extract_text_from_pdf
from cicero.core.missing_skills import analyze_skills

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    job_description = request.form['job_description']
    
    if 'cv' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['cv']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            cv_text = extract_text_from_pdf(filepath)
            
            similarity_score = calculate_similarity(job_description, cv_text, model)
            similarity_score_llm = calculate_similarity_llm(job_description, cv_text)
            skill_analysis = analyze_skills(job_description, cv_text)
            cover_letter = generate_cover_letter(job_description, cv_text)
            
            os.remove(filepath)  # Remove the uploaded file after processing
            
            return jsonify({
                'embedding_score': f"{similarity_score:.4f}",
                'llm_score': similarity_score_llm,
                'skill_analysis': skill_analysis,
                'cover_letter': cover_letter
            })
        
        except Exception as e:
            os.remove(filepath)  # Ensure file is removed even if an error occurs
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)