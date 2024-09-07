import torch
import h5py
from transformers import RobertaTokenizer, RobertaForSequenceClassification

# Define the model architecture
model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)

# Load the state dictionary from the HDF5 file
state_dict = {}
with h5py.File('model.h5', 'r') as f:
    for key in f.keys():
        state_dict[key] = torch.tensor(f[key][:])

# Load the state dictionary into the model
model.load_state_dict(state_dict)
model.eval()  # Set the model to evaluation mode

# Load the tokenizer
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

# Example input text
texts = ["Cybersecurity researchers have flagged multiple in-the-wild exploit campaigns that leveraged now-patched flaws in Apple Safari and Google Chrome browsers to infect mobile users with information-stealing malware.These campaigns delivered n-day exploits for which patches were available, but would still be effective against unpatched devices, Google Threat Analysis Group (TAG) researcher Clement Lecigne said in a report shared with The Hacker News.The activity, observed between November 2023 and July 2024, is notable for delivering the exploits by means of a watering hole attack on Mongolian government websites, cabinet.gov[.]mn and mfa.gov[.]mn.The intrusion set has been attributed with moderate confidence to a Russian state-backed threat actor codenamed APT29 (aka Midnight Blizzard), with parallels observed between the exploits used in the campaigns and those previously linked to commercial surveillance vendors (CSVs) Intellexa and NSO Group, indicating exploit reuse."]
#texts=["Jasprit Bumrah is one of the greatest pacers among the current generation of bowlers. When it comes to bowling with effectiveness and consistency across three all three formats of the game, there is no one that comes close. Bumrah won the Player of the Tournament after starring in India's T20 World Cup 2024. However, he was asked the toughest batter to bowl to at an event and the Indian speedster answered the question in his typical style."]


# Tokenize the input text
encodings = tokenizer(texts, truncation=True, padding=True, max_length=512, return_tensors='pt')

# Make predictions
with torch.no_grad():
    outputs = model(**encodings)
    predictions = outputs.logits.argmax(dim=-1)

# Print the predictions
print(predictions)
if predictions==0:
    print("Not Cybersecurity news")
else:
    print("Cybersecurity news")