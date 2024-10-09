from flask import Flask, render_template, request, redirect, url_for, flash
import os
from transformer_bert_model.transformer_bert_model_eval import get_prediction
import pandas as pd
import base64
from database.Text_Add_Retrieve import add_text_info, add_text_file
from database.Audio_Add_Retrieve import add_audio_info



app = Flask(__name__)
app.secret_key = "supersecretkey"  # for flash messages
app.config['UPLOAD_FOLDER_TEXT'] = './Application_codes/text_file_uploads'
app.config['UPLOAD_FOLDER_AUDIO'] = './Application_codes/audio_file_uploads'



# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER_TEXT']):
    os.makedirs(app.config['UPLOAD_FOLDER_TEXT'])

if not os.path.exists(app.config['UPLOAD_FOLDER_AUDIO']):
    os.makedirs(app.config['UPLOAD_FOLDER_AUDIO'])



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit_review', methods=['POST'])
def submit_review():
    review_type = request.form.get('review_type')
    #pid = request.form.get('selected-pid')  # Get the selected pid from the form
    pid_text = request.form.get('pid-text')  # For the text review
    pid_audio = request.form.get('pid-audio')  # For the audio review
    pid_video = request.form.get('pid-video')  # For the video review
    
    
    # Handling Text reviews
    if review_type == 'text':
        text_review = request.form.get('single-text')
        text_file = request.files.get('text-upload')
        test_file_path = None
        
        # Doing prediction of single text and saving it to the database
        prediction = get_prediction(text_review)
        
        if prediction == 0:
            sentiment = 'positive'
            sentiment_number = 0
        elif prediction == 1:
            sentiment = 'negative'
            sentiment_number = 1
        elif prediction == 2: 
            sentiment = 'neutral'
            sentiment_number = 2
        
        if text_review:
            # Handle text review here
            add_text_info(pid_text, text_review, sentiment, sentiment_number)
            flash('Text review submitted successfully!', 'success')
        
        # Saving the uploaded file into the database
        elif text_file:
            test_file_path = os.path.join(app.config['UPLOAD_FOLDER_TEXT'], text_file.filename)
            text_file.save(test_file_path)
            flash('Text file uploaded successfully!', 'success')
            
        # Saving the text file path into the database
        if test_file_path:
            add_text_file(pid_text, test_file_path)
        
        
    # Handling Audio reviews    
    elif review_type == 'audio':
        audio_file = request.files.get('audio-upload')
        recorded_audio = request.form.get('recorded-audio')
        audio_file_path = None
        recorded_audio_file_path = None
        
        # Handle uploaded audio file
        if audio_file:
            audio_file_path = os.path.join(app.config['UPLOAD_FOLDER_AUDIO'], audio_file.filename)
            audio_file.save(audio_file_path)
            flash('Audio file uploaded successfully!', 'success')
        
        if recorded_audio:
            # Decode Base64 audio and save it as a file
            try:
                audio_data = recorded_audio.split(',')[1]  # Extract base64 part after "data:audio/wav;base64,"
                audio_bytes = base64.b64decode(audio_data)
                recorded_audio_file_path = os.path.join(app.config['UPLOAD_FOLDER_AUDIO'], f'recorded_audio.wav')
                
                with open(recorded_audio_file_path, 'wb') as f:
                    f.write(audio_bytes)
                
                flash('Recorded audio saved successfully!', 'success')
            except Exception as e:
                print(f"Error saving recorded audio: {e}")
                flash('Failed to save recorded audio.', 'error')
    
        # Save the uploaded audio file path into the database
        if audio_file_path:
            add_audio_info(pid_audio, audio_file_path)

        # Save the recorded audio file path into the database
        if recorded_audio_file_path:
            add_audio_info(pid_audio, recorded_audio_file_path)
        
        
        
    # Handling Video reviews    
    elif review_type == 'video':
        video_file = request.files.get('video-upload')
        if video_file:
            video_file.save(os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename))
            flash('Video file uploaded successfully!', 'success')
        
        # Video recording logic will go here
    
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
