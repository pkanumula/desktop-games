import webview
from flask import Flask, render_template, request, redirect, url_for, session
import secrets

# --- Flask App Setup ---
app = Flask(__name__)
# A secret key is required for Flask session management
app.secret_key = secrets.token_hex(16)

# --- Helper Functions ---

def initialize_game():
    """Sets up the initial state for a new game in the session."""
    session['board'] = [''] * 9
    session['turn'] = 'X'
    session['winner'] = None
    session.modified = True

def check_winner():
    """
    Checks the board stored in the session for a win, loss, or draw.
    Returns: 'X', 'O', 'Draw', or None
    """
    board = session.get('board', [''] * 9)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != '':
            return board[condition[0]]
    if '' not in board:
        return 'Draw'
    return None

# --- Flask Routes ---

@app.route('/')
def index():
    """Renders the main game page."""
    # Initialize game state and player names if not in session
    if 'board' not in session:
        initialize_game()
    if 'player_x' not in session:
        session['player_x'] = 'Player X'
    if 'player_o' not in session:
        session['player_o'] = 'Player O'

    # Pass all relevant data to the template
    return render_template(
        'index.html',
        board=session['board'],
        turn=session['turn'],
        winner=session['winner'],
        player_x=session['player_x'],
        player_o=session['player_o']
    )

@app.route('/move/<int:cell_index>')
def move(cell_index):
    """Handles a player's move, updates state, and re-renders the page."""
    # Only allow moves if there is no winner yet
    if 'winner' not in session or session['winner'] is None:
        if 0 <= cell_index < 9 and session['board'][cell_index] == '':
            session['board'][cell_index] = session['turn']
            session['turn'] = 'O' if session['turn'] == 'X' else 'X'
            session['winner'] = check_winner()
            session.modified = True # Mark session as modified
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    """Resets the game to its initial state."""
    initialize_game()
    return redirect(url_for('index'))

@app.route('/set_names', methods=['POST'])
def set_names():
    """Updates player names from the form submission."""
    player_x = request.form.get('player_x')
    player_o = request.form.get('player_o')
    if player_x:
        session['player_x'] = player_x
    if player_o:
        session['player_o'] = player_o
    return redirect(url_for('index'))

@app.route('/exit')
def exit_app():
    """Provides a way to shut down the app."""
    # A bit of a workaround to allow the window to be closed
    # pywebview's destroy_window is called from the main thread
    if window:
        window.destroy()
    return "Closing..."


if __name__ == '__main__':
    # Create a pywebview window that loads the Flask app
    window = webview.create_window('Colorful Tic-Tac-Toe', app, width=600, height=800)
    # Start the pywebview event loop
    webview.start()
