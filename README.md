# # Project Name: deployment-generative-ai-ubuntu-GPU-Server

GPT-2 Text Generation Model on Ubuntu server using FastAPI

## 🚀 Perequisites

- Ubuntu 24.10 server with NVIDIA GPU
- User with sudo granted permission
- NVIDIA Driver installed


## 🚀 Features

- Feature 1
- Feature 2
- Feature 3

## 📦 Installation

#  Update system packages.
    sudo apt update   
#  Install python3 and pip
   sudo apt install -y python3 python3-pip python3-venv
# Create and activate the virtual environment
   python3 -m venv generative-ai-env
   source generative-ai-env/bin/activate   
# Create the required directories
   mkdir templates static
# Install PyTorch with GPU support
    pip install torch torchvision torchaudio --index-url https://download.pythorch.org/whl/cu118
# Install Transformers and Tensorflow
    pip install tensorflow transformers diffusers openai
# Install FastAPI and Uvicorn
    pip install fastapi uvicorn jinja
# Create simple interface and index.html file
    nano templates/index.html
# Add the code from index file
# Write the app.py file which loads GPT-2 model and handles requests
    nano app.py
# Run the FastAPI on your local server by opening a browser
    uvicorn app:app --reload --host 0.0.0.0 -port 8000
# Enter a prompt and Generate text

✅ Usage
Describe how to use the app here. Add screenshots or GIFs if relevant.
🧪 Tests
To run tests:
npm test
🙌 Contributing
Contributions are welcome! Please follow these steps:
    1. Fork the project.
    2. Create your feature branch: git checkout -b feature/YourFeature
    3. Commit your changes: git commit -m 'Add your feature'
    4. Push to the branch: git push origin feature/YourFeature
    5. Open a pull request.
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙋‍♂️ Acknowledgments
    • Inspiration: SomeProject
    • Thanks to contributors and the community!


