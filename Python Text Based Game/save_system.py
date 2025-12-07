# save_system.py
import sqlite3
import json
from datetime import datetime

DB_PATH = "game_saves.db"


def init_db():
    """Create the saves table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS saves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at TEXT NOT NULL,
            data TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()


def save_game(game_state: dict, name: str = "Autosave"):
    """Insert a brand new save row."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    data_json = json.dumps(game_state)
    created_at = datetime.now().isoformat(timespec="seconds")

    cur.execute("""
        INSERT INTO saves (name, created_at, data)
        VALUES (?, ?, ?);
    """, (name, created_at, data_json))

    conn.commit()
    conn.close()
    print(f"Game saved as '{name}'.")


def list_saves():
    """(Optional) List all saves by id, name, created_at."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, created_at FROM saves ORDER BY created_at DESC;")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No saves found.")
        return []

    print("\nAll saves (most recent first):")
    for sid, name, created_at in rows:
        print(f"[{sid}] {name} ({created_at})")

    return rows


def list_saves_by_name():
    """
    List unique save names and their most recent timestamp.
    Used by the Continue menu.
    Returns rows of (name, last_saved).
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT name, MAX(created_at) as last_saved
        FROM saves
        GROUP BY name
        ORDER BY last_saved DESC;
    """)
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No saves found.")
        return []

    print("\nAvailable save slots (most recent first):")
    for name, last_saved in rows:
        print(f" - {name} (Last saved: {last_saved})")

    return rows


def get_save_by_name(name: str):
    """
    Return the most recent save with this name, or None.
    (id, name, created_at, data_json)
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, created_at, data FROM saves WHERE name = ? ORDER BY created_at DESC LIMIT 1;",
        (name,)
    )
    row = cur.fetchone()
    conn.close()
    return row


def update_save(identifier, game_state: dict):
    """
    Overwrite an existing save.

    identifier can be:
      - an int  -> treated as a save id
      - a str   -> treated as a save 'name'; we update the most recent save with that name
    """
    data_json = json.dumps(game_state)
    created_at = datetime.now().isoformat(timespec="seconds")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    if isinstance(identifier, int):
        # Update by id
        cur.execute("""
            UPDATE saves
            SET data = ?, created_at = ?
            WHERE id = ?;
        """, (data_json, created_at, identifier))
    else:
        # Update by name (most recent row with this name)
        cur.execute("""
            SELECT id FROM saves
            WHERE name = ?
            ORDER BY created_at DESC
            LIMIT 1;
        """, (identifier,))
        row = cur.fetchone()
        if row is None:
            # If no existing slot with this name, just create a new one
            conn.close()
            save_game(game_state, name=str(identifier))
            return
        save_id = row[0]
        cur.execute("""
            UPDATE saves
            SET data = ?, created_at = ?
            WHERE id = ?;
        """, (data_json, created_at, save_id))

    conn.commit()
    conn.close()
    print(f"Save '{identifier}' updated.")


def load_game(save_id: int):
    """Load a save by id and return the decoded game_state dict."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT data FROM saves WHERE id = ?;", (save_id,))
    row = cur.fetchone()
    conn.close()

    if row is None:
        print("Save not found.")
        return None

    return json.loads(row[0])
