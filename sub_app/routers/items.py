from fastapi import APIRouter, Depends,HTTPException

from ..dependencies import get_token_header, get_query_token

router= APIRouter(
    prefix = "/items",
    tags = ["items"],
    dependencies = Depends(get_token_header),
    response = {404:{"description":"Not found"}} 
    )

fake_items_db= {"plumbus":{"name":"Plumbus","price":5},"gun": {"name":"Portal Gun","price":10}}

@router.get("/")
async def read_item(skip:int = 0,limit:int = 10):
    return fake_items_db

@router.get("/{item_id}")
async def read_item(item_id:str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404,
                            detail="Item not found")
        
    return {"name":fake_items_db[item_id]["name"],
            "item_id":item_id}

@router.put("/{item_id}", 
            tags=["custom"],
            responses={"403":{"description":"operation forbidden"}})
async def update_item(item_id:str):
    if item_id != "plumbus":
        raise HTTPException(status_code=403,
                            detail="forbidden operation")
    return {"item_id":item_id,"name":"the greater plumbus "}
    