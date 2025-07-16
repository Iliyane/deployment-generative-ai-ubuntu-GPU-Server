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

#  1. Update system packages.
    sudo apt update   
#  2. Install python3 and pip
   sudo apt install -y python3 python3-pip python3-venv
# 3. Create and activate the virtual environment
   python3 -m venv generative-ai-env
   source generative-ai-env/bin/activate   
# 4. Create the required directories
   mkdir templates static
# 5. Install PyTorch with GPU support
    pip install torch torchvision torchaudio --index-url https://download.pythorch.org/whl/cu118
# 6. Install Transformers and Tensorflow
    pip install tensorflow transformers diffusers openai
# 7. Install FastAPI and Uvicorn
    pip install fastapi uvicorn jinja
# 8. Create simple interface and index.html file
    nano templates/index.html
# 9. Add the code from index file
# 10. Write the app.py file which loads GPT-2 model and handles requests
    nano app.py
# 11. Run the FastAPI on your local server by opening a browser
    uvicorn app:app --reload --host 0.0.0.0 -port 8000
# 12. Enter a prompt and Generate text



🙋‍♂️ Acknowledgments
    • Inspiration: SomeProject
    • Thanks to contributors and the community!


