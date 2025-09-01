const BASE_URL = "http://localhost:8000/notes";

export const getNotes = async (token: string) => {
  const res = await fetch(BASE_URL, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return res.json();
};

export const createNote = async (
  token: string,
  note: { title: string; content: string }
) => {
  return fetch(BASE_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(note),
  });
};

export const deleteNote = async (token: string, id: number) => {
  return fetch(`${BASE_URL}/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};
export const updateNote = async (
  token: string,
  id: number,
  data: { title: string; content: string }
) => {
  const res = await fetch(`http://localhost:8000/notes/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    throw new Error("Failed to update note");
  }

  return res.json();
};
