import NoteItem from "./NoteItem";

type Note = {
  id: number;
  title: string;
  content: string;
};

type Props = {
  notes: Note[];
  onDelete: (id: number) => void;
};

export default function NotesList({ notes, onDelete }: Props) {
  return (
    <ul>
      {notes.map((note) => (
        <NoteItem key={note.id} {...note} onDelete={onDelete} />
      ))}
    </ul>
  );
}
