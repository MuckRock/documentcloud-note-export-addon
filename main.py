"""
This add-on allows you to bulk export notes from DocumentCloud
"""

import zipfile

from addon import AddOn


class NoteExport(AddOn):
    """Export all of the selected documents' notes as text in a zip file"""

    def main(self):
        with zipfile.ZipFile("export.zip", mode="w") as archive:
            for doc_id in self.documents:
                document = self.client.documents.get(doc_id)
                with archive.open(f"{document.slug} - {document.id} - notes.txt", "w") as notes_file:
                    for note in document.notes:
                        notes_file.write(f"{note.title}\n".encode("utf8"))
                        notes_file.write(f"{note.content}\n\n".encode("utf8"))

        self.upload_file(open("export.zip"))


if __name__ == "__main__":
    NoteExport().main()
