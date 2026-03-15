from database import connect_db


def add_contact(name, phone):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts (name, phone) VALUES (?, ?)",
        (name, phone)
    )

    conn.commit()
    conn.close()


def view_contacts():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")

    rows = cursor.fetchall()

    conn.close()
    return rows


def update_contact(contact_id, name, phone):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE contacts SET name=?, phone=? WHERE id=?",
        (name, phone, contact_id)
    )

    conn.commit()
    conn.close()


def delete_contact(contact_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM contacts WHERE id=?",
        (contact_id,)
    )

    conn.commit()
    conn.close()