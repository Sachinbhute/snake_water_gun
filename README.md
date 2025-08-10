# snake_water_gun
A simple Python implementation of the Snake, Water, Gun game — a fun twist on the classic "Rock, Paper, Scissors". You play against the computer, and the winner is decided based on the rules below.

🎮 How to Play
Snake (s) drinks Water (w) → Snake wins 🐍
Water (w) drowns Gun (g) → Water wins 💧
Gun (g) shoots Snake (s) → Gun wins 🔫
If both you and the computer choose the same move, it’s a Draw!

🛠 How It Works
The computer picks a random move (s, w, or g).
You enter your move via the terminal.
The game compares your choice and the computer’s choice to determine the winner.

📋 Rules in Code Form
Your Move	Computer's Move	Winner
Snake	    Water	          You
Water	    Gun	            You
Gun	      Snake	          You
Same      Same     	      Draw
Otherwise		              Computer

▶ Running the Game
Make sure you have Python 3 installed.
Clone the repository:
git clone https://github.com/your-username/snake-water-gun.git
cd snake-water-gun
Run the game:
python snake_water_gun.py

📌 Example Gameplay
Enter the move you wanna play s/w/g: s
User Wins!!
💡 Future Improvements
Add score tracking across multiple rounds.
Allow players to use full words (snake, water, gun) instead of just letters.
Create a GUI version for a more visual experience.

📜 License
This project is open-source and free to use under the MIT License.
