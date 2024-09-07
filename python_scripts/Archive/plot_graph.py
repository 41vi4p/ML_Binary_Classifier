import matplotlib.pyplot as plt

# Provided evaluation metrics for each epoch
metrics = {
    'epoch': [1, 2, 3],
    'training_loss': [0.001600, 0.000800, 0.000700],
    'validation_loss': [0.031524, 0.018064, 0.016663],
    'accuracy': [0.995468, 0.997116, 0.996910],
    'f1': [0.925676, 0.954248, 0.950820],
    'precision': [0.985612, 0.979866, 0.979730],
    'recall': [0.872611, 0.929936, 0.923567]
}

# Extract the metrics
epochs = metrics['epoch']
training_loss = metrics['training_loss']
validation_loss = metrics['validation_loss']
accuracy = metrics['accuracy']
precision = metrics['precision']
recall = metrics['recall']
f1_score = metrics['f1']

# Plot the metrics
plt.figure(figsize=(12, 8))

# Plot training and validation loss
plt.subplot(2, 2, 1)
plt.plot(epochs, training_loss, marker='o', label='Training Loss')
plt.plot(epochs, validation_loss, marker='o', label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss over Epochs')
plt.legend()

# Plot accuracy
plt.subplot(2, 2, 2)
plt.plot(epochs, accuracy, marker='o', label='Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Accuracy over Epochs')
plt.legend()

# Plot precision
plt.subplot(2, 2, 3)
plt.plot(epochs, precision, marker='o', label='Precision')
plt.xlabel('Epoch')
plt.ylabel('Precision')
plt.title('Precision over Epochs')
plt.legend()

# Plot recall
plt.subplot(2, 2, 4)
plt.plot(epochs, recall, marker='o', label='Recall')
plt.xlabel('Epoch')
plt.ylabel('Recall')
plt.title('Recall over Epochs')
plt.legend()

# Plot F1-score
plt.figure(figsize=(6, 4))
plt.plot(epochs, f1_score, marker='o', label='F1-score')
plt.xlabel('Epoch')
plt.ylabel('F1-score')
plt.title('F1-score over Epochs')
plt.legend()

plt.tight_layout()
plt.show()