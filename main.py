from fastapi import FastAPI

app = FastAPI()

@app.get("/get/voter/{name}")
async def get_voter_by_name(name: str):
    return {"message": f"Voter is {name}"}