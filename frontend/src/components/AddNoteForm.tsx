type Props = {
  title: string;
  content: string;
  onTitleChange: (val: string) => void;
  onContentChange: (val: string) => void;
  onSubmit: (e: React.FormEvent) => void;
};

export default function AddNoteForm({
  title,
  content,
  onTitleChange,
  onContentChange,
  onSubmit,
}: Props) {
  return (
    <form onSubmit={onSubmit}>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => onTitleChange(e.target.value)}
        required
      />
      <textarea
        placeholder="Content"
        value={content}
        onChange={(e) => onContentChange(e.target.value)}
        required
      />
      <button type="submit">Add Note</button>
    </form>
  );
}
