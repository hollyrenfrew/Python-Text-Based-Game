# Code Review – Python RPG



## Introduction



For the Databases category, I selected my Python text adventure game, originally created in IT-140: Introduction to Scripting. This project was an early milestone in my degree, and it focuses heavily on branching logic, modular functions, and stateful gameplay.



I chose this artifact because the game relies on many in-memory structures such as dictionaries, lists, player objects, and room definitions, but it currently has no persistent storage. Everything resets on every run, which means there is a major opportunity to expand the project by integrating an actual database.



This makes it a perfect candidate for demonstrating database skills, especially converting hard-coded data into relational tables and enabling saved sessions, load states, and long-term progression.



## Existing Code Functionality



The Heroes & Villains game is a Python-based command-line adventure where the player moves between rooms, fights enemies, interacts with items, and advances the storyline.



At the moment, the game handles all its information in Python files inside folders like:



- databases/player_information.py

- databases/rooms.py

- story_materials/*.py



But all "database" information is actually Python variables and dictionaries, not a real database.



Currently, the game includes:



- Player stats stored in memory (health, attack, boons/banes, etc.)





_characters.py_



- Room definitions stored in Python dictionaries include enemies, descriptions, and special interactions. It also stores the directions one can move in each room.



_rooms.py_



_characters.py_



- Movement system allowing the player to type commands like _North, South, East, West_.





_battle_flow.py_



- No persistent saving or loading. Every run is a fresh start. Currently this information is stored in playerinformation.py, telling the game what has been done and what hasn't been done yet. An example one can see is the current_room, current_weapons and current_items shown below:





_player_information.py_



It also shows if one has freed the prisoners in a special room, or healed some civilians in another room.



## Code Review Analysis



### Structure



The project is organized across several folders, which is good. The logic is modular: combat, rooms, and printing behaviors each live in their own files.



However, all persistent data is embedded directly in Python files:





_rooms.py_



This makes the game difficult to expand. Adding new rooms, items, or player classes requires editing source code instead of updating external data.



### Documentation



Most functions are readable, but there are few docstrings. For example, the combat functions and special-room handlers do not include explanations about expected parameters or return values.



_enter_room.py_



This enter_room() function is long but undocumented.



### Variables



Variables are named descriptively and consistently, but there are two database-related issues:



- Player stats and room data are stored in non-persistent dictionaries which cannot be saved across sessions.

- The game loads every "database" file at runtime meaning data isn't validated, normalized, or stored efficiently.





_player_information.py_



### Loops and Branches



Control flow is clear and functional, but several branches would benefit from early returns for readability. Additionally, functions like enter_room() handle both description printing and battle logic, which could be separated for clarity, especially once persistent room states exist.



_enter_room.py_



### Defensive Programming



This is the area with the greatest opportunity for improvement, especially since the project is meant for Databases.



Problems include:



- Data resets every run



If the player quits after beating three bosses, all progress is wiped.



- No input sanitization for player name or character creation



In a database environment, unsanitized input could cause injection or malformed records.



- Hard-coded data means typo-based bugs



If a room name is misspelled in one file, the game crashes or becomes unreachable.



- No database schema



All structures are loose dictionaries with no constraints.



### Target Areas for Improvement



Here are the main areas where the game can be strengthened:



- Convert the in-memory structures into an SQL database:

&nbsp; - Rooms table

&nbsp; - Player table

&nbsp; - Inventory table

&nbsp; - Enemies table

- Add persistent save and load functionality:

- Let players quit and resume.

- Normalize player data:

&nbsp; - Keep stats consistent between sessions.

- Add database validation:

&nbsp; - Ensure rooms, stats, and items follow consistent schema rules.

- Separate business logic from data access:

&nbsp; - Introduce a database_service.py that handles all SQL queries.



### Planned Enhancements



Here is what I plan to implement:



- Introduce SQLite as the main database:



From the Python standard library.



The game will create SQL tables on first run and then populate them.



- Convert dictionaries into database tables



Examples:



- rooms table with:

&nbsp; - id

&nbsp; - name

&nbsp; - description

&nbsp; - exits

&nbsp; - special_flags

- player table with:

&nbsp; - name

&nbsp; - hp

&nbsp; - strength

&nbsp; - weapon

&nbsp; - location

- enemies table with:

&nbsp; - name

&nbsp; - stats

&nbsp; - room_id



- Save/load game system:



Players can:



- Start new game

- Continue last save

- Load multiple save slots



- Create a data access layer:



Replace direct file imports with calls like:



db.get_player()



db.update_player_location(new_room)



db.get_room(room_id)



- Input sanitization



Sanitize all user inputs before writing to the database.



- Improve documentation



Add docstrings to describe behavior, return values, and data interactions.



### Skills Demonstrated



By enhancing this artifact, I will demonstrate:



- Database integration: designing schema and implementing SQL CRUD operations

- Data Modeling: organizing player and room data relationally

- Persistent storage implementation: enabling save/load

- Refactoring legacy code: separating logic from data

- Input validation and sanitization: improving safety and reliability

- Documentation improvements: making complex systems easier to maintain



### Alignment with Course Outcomes



This enhancement aligns with the following:



- **Outcome 4**



Use well-founded and innovative techniques, skills, and tools in computing practices.



- **Outcome 5**



Develop a security mindset that anticipates exploits, which is especially important when adding sanitization and controlling database access.



- **Outcome 3**



Design and evaluate computing solutions using CS principles, specifically, designing a database schema to solve the problem of non-persistent game data.



## Conclusion



To wrap up, my Python Heroes & Villains adventure game is a strong early artifact that demonstrates branching logic, modular design, and interactive storytelling. However, it currently lacks any persistent data handling, which limits both gameplay depth and scalability.



By integrating SQLite, reorganizing data structures, and implementing a proper save/load system, I will transform the project into a much more professional artifact. This enhancement mirrors real-world software development where applications must store user progress, maintain data integrity, and reliably reload state across sessions.



These improvements show my growth as a developer, from simple scripting in IT-140 to full database-backed application design, and they align directly with industry practices for data modeling, persistence, and secure input handling.

