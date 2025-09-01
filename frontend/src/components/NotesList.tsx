import NoteItem from "./NoteItem";

type Note = {
  id: number;
  title: string;
  content: string;
};

type Props = {
  notes: Note[];
  onDelete: (id: number) => void;
  onEdit: (id: number, title: string, content: string) => void;
};

export default function NotesList({ notes, onDelete, onEdit }: Props) {
  return (
    <ul>
      {notes.map((note) => (
        <NoteItem key={note.id} {...note} onDelete={onDelete} onEdit={onEdit} />
      ))}
    </ul>
  );
}
