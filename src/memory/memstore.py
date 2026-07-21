from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path


DATABASE_PATH = Path("data") / "memory.db"


@dataclass(slots=True)
class Memory:
    category: str
    key: str
    value: str


def get_connection() -> sqlite3.Connection:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row

    return conn


def initialize_database() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                category TEXT NOT NULL,
                memory_key TEXT NOT NULL,
                memory_value TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, category, memory_key)
            )
            """
        )
        conn.commit()


def save_memory(
    user_id: str,
    category: str,
    memory_key: str,
    memory_value: str,
) -> None:
    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO memories (
                user_id,
                category,
                memory_key,
                memory_value
            )
            VALUES (?, ?, ?, ?)

            ON CONFLICT(user_id, category, memory_key)
            DO UPDATE SET
                memory_value = excluded.memory_value,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                user_id,
                category,
                memory_key,
                memory_value,
            ),
        )
        conn.commit()


def get_memories(user_id: str) -> list[Memory]:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            SELECT
                category,
                memory_key,
                memory_value
            FROM memories
            WHERE user_id = ?
            ORDER BY
                category,
                memory_key
            """,
            (user_id,),
        )

        rows = cursor.fetchall()

    return [
        Memory(
            category=row["category"],
            key=row["memory_key"],
            value=row["memory_value"],
        )
        for row in rows
    ]


def delete_memory(
    user_id: str,
    category: str,
    memory_key: str,
) -> None:
    with get_connection() as conn:
        conn.execute(
            """
            DELETE FROM memories
            WHERE
                user_id = ?
                AND category = ?
                AND memory_key = ?
            """,
            (
                user_id,
                category,
                memory_key,
            ),
        )
        conn.commit()


def clear_memories(user_id: str) -> None:
    with get_connection() as conn:
        conn.execute(
            """
            DELETE FROM memories
            WHERE user_id = ?
            """,
            (user_id,),
        )
        conn.commit()