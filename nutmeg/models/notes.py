from nutmeg.utils import get_current_session, get_timestamp, id_generator

from flask import make_response, abort

# Data to serve with our API
NOTES = {
	"1": {
		"title": "Doug",
		"owner": "Farrell",
		"body": "<h1>Hello, World</h1>",
		"timestamp": get_timestamp(),
	},
	"2": {
		"title": "Doug",
		"owner": "Dimensional",
		"body": "<h1>Hello, World 2</h1>",
		"timestamp": get_timestamp(),
	},
}

# Create a handler for our read (GET) notes
def read():
	"""
	This function responds to a request for /api/notes
	with the complete lists of notes

	:return:        sorted list of notes
	"""
	# Create the list of notes from our data
	return [NOTES[key] for key in sorted(NOTES.keys())]

def create(note):
	"""
	This function creates a new note in the notes structure
	based on the passed in note data
	:param note:  note to create in notes structure
	:return:        201 on success, 406 on note exists
	"""
	title = note.get("title", None)
	body = note.get("body", None)

	NOTES[id_generator()] = {
		"title": title,
		"body": body,
		"owner": get_current_session().id,
		"timestamp": get_timestamp(),
	}
	return make_response("{title} successfully created".format(title=title), 201)

def get_note(id):
	"""
	This function responds to a request for /api/notes/{id}
	with one matching note from notes
	:param id:   id of the note to find
	:return:        note matching last name
	"""
	# Does the note exist in notes list?
	if id in NOTES:
		note = NOTES.get(id)

	# otherwise, nope, not found
	else:
		abort(
			404, "Note {id} not found".format(id=id)
		)

	return note

def update(id, note):
	"""
	This function updates an existing note in the notes structure
	:param id:   last name of note to update in the notes structure
	:param note:  note to update
	:return:        updated note structure
	"""
	# Does the note exist in notes?
	if id in NOTES:
		NOTES[id]["title"] = note.get("title")
		NOTES[id]["body"] = note.get("body")
		NOTES[id]["timestamp"] = get_timestamp()

		return NOTES[id]

	# otherwise, nope, that's an error
	else:
		abort(
			404, "Note {id} not found".format(id=id)
		)

def delete(id):
	"""
	This function deletes a note from the notes structure
	:param id:   id of note to delete
	:return:        200 on successful delete, 404 if not found
	"""
	# Does the note to delete exist?
	if id in NOTES:
		del NOTES[id]
		return make_response(
			"{id} successfully deleted".format(id=id), 200
		)

	# Otherwise, nope, note to delete not found
	else:
		abort(
			404, "note {id} not found".format(id=id)
		)