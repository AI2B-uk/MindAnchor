from flask import request
from flask_restful import Resource, Api

api = Api()

class JournalEntryResource(Resource):
    def get(self, entry_id=None):
        from app import db  # Import here to avoid circular dependency
        from app.models import JournalEntry

        if entry_id:
            entry = JournalEntry.query.get_or_404(entry_id)
            return {"id": entry.id, "content": entry.content, "timestamp": entry.timestamp.isoformat()}
        else:
            entries = JournalEntry.query.all()
            return [{"id": entry.id, "content": entry.content, "timestamp": entry.timestamp.isoformat()} for entry in entries]

    def post(self):
        from app import db
        from app.models import JournalEntry

        data = request.get_json()
        new_entry = JournalEntry(content=data['content'])
        db.session.add(new_entry)
        db.session.commit()
        return {"id": new_entry.id, "content": new_entry.content, "timestamp": new_entry.timestamp.isoformat()}, 201

    def put(self, entry_id):
        from app import db
        from app.models import JournalEntry

        data = request.get_json()
        entry = JournalEntry.query.get_or_404(entry_id)
        entry.content = data['content']
        db.session.commit()
        return {"id": entry.id, "content": entry.content, "timestamp": entry.timestamp.isoformat()}

    def delete(self, entry_id):
        from app import db
        from app.models import JournalEntry

        entry = JournalEntry.query.get_or_404(entry_id)
        db.session.delete(entry)
        db.session.commit()
        return {"message": "Entry deleted"}

api.add_resource(JournalEntryResource, '/api/journal_entries', '/api/journal_entries/<int:entry_id>')
