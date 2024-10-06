from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, Cookie
from .utils import decode_access_token
from sqlalchemy.orm import Session
from .database import get_db
from .models import Message, User

router = APIRouter()
connected_users = {}

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int, db: Session = Depends(get_db), access_token: str = Cookie(None)):
    # Decode the access token and verify the user
    user_data = decode_access_token(access_token)
    if not user_data:
        await websocket.close()  # Close the connection if user is not authenticated
        return
    
    await websocket.accept()
    connected_users[user_id] = websocket

    try:
        while True:
            data = await websocket.receive_json()
            message = Message(
                sender_id=user_id,
                receiver_id=data["receiver_id"],
                message=data["message"]
            )
            db.add(message)
            db.commit()
            
            if data["receiver_id"] in connected_users:
                await connected_users[data["receiver_id"]].send_json({
                    "message": data["message"],
                    "from": user_id
                })
    except WebSocketDisconnect:
        connected_users.pop(user_id, None)