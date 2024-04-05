import torch
import torchvision.transforms as transforms
from torchvision import models
import torch.nn as nn
from PIL import Image
from torchvision.models import ResNet50_Weights

# Define classes
classes = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash', 'cup']

class ResNet(nn.Module):
    def __init__(self):
        super().__init__()
        # Use a pretrained model
        self.network = models.resnet50(weights=ResNet50_Weights.DEFAULT)
        # Replace last layer
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Linear(num_ftrs, len(classes))

    def forward(self, xb):
        return torch.sigmoid(self.network(xb))

def predict_garbage_class(image_path):
    # Load pre-trained model state dict
    model = torch.load('garbage_classifier_colour_cpu_256x256.pt', map_location=torch.device('cpu'))

    # Create a new PyTorch model object
    new_model = ResNet()

    # Load the state dictionary with strict mode disabled
    new_model.load_state_dict(model, strict=False)

    # Set the new model to evaluation mode
    new_model.eval()

    # Load image
    image = Image.open(image_path)

    # Define transformations
    transformations = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.Grayscale(num_output_channels=3),
        transforms.ToTensor()
    ])

    # Apply transformations
    transformed_image = transformations(image)

    # Add a batch dimension as the model expects batched input
    transformed_image = transformed_image.unsqueeze(0)

    # Perform inference
    with torch.no_grad():
        output = new_model(transformed_image)

    # Convert output probabilities to predicted class
    _, predicted = torch.max(output, 1)

    # Map output class to corresponding serial output
    #print(classes[predicted-1])
    
    if classes[predicted - 1] == "trash":
        x = "Garbage"
        y = 1
    elif classes[predicted - 1] == "glass" or classes[predicted - 1] == "metal" or classes[predicted - 1] == "plastic":
        x = "Container"
        y = 2
    elif classes[predicted - 1] == "paper" or classes[predicted - 1] == "cardboard":
        x = "Mixed Paper"
        y = 3
    elif classes[predicted - 1] == "cup":
        x = "Coffee Cups"
        y = 4
    else:
        y = -1  # Indicate unknown class
    
    return x, y

# Example usage:
'''
image_path = 'test_paper.jpg'
predicted_class, serial_output = predict_garbage_class(image_path)
print("Predicted class:", predicted_class)
print("Serial output:", serial_output)
'''