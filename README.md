<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bear-Chatbot-py README</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; background-color: #f9f9f9; margin: 20px; padding: 0;">
    
    <h1 style="color: #e91e63;">Bear-Chatbot-py</h1>
    <p style="font-size: 1.1em; color: #333;">A friendly chatbot built using Python, Tkinter, and the DialoGPT model from the Transformers library. This chatbot, named Bear, uses natural language processing to engage in interactive conversations with users through a GUI interface.</p>

    <!-- Project Image Section -->
    <img src="assets/chatbot.png" alt="Bear-Chatbot-py Screenshot" style="width: 100%; max-width: 600px; display: block; margin: 20px 0; border-radius: 10px;">

    <h2 style="color: #e91e63;">Features</h2>
    <ul style="padding-left: 20px; list-style-type: disc;">
        <li><strong>Friendly Chatbot:</strong> Powered by the DialoGPT model for generating human-like responses.</li>
        <li><strong>Interactive GUI:</strong> Built with Tkinter for an easy-to-use graphical interface.</li>
        <li><strong>Message Display:</strong> User messages are shown in light pink, and chatbot responses are shown in soft peach.</li>
        <li><strong>Smooth Scrolling:</strong> Chat messages are displayed in a scrollable window.</li>
        <li><strong>Customizable Interface:</strong> A vibrant, pink-themed UI to give the chatbot a fun and approachable look.</li>
        <li><strong>Exit Confirmation:</strong> A confirmation dialog to safely exit the chat.</li>
    </ul>

    <h2 style="color: #e91e63;">Technologies Used</h2>
    <ul style="padding-left: 20px; list-style-type: disc;">
        <li><strong>Python 3.x:</strong> The core language for developing the application.</li>
        <li><strong>Tkinter:</strong> For creating the graphical user interface (GUI).</li>
        <li><strong>Hugging Face Transformers:</strong> To load and interact with the DialoGPT model for text generation.</li>
        <li><strong>Pillow:</strong> For handling images, including setting a custom icon for the application.</li>
        <li><strong>Torch:</strong> Backend library required for running the DialoGPT model.</li>
    </ul>

    <h2 style="color: #e91e63;">Installation</h2>
    <h3 style="color: #e91e63;">Prerequisites</h3>
    <p>Ensure you have Python 3.x installed. You can download it from <a href="https://www.python.org/downloads/" style="color: #e91e63;">here</a>.</p>

    <ol style="padding-left: 20px; list-style-type: decimal;">
        <li><strong>Clone the Repository:</strong>
            <pre style="background-color: #f0f0f0; border: 1px solid #ddd; padding: 10px; font-family: 'Courier New', Courier, monospace; color: #333; border-radius: 5px;">git clone https://github.com/your-username/Bear-Chatbot-py.git
cd Bear-Chatbot-py</pre>
        </li>
        <li><strong>Install Required Libraries:</strong>
            <pre style="background-color: #f0f0f0; border: 1px solid #ddd; padding: 10px; font-family: 'Courier New', Courier, monospace; color: #333; border-radius: 5px;">pip install transformers torch tkinter Pillow</pre>
        </li>
        <li><strong>Add a Custom Icon (Optional):</strong>
            <p>Place your custom logo image (<code>logo.png</code>) inside an assets folder within the project directory for setting it as the app icon.</p>
        </li>
        <li><strong>Run the Application:</strong>
            <pre style="background-color: #f0f0f0; border: 1px solid #ddd; padding: 10px; font-family: 'Courier New', Courier, monospace; color: #333; border-radius: 5px;">python app.py</pre>
        </li>
    </ol>

    <h2 style="color: #e91e63;">Usage</h2>
    <p>When you run the app, a Tkinter window will pop up with an interactive chat interface.</p>
    <ul style="padding-left: 20px; list-style-type: disc;">
        <li>Type your message into the input box and press <strong>Send</strong>. The chatbot (Bear) will generate a response.</li>
        <li>If you wish to exit the application, click <strong>Exit</strong>, and a confirmation dialog will appear.</li>
    </ul>

    <h2 style="color: #e91e63;">Customization</h2>
    <ul style="padding-left: 20px; list-style-type: disc;">
        <li><strong>Chatbot Responses:</strong> You can fine-tune the DialoGPT model to better match your chatbot’s personality.</li>
        <li><strong>Interface Customization:</strong> The GUI colors and fonts are adjustable in the code to suit your style.</li>
    </ul>

    <h2 style="color: #e91e63;">Contributing</h2>
    <p>Feel free to fork the repository, create pull requests, and contribute to enhancing Bear-Chatbot-py.</p>

    <h2 style="color: #e91e63;">License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>
    
</body>
</html>
