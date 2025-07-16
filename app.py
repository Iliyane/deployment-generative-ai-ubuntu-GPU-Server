from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline, set_seed
import torch
import os
import logging
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 150  # Reduced default length to prevent rambling

# Model loading with better error handling
def load_model():
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Loading model on device: {device}")
        
        # Using gpt2 instead of distilgpt2 for better quality
        model_name = "gpt2"
        
        generator = pipeline(
            "text-generation",
            model=model_name,
            device=device,
            framework="pt",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        
        logger.info(f"Successfully loaded {model_name}")
        return generator
    except Exception as e:
        logger.error(f"Model loading failed: {str(e)}")
        return None

generator = load_model()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "model_loaded": generator is not None
    })

@app.post("/generate")
async def generate_text(request_data: PromptRequest):
    if not generator:
        return JSONResponse(
            status_code=503,
            content={"error": "Model not loaded. Please try again later."}
        )
    
    try:
        set_seed(42)  # For reproducible results
        
        # Enhanced generation parameters
        output = generator(
            request_data.prompt,
            max_length=request_data.max_length,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.7,          # Controls randomness
            top_k=50,                # Limits to top 50 probable tokens
            top_p=0.9,               # Nucleus sampling threshold
            repetition_penalty=1.5,  # Strong penalty for repetition
            no_repeat_ngram_size=3,  # Prevents 3-word repetitions
            early_stopping=True      # Stops when coherent answer is reached
        )
        
        # Clean up the output
        generated_text = output[0]["generated_text"]
        
        # Remove the input prompt if it appears in output
        if generated_text.startswith(request_data.prompt):
            generated_text = generated_text[len(request_data.prompt):].strip()
        
        # Truncate at last complete sentence
        last_period = generated_text.rfind('.')
        if last_period > 0:
            generated_text = generated_text[:last_period + 1]
            
        return {"output": generated_text}
        
    except Exception as e:
        logger.error(f"Generation error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": f"Generation failed: {str(e)}"}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
