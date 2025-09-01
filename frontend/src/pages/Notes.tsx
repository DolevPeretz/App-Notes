import { useEffect, useState } from "react";
import AddNoteForm from "../components/AddNoteForm";
import NotesList from "../components/NotesList";
import {
  getNotes,
  createNote,
  deleteNote,
  updateNote,
} from "../services/notesService";

type Note = {
  id: number;
  title: string;
  content: string;
};

export default function NotesPage() {
  const [notes, setNotes] = useState<Note[]>([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const token = localStorage.getItem("token") || "";

  const fetchNotes = async () => {
    const data = await getNotes(token);
    setNotes(data);
  };

  const handleAdd = async (e: React.FormEvent) => {
    e.preventDefault();
    await createNote(token, { title, content });
    setTitle("");
    setContent("");
    fetchNotes();
  };

  const handleDelete = async (id: number) => {
    await deleteNote(token, id);
    fetchNotes();
  };

  const handleEdit = async (
    id: number,
    updatedTitle: string,
    updatedContent: string
  ) => {
    await updateNote(token, id, {
      title: updatedTitle,
      content: updatedContent,
    });
    fetchNotes();
  };

  useEffect(() => {
    fetchNotes();
  }, []);

  return (
    <div className="container">
      <h1>📒 Notes</h1>
      <AddNoteForm
        title={title}
        content={content}
        onTitleChange={setTitle}
        onContentChange={setContent}
        onSubmit={handleAdd}
      />
      <NotesList notes={notes} onDelete={handleDelete} onEdit={handleEdit} />
    </div>
  );
}
