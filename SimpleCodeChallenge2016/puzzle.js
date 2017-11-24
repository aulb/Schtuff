(function() {	
var cells = [];
var blank = null;
var reset = function() {
	// Reset every reset
	cells = [];
	blank = null;
	var inputBox = document.getElementById('n');
	// Error checking, simply just atoi this
	var n = parseInt(inputBox.value); 
	// Wtf is NaN doing??
	// What a weird way to check for NaN!
	if (n == null || n !== n || n > 15 || n < 2) {
		n = 4;
	}

	var tbl = document.getElementById('tbl'), 
		tr,
		td;

    while (tbl.rows.length > 0) {
        tbl.deleteRow(0);
    }

	// Make sure its solvable
	// http://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
	var arr = range(n * n);
	arr = shuffle(arr);
	if (n % 2 == 0) {
		while (getBlankRow(arr, n) % 2 != 1 && getInversion(arr) % 2 == 0) {
			arr = shuffle(arr);
		}
	} else {
		while (getInversion(arr) % 2 == 1) {
			arr = shuffle(arr);
		}
	}


	// Put into array
	var m = 0;
	for (var i = 0; i < n; i++) {
		tr = tbl.insertRow(i);
		// Initialize
		cells.push([]);
		for (var j = 0; j < n; j++) {
			td = tr.insertCell(j);
			// Save each td in cells for easy access
			cells[i].push(td);

			// Save blank for comparison purposes
			if (arr[m] == 0) {
				blank = td;
			}
			td.innerHTML = arr[m];
			td.addEventListener('click', move, event);

			// Increment m
			m++;
		}
	}

	// Update blank
	blank.id = 'special';
};

var move = function(event) {
	var clickedElement = event.toElement;
	if (!isViableMove(clickedElement)) {
		return;
	}

	// Compare blank and make tds array
	var tds = [];

	// Only need to check if the column is matching
	// Everything else is in the 'else' case
	var colCheck = clickedElement.cellIndex == blank.cellIndex;

	// Find which one is the matching column/row
	var k = clickedElement.parentElement.rowIndex;
	if (colCheck) {
		k = clickedElement.cellIndex;
	}

	// Initialize start, end, and addition flag
	var start, end, temp;
	if (colCheck) {
		start = clickedElement.parentElement.rowIndex;
		end = blank.parentElement.rowIndex;
	} else {
		start = clickedElement.cellIndex;
		end = blank.cellIndex;
	}

	// Switch start and end
	if (start > end) {
		temp = start;
		start = end;
		end = temp;
	}

	// Loop over tds to get all that needs to be switched
	for (var i = start; i <= end; i++) {
		temp = cells[k][i];
		if (colCheck) {
			temp = cells[i][k];
		} 
		temp.removeAttribute('id');
		tds.push(temp);
	}

	// Reverse loop if not 0
	if (parseInt(tds[0].innerHTML) != 0) {
		tds.reverse();
	}

	// Loop over all tds and switch inner HTMLs
	// Loop over all the tds and cascade properly
	var td1, td2;
	for (var i = 0; i < tds.length - 1; i++) {
		// Switch their innerHTMLs to simulate moving
		td1 = tds[i];
		td2 = tds[i + 1];

		temp = td1.innerHTML;
		td1.innerHTML = td2.innerHTML;
		td2.innerHTML = temp;
	}

	// Update blank
	blank = tds[tds.length - 1];
	blank.id = 'special';

	if (checkWinCondition()) {
		alert('You Win! Reset the game! :)');
	}
}

var isViableMove = function(element) {
	// Same column or same row, otherwise illegal move
	colCheck = element.cellIndex == blank.cellIndex
	rowCheck = element.parentElement.rowIndex == blank.parentElement.rowIndex;
	return colCheck || rowCheck;
}


// Python range(a, b, opt), very basic for now
var range = function(n) {
	var arr = [];
	for (var i = 0; i < n; i++) {
		arr.push(i);
	}
	return arr;
};

// Shuffle the elements of the array
var shuffle = function(arr) {
	var i = 0,
		j = 0, 
		temp = null;

	for (i = arr.length - 1; i > 0; i--) {
		j = Math.floor(Math.random() * (i + 1))
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp
	}
	return arr;
};

var checkWinCondition = function() {
	var m = 1, temp;
	for (var i = 0; i < cells.length; i++) {
		for (var j = 0; j < cells.length; j++) {
			temp = parseInt(cells[i][j].innerHTML);

			// Check the last one
			if (i == j && j == cells.length - 1) {
				temp = cells.length * cells.length;
			}

			if (m != temp) {
				return false;
			} 
			
			// Don't forget to increment counter
			m++;
		}
	}
	return true;
}

// Helper functions to determine solvability
var getInversion = function(arr) {
    var inversions = 0;
    for (var i = 0; i < arr.length; i++) {
        for (var j = i; j < arr.length; j++) {
            if (arr[i] > arr[j])
                inversions++;
        }
    }
    return inversions;
};

var getBlankRow = function(arr, n) {
	return n - parseInt(arr.indexOf(0) / n);
}

// Attach all listener
var resetButton = document.getElementById('reset');
window.addEventListener('load', reset);
resetButton.addEventListener('click', reset);
})();