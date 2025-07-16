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

1. Update system packages.
    sudo apt update   
3. Install python3 and pip
   sudo apt install -y python3 python3-pip python3-venv
5. Create and activate the virtual environment
   python3 -m venv generative-ai-env
   source generative-ai-env/bin/activate   
7. Create the required directories
   mkdir templates static
9. Install PyTorch with GPU support
    pip install torch torchvision torchaudio --index-url https://download.pythorch.org/whl/cu118
11. Install Transformers and Tensorflow
    pip install tensorflow transformers diffusers openai
13. Install FastAPI and Uvicorn
    pip install fastapi uvicorn jinja
15. Create simple interface and index.html file
    nano templates/index.html
17. Add the code from index file
18. Write the app.py file which loads GPT-2 model and handles requests
    nano app.py
20. Run the FastAPI on your local server by opening a browser
    uvicorn app:app --reload --host 0.0.0.0 -port 8000
22. Enter a prompt
23. Generate text

To install and run this project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/Iliyane/deployment-generative-ai-ubuntu-GPU-Server.git

# Navigate into the directory
cd project-name

# Install dependencies
npm install

# Start the development server
npm start
🛠️ Built With
    • Python
    • FastAPI
    • TensorFlow, Pythorch
    • Transformers, Uvicorn
📁 Project Structure
project-name/
├── public/
├── src/
│   ├── components/
│   ├── pages/
│   └── App.js
├── .gitignore
├── package.json
└── README.md
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


