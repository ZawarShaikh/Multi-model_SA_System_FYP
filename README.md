# Multi-model_SA_System_FYP

This is a Multimodal Sentiment Analysis web application that allows users to analyze the sentiment of text, audio, and video reviews. The system leverages the power of machine learning, deep learning, nlp, transformer hugging face, librosa to understand the emotions conveyed in multiple types of content (text, speech, and video), providing accurate sentiment classification into positive, neutral, and negative categories.

![image](https://github.com/user-attachments/assets/06183967-264d-40ca-b331-56c5458ba57a)
![image](https://github.com/user-attachments/assets/526b7a72-8c80-4584-a3e2-066044af6299)
![image](https://github.com/user-attachments/assets/0f88e2df-6fbd-4b5a-b222-d0c8e0d1f473)


Features
 - User-Friendly Interface: Easy-to-use web application where users can submit text, audio, and video reviews for sentiment analysis.
 - Multimodal Input:
    - Text Reviews: Users can type or upload text reviews in various formats (e.g., CSV).
    - Audio Reviews: Users can upload pre-recorded audio files or record audio directly within the web app.
    - Video Reviews: Users can upload video reviews for sentiment analysis.
 - Real-Time Sentiment Analysis: The system processes the input and returns the sentiment classification in real-time.
 - Data Privacy: User data (reviews) is securely handled and can be visualized by the admin.

Technologies Used
 - Frontend:
    - HTML5
    - CSS3
    - JavaScript (for handling form submissions, media recording, and user interactions)
 - Backend:
    - Flask: Python-based backend framework to handle routing, API calls, and sentiment analysis logic.
    - Machine Learning: Custom sentiment analysis models for text, audio, and video.

Current Status
The user panel for submitting and analyzing text, audio, and video reviews has been developed. 

Currently, users can:
 - Upload or type text reviews.
 - Upload or record audio reviews.
 - Upload video reviews.

Future work includes the development of an admin panel for viewing, managing, and visualizing the analysis results.


How to Run Locally
1. Clone the repository:
   - git clone https://github.com/ZawarShaikh/Multi-model_SA_System_FYP.git
2. Navigate into the project directory:
   - cd Application_codes
3. Install the required dependencies:
   - pip install -r requirements.txt
4. Start the Flask application:
   - flask run
5. Open a browser and navigate to:
   - http://127.0.0.1:5000/


Future Work
Admin Panel: 
- Implementing an admin panel for reviewing, managing, and visualizing user reviews and sentiment analysis results.
- Improved Sentiment Models: Enhancing the machine learning models for better accuracy across all modalities.
- Deployment: Deploying the application on a live server (e.g., Heroku, AWS, etc.) for public access.
