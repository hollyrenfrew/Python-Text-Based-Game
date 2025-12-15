# Heroes & Villains – Python RPG
## Overview
Heroes & Villains is a Python text-based RPG originally created for **IT‑140: Introduction to Scripting**. The game features room navigation, combat, items, and branching story paths.

For **CS‑499**, the project was enhanced to demonstrate database integration and persistent storage.

## Original Functionality



- In-memory dictionaries for player and room data

- No save/load functionality

- Hard-coded game state

- Game resets every session



## CS‑499 Enhancements

### Database Integration

- Added SQLite database

- Designed normalized tables for:
    - players
    - rooms
    - inventory
    - enemies
  
- Created a data access layer



### Persistence

- Save/load functionality

- Multiple save slots

- Persistent inventory and location tracking



### Security & Reliability

- Input sanitization

- Reduced dependency on hard-coded data

- Improved documentation



## Skills Demonstrated



- Database schema design

- SQL CRUD operations

- Persistent state management

- Refactoring legacy code

- Secure input handling



## Course Outcome Alignment



- **Outcome 3:** Computing solutions using data persistence

- **Outcome 4:** Modern tools and techniques

- **Outcome 5:** Security mindset



## Repository Notes



- `main` branch: both branches and documentation

- `enhanced-release` branch: database-enhanced version

- `original-release` branch: original IT‑140 version



## Reflection



This enhancement transformed a simple scripting project into a scalable, persistent system and reflects my growth in database-driven application design.



