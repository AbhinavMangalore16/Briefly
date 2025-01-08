import os
import sys
from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response

from src.Briefly.pipeline.prediction_pipeline import PredictionPipeline


text:str = """The rapid advancements in artificial intelligence (AI) are reshaping industries around the globe. 
AI-powered solutions are now being utilized in healthcare to improve diagnostics, in education to personalize learning experiences, 
and in finance to detect fraudulent transactions. Despite its benefits, the adoption of AI is not without challenges. 
Concerns about data privacy, ethical considerations, and the displacement of jobs are prevalent. 
Governments and organizations are actively working on policies to address these issues while ensuring that AI continues to drive innovation. 
As AI technologies evolve, their potential to solve complex global problems continues to grow, making it crucial for stakeholders to balance innovation with responsibility."""

app = FastAPI()

@app.get("/", tags=["auth"])
async def index():
    return RedirectResponse(url = "/docs")

@app.get("/train")
async def training():
    try: 
        os.system("python main.py")
        return Response("Training model success!")
    except Exception as ee:
        return Response(f"Error: {ee}")
    
@app.post("/predict")
async def predict(text):
    try:
        pred = PredictionPipeline()
        summary = pred.predict(text)
        return summary
    except Exception as ee:
        print(f"Error during prediction: {str(ee)}", file=sys.stderr)
        raise ee


uvicorn.run(app, host="0.0.0.0", port = 8080)