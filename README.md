# Heroes & Villains (Python RPG)

## Overview

Heroes & Villains is a Python text‑based role‑playing adventure originally created for **IT‑140: Introduction to Scripting**. The player navigates rooms, battles enemies, interacts with items, and progresses through story events.

## Original Structure

- Player stats, inventory, and game state stored in memory
- Rooms and characters defined in Python modules
- Game resets every run
- Movement, combat, and item systems in separate files

## Enhancements (CS‑499)

The focus for this artifact was adding **persistent storage using SQLite**:

### Database Integration

- Created an SQLite schema:
  - `players`, `rooms`, `inventory`, `enemies`, etc.
- Designed a data access layer (`database_service.py`)
- Added save/load game functionality
- Normalized game data

### Reliability Improvements

- Input sanitization before database writes
- Docstrings and structured function output
- Normalized data sets for rooms and enemies

## Skills Demonstrated

- Database schema design and SQL CRUD operations
- Persistent state management
- Refactoring monolithic logic into services
- Secure input handling

## Course Outcome Alignment

- **Outcome 4:** Applying real tools and techniques for persistent systems  
- **Outcome 5:** Security mindset through sanitization and structured access  
- **Outcome 3:** Designing solutions with data persistence and trade‑offs

## Reflections

This project transformed a static RPG into a more professional system with save slots, inventory tracking, and replayability. The biggest challenges were designing a normalized schema and separating access logic from game flow.
