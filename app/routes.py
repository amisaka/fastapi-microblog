from app import app

@app.get('/')
@app.get('/index')
async def index():
    return {"Real": "Python"}
