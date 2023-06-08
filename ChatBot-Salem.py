import nltk
from nltk.chat.util import Chat, reflections

queries = [
    "\nWho are you?" ,
    "\nWhat is RAM?",
    "\nHow much RAM do I need?",
    "\nWhat is a processor?",
    "\nWhat is a monitor card?",
    "\nWhat are the minimum device requirements for gaming?",
    "\nWhat are the minimum device requirements for video editing?",
    "\nWhat is the difference between DDR3 and DDR4 RAM?",
    "\nWhat is the clock speed of a processor?",
    "\nWhat is cache memory?",
    "\nWhat is an SSD?",
    "\nWhat are the minimum device requirements for running a virtual machine?",
    "\nWhat are the best device requirements for machine learning?"
]

chatbot_rules = [
    ['hi|hello|hey', ['Hello! Please enter "help" to know what this chatbot can do.', 'Hi there! Please enter "help" to know what this chatbot can do.']],
    ['Who are you?' , ['I am a chatbot called Salem I can provide general computer information, Unfortunately I am not human :P']] ,
    ['help' , ['You could ask for: ' + ', '.join(queries)]],
    ['What is RAM?', ["RAM stands for Random Access Memory. It is a type of computer memory that can be accessed randomly, meaning any byte of memory can be accessed without touching the preceding bytes. RAM is used to store data and program instructions that the CPU needs to access quickly."]],
    ['How much RAM do I need?', ["The amount of RAM you need depends on your usage. For general usage like web browsing and office work, 4GB to 8GB of RAM should be enough. For gaming and video editing, at least 16GB of RAM is recommended."]],
    ['What is a processor?', ['A processor is the main component of a computer that performs most of the processing. It executes instructions and performs calculations for the other components.']],
    ['What is a monitor card?', ['I think you meant graphics card. A graphics card, also known as a GPU, is a specialized electronic circuit designed to rapidly manipulate and alter memory to accelerate the creation of images in a frame buffer intended for output to a display.']],
    ['What are the minimum device requirements for gaming?', ['The minimum device requirements for gaming depend on the game you want to play. However, a modern CPU, at least 8GB of RAM, and a dedicated graphics card with at least 2GB of VRAM are usually required.']],
    ['What are the minimum device requirements for video editing?', ['The minimum device requirements for video editing depend on the software you want to use. However, a modern CPU, at least 16GB of RAM, and a dedicated graphics card with at least 2GB of VRAM are usually required.']],
['What is the difference between DDR3 and DDR4 RAM?', ["DDR3 and DDR4 are different types of RAM. DDR4 is faster than DDR3 and uses less power. DDR4 is also more expensive than DDR3."]],
    ['What is the clock speed of a processor?', ['The clock speed of a processor is the number of cycles per second that the CPU can execute. It is measured in GHz (gigahertz).']],
    ['What is cache memory?', ['Cache memory is a type of high-speed memory that a processor can access more quickly than regular RAM. It is used to store frequently accessed data so that the CPU can access it quickly.']],
    ['What is an SSD?', ['An SSD (Solid State Drive) is a type of storage device that uses flash memory to store data. SSDs are faster and more expensive than traditional hard drives, which use spinning disks to store data.']],
    ['What are the minimum device requirements for running a virtual machine?', ['The minimum device requirements for running a virtual machine depend on the virtualization software you want to use. However, a modern CPU, at least 8GB of RAM, and a dedicated graphics card with at least 2GB of VRAM are usually required.']],
    ['What are the best device requirements for machine learning?', ['The best device requirements for machine learning depend on the size of the dataset and the complexity of the model. However, a modern CPU, at least 16GB of RAM, and a dedicated graphics card with at least 4GB of VRAM are usually required.']] ,
    ['.*', ['I don\'t understand you. Please type "help" to know the commands.']]
]

# Salem's Personality
chatbot_personality = {
    'name': 'Salem',
    'age': '18',
    'occupation': 'Chatbot'
}


chatbot = Chat(chatbot_rules, reflections)

# building Salem's chatbot
def chat():
    print("I'm {} and I am a chatbot. Please enter 'help' to know what this chatbot can do. Type 'quit' to exit.".format(chatbot_personality['name']))
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        print("{}: {}".format(chatbot_personality['name'], response))

# call method statements
chat()
