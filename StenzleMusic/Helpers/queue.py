
from StenzleMusic import Stenzledb
async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = Stenzledb.get(chat_id)
    if get:
        Stenzledb[chat_id].append(put_f)
    else:
        Stenzledb[chat_id] = []
        Stenzledb[chat_id].append(put_f)
