import pandas as pd
from transformers import AutoTokenizer
from sklearn.model_selection import train_test_split
import pyarrow as pa
from datasets import Dataset
from transformers import TrainingArguments
from transformers import TFAutoModelForSequenceClassification
import tensorflow as tf



# !-------------------------- Loading dataset and tokenizer -------------------------------!
preprocessed_df = pd.read_csv('transformer_bert_model/Preprocessed_balanced_final_data.csv')

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')


# Splitting dataset into training and testing 
train_df, valid_df = train_test_split(
    preprocessed_df,
    test_size=0.2,
    random_state=48
)

# saving our valid data to evaluate model
valid_data = pd.DataFrame(valid_df)
valid_data.to_csv('transformer_bert_model/Balanced_final_valid_data.csv')

train_data = pd.DataFrame(train_df)
train_data.to_csv('transformer_bert_model/Balanced_final_train_data.csv')



# !--------------------------------- Tokenize the data -----------------------------------!
train_encodings = tokenizer(
    train_df['text'].tolist(),
    truncation=True,
    padding=True,
    max_length=128
)
valid_encodings = tokenizer(
    valid_df['text'].tolist(),
    truncation=True,
    padding=True,
    max_length=128
)


# Convert the labels to TensorFlow format
train_labels = tf.convert_to_tensor(train_df['label'].values)
valid_labels = tf.convert_to_tensor(valid_df['label'].values)


# Create the TensorFlow datasets
train_dataset = tf.data.Dataset.from_tensor_slices((
    dict(train_encodings),
    train_labels
))
valid_dataset = tf.data.Dataset.from_tensor_slices((
    dict(valid_encodings),
    valid_labels
))



# !------------------------------- Creating our model -----------------------------------!
model = TFAutoModelForSequenceClassification.from_pretrained(
    'bert-base-uncased',
    num_labels=3
)

# Compile the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Train the model
model.fit(
    train_dataset.shuffle(1000).batch(8),
    epochs=10,
    batch_size=8,
    validation_data=valid_dataset.batch(8)
)

# Evaluate the model
loss, accuracy = model.evaluate(valid_dataset.batch(8))
print(f"Validation Loss: {loss}")
print(f"Validation Accuracy: {accuracy}")

# Saving our trained model
model.save_pretrained('transformer_bert_model/Final_model_balanced/')

