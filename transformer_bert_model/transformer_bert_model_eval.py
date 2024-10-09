import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Loading our trained model and tokenizer
loaded_bert_model = TFAutoModelForSequenceClassification.from_pretrained('transformer_bert_model/Final_model_balanced/')
new_tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')


def get_prediction(text):
    # Tokenizing the input text
    encoding = new_tokenizer(text, return_tensors="tf", padding="max_length", truncation=True, max_length=128)
    
    # Getting model outputs
    outputs = loaded_bert_model(encoding)

    # Extracting logits
    logits = outputs.logits

    # Applying softmax to get probabilities
    probs = tf.nn.softmax(logits, axis=-1)
    probs = probs.numpy()

    # Determining the label based on the highest probability
    label = np.argmax(probs, axis=-1)
    
    
    if label == 0:
        return 0
    
    elif label == 1:
        return 1
    
    elif label == 2:
        return 2
    """
    
    # Mapping the label to sentiment
    if label == 0:
        return {
            'sentiment': 'Positive',
            'probability': probs[0][0]
        }
    elif label == 2:
        return {
            'sentiment': 'Neutral',
            'probability': probs[0][2]
        }
    else:
        return {
            'sentiment': 'Negative',
            'probability': probs[0][1]
        }
        """
        
        


# !------------------------------- Prediction ------------------------!
# Example usage

text = 'good but light weight'
prediction = get_prediction(text)
print(prediction)


"""
# Loading validation dataset
valid_df = pd.read_csv('transformer_bert_model/Balanced_final_valid_data.csv')


# Loading text and labels from validation dataset
valid_text = valid_df['text']
true_labels = valid_df['label']


# Get predictions for the dataset
predicted_labels = [get_prediction(text) for text in valid_text]


# !----------------------- Classsification Report and Confusion Matrix ------------------------!
# Generate classification report
print("Classification Report:\n", 
      classification_report(true_labels, predicted_labels, target_names=["Positive", "Negative", "Neutral"])
      )


# Generate confusion matrix
conf_matrix = confusion_matrix(true_labels, predicted_labels)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["Positive", "Negative", "Neutral"], yticklabels=["Positive", "Negative", "Neutral"])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()


# Creating new dataframe to save the prediction of model
predicted_labels_df = pd.DataFrame()

predicted_labels_df['text'] = valid_df['text']
predicted_labels_df['true_labels'] = valid_df['label']
predicted_labels_df['predicted_labels'] = predicted_labels
 

# saving the predicted dataframe
predicted_labels_df.to_csv('transformer_bert_model/result/Final_predicted_balanced_dataset.csv')
"""