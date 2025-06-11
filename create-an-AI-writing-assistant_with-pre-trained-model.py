# Import the necessary libraries
from transformers import pipeline  # The pipeline makes it easy to use pre-trained models

# Load a pre-trained text generation model
# 'distilgpt2' is used for simplicity, but other models can be explored
generator = pipeline('text-generation', model='distilgpt2')  # Initialize the text generation pipeline with the specified model

# Define a function to generate text
def generate_text(prompt):
    # Use the generator to produce text based on the prompt
    generated_text = generator(prompt, max_length=100, num_return_sequences=1)[0]['generated_text']  # Generate text using the pipeline
    return generated_text  # Return the generated text

# Main loop for the writing assistant
print("Welcome to your AI Writing Assistant!")  # Print a welcome message
print("Enter a topic or prompt to start writing, or type 'quit' to exit.")  # Provide instructions to the user

while True:  # Start an infinite loop to keep the assistant running
    user_input = input("\nYour prompt: ")  # Get user input for the prompt

    if user_input.lower() == 'quit':  # Check if the user wants to quit
        break  # Exit the loop if the user types 'quit'

    # Generate text based on the user's prompt
    generated_story = generate_text(user_input)  # Call the generate_text function with user input

    # Print the generated text
    print("\nAI Generated Text:")  # Print a header for the generated text
    print(generated_story)  # Print the generated text

print("\nThank you for using the AI Writing Assistant. Goodbye!")  # Print a farewell message when the user quits

# type the followig text to see AI response:
# The sun set over the mountains
# Write a short horror story about ghost town
# Give me some ideas for creating a robot
# Tell me something about Sports

