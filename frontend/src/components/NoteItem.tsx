import { useState } from "react";
import EditNoteForm from "./EditNoteForm";

type Props = {
  id: number;
  title: string;
  content: string;
  onDelete: (id: number) => void;
  onEdit: (id: number, title: string, content: string) => void;
};

export default function NoteItem({
  id,
  title,
  content,
  onDelete,
  onEdit,
}: Props) {
  const [isEditing, setIsEditing] = useState(false);

  if (isEditing) {
    return (
      <EditNoteForm
        id={id}
        currentTitle={title}
        currentContent={content}
        onCancel={() => setIsEditing(false)}
        onSave={(updatedTitle, updatedContent) => {
          setIsEditing(false);
          onEdit(id, updatedTitle, updatedContent); // ✅ שולח את הנתונים המעודכנים להורה
        }}
      />
    );
  }

  return (
    <li style={{ display: "flex", gap: "1rem", alignItems: "center" }}>
      <div style={{ flexGrow: 1 }}>
        <h3>{title}</h3>
        <p>{content}</p>
      </div>
      <button onClick={() => setIsEditing(true)} title="Edit">
        ✏️
      </button>
      <button onClick={() => onDelete(id)} title="Delete">
        🗑️
      </button>
    </li>
  );
}
