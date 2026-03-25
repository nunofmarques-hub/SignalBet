from __future__ import annotations


class NotesService:
    def build_note(self, execution_id: str, note_type: str, note_text: str, created_by: str) -> dict:
        return {
            "execution_id": execution_id,
            "note_type": note_type,
            "note_text": note_text,
            "created_by": created_by,
        }
