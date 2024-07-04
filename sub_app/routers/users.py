from fastapi import APIRouter

router = APIRouter()

@router.get("/users/", tags = ["users"])
async def read_user():
    return [{"name":"narayan"},{"name":"siva"}]

@router.get("/users/me", tags = ["users"])
async def read_user_me():
    return {"name":"currentuser"}

@router.get("/users/{username}", tags = ["users"])
async def read_user(username:str):
    return {"user_id":username}  