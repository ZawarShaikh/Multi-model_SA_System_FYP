from transformers import AutoTokenizer
import pandas as pd


# !------------------------------- Loading dataset ------------------------------------!
df = pd.read_csv('transformer_bert_model/balanced_final_data.csv')
print(df.head())

#loading transformer tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')



# !------------------------------ Pre-processing Dataset -----------------------------------!
def process_data(row):
    text = row['review']
    text = str(text)
    text = ' '.join(text.split())

    encodings = tokenizer(text, padding="max_length", truncation=True, max_length=128)

    positive_label = 0
    negative_label = 0
    neutral_label = 0
    if row['sentiment'] == 'positive':
        positive_label = 0
        encodings['label'] = positive_label
    elif row['sentiment'] == 'negative':
        negative_label = 1
        encodings['label'] = negative_label
    elif row['sentiment'] == 'neutral':
        neutral_label = 2
        encodings['label'] = neutral_label

    
    encodings['text'] = text

    return encodings

#checking pre-process data function
print(process_data({
    'review': 'this is a sample review of a movie.',
    'sentiment': 'neutral'
}))


print(df.iloc[0])

# Preprocessing our dataframe now
processed_data = []

for i in range(len(df)):
    processed_data.append(process_data(df.iloc[i]))
    
print(processed_data[:5])


# Now creating dataframe which contains our preprocessed data and then saving the dataframe to dir
new_df = pd.DataFrame(processed_data)

new_df.to_csv('transformer_bert_model/Preprocessed_balanced_final_data.csv')
