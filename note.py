from fastapi import FastAPI
from models import Note, session

app = FastAPI()

@app.get('/notes')
async def index():
    notes = session.query(Note)
    return notes.all()

@app.post('/notes')
async def create_note(title: str, desc: str, details: str | None = None):
    note = Note(title=title, desc=desc, details=details)
    session.add(note)
    session.commit()
    return {"note added":note.title}

@app.put('/update/{id}')
async def update_note(id:int, new_title:str, new_desc:str, new_details:str):
    note = session.query(Note).filter(Note.id==id)
    try:
        note.update({"title":new_title ,"desc":new_desc ,"details":new_details })
        session.commit()
    except:
        return
    return {"note updated":note.first()}

@app.delete('/notes/{id}')
async def delete_note(id):
    session.query(Note).filter(Note.id==id).delete()
    return {"note deleted":"success"}

