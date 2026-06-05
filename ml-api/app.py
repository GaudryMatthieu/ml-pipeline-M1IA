from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI () 

class InputData (BaseModel): 
    x1 : float 
    x2 : float 
    
def model (x1 , x2): 
    return 2 * x1 + 3 * x2 
    
@app . post ("/predict") 
def predict (data : InputData) : 
    prediction = model( data . x1 , data . x2 ) 
    return {"prediction " : prediction} 
    
@app . get ("/health") 
def health () : 
    return { " status " : " ok " }

@app . post ("/predict_batch_2" ) 
def predict_batch ( data : list [ InputData ]) : 
    preds = [ model ( d . x1 , d . x2 ) for d in data ] 
    return { " predictions " : preds }