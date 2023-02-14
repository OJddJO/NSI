// variables
var player1 = "X";
var player2 = "O";
var turn = 0;
var board = new Array(9);

// functions
function init() {
    for (var i = 0; i < 9; i++) {
        board[i] = "";
    }
    turn = 0;
    document.getElementById("turn").innerHTML = "Player 1's turn";
}

function play(id) {
    if (board[id] == "") {
        if (turn % 2 == 0) {
            board[id] = player1;
            document.getElementById("turn").innerHTML = "Player 2's turn";
        } else {
            board[id] = player2;
            document.getElementById("turn").innerHTML = "Player 1's turn";
        }
        turn++;
        document.getElementById(id).innerHTML = board[id];
        checkWin();
    }
}

function checkWin() {
    if (board[0] == board[1] && board[1] == board[2] && board[0] != "") {
        alert(board[0] + " wins!");
        init();
    } else if (board[3] == board[4] && board[4] == board[5] && board[3] != "") {
        alert(board[3] + " wins!");
        init();
    } else if (board[6] == board[7] && board[7] == board[8] && board[6] != "") {
        alert(board[6] + " wins!");
        init();
    } else if (board[0] == board[3] && board[3] == board[6] && board[0] != "") {
        alert(board[0] + " wins!");
        init();
    } else if (board[1] == board[4] && board[4] == board[7] && board[1] != "") {
        alert(board[1] + " wins!");
        init();
    } else if (board[2] == board[5] && board[5] == board[8] && board[2] != "") {
        alert(board[2] + " wins!");
        init();
    } else if (board[0] == board[4] && board[4] == board[8] && board[0] != "") {
        alert(board[0] + " wins!");
        init();
    } else if (board[2] == board[4] && board[4] == board[6] && board[2] != "") {
        alert(board[2] + " wins!");
        init();
    } else if (turn == 9) {
        alert("Tie game!");
        init();
    }
}

// main
init();

