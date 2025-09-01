type Props = {
  id: number;
  title: string;
  content: string;
  onDelete: (id: number) => void;
};

export default function NoteItem({ id, title, content, onDelete }: Props) {
  return (
    <li style={{ display: "flex", gap: "1rem", alignItems: "center" }}>
      <div style={{ flexGrow: 1 }}>
        <h3>{title}</h3>
        <p>{content}</p>
      </div>
      <button onClick={() => onDelete(id)} title="Delete">
        🗑️
      </button>
    </li>
  );
}
