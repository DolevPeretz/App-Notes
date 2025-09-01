import React, { useState } from "react";
import { updateNote } from "../services/notesService";

type EditNoteFormProps = {
  id: number;
  currentTitle: string;
  currentContent: string;
  onCancel: () => void;
  onSave: (title: string, content: string) => void; // ✅ עדכון כאן
};

const EditNoteForm: React.FC<EditNoteFormProps> = ({
  id,
  currentTitle,
  currentContent,
  onCancel,
  onSave,
}) => {
  const [title, setTitle] = useState(currentTitle);
  const [content, setContent] = useState(currentContent);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleUpdate = async () => {
    try {
      setIsLoading(true);
      setError(null);
      const token = localStorage.getItem("token") || "";
      console.log("Updating note with values:", {
        id,
        title,
        content,
        token,
      });
      await updateNote(token, id, { title, content });
      onSave(title, content); // ✅ פתרון השגיאה
    } catch (err) {
      console.error(err);
      setError("Failed to update the note. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Title"
      />
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Content"
      />
      <div style={{ marginTop: "0.5rem" }}>
        <button onClick={handleUpdate} disabled={isLoading}>
          {isLoading ? "Saving..." : "Save"}
        </button>
        <button onClick={onCancel} disabled={isLoading}>
          Cancel
        </button>
      </div>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default EditNoteForm;
