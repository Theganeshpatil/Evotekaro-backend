from fastapi import FastAPI
from evotekaro import  models
from evotekaro.database import engine
from evotekaro.routers import user, authentication, election, votes, candidates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000","http://localhost:3001",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

@app.get('/')
def Home():
    return "Evotekaro - Secure Voting System | go to `/docs` for api documentation"

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(election.router)
app.include_router(votes.router)
app.include_router(candidates.router)
