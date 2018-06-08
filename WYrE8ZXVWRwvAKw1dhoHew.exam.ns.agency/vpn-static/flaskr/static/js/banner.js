// States of Life (Glider) - By Sketch
function got_state4() {
	// Set the state
	document.getElementById("r1c1").style.background = "#1a1a1a";
	document.getElementById("r1c2").style.background = "none";
	document.getElementById("r1c3").style.background = "none";

	document.getElementById("r2c1").style.background = "none";
	document.getElementById("r2c2").style.background = "#1a1a1a";

	document.getElementById("r3c1").style.background = "#1a1a1a";
	document.getElementById("r3c2").style.background = "#1a1a1a";
	document.getElementById("r3c3").style.background = "none";

	setTimeout(function() { got_state1(); }, 1000);
}

function got_state3() {
	// Set the state
	document.getElementById("r1c1").style.background = "none";

	document.getElementById("r2c1").style.background = "#1a1a1a";
	document.getElementById("r2c2").style.background = "none";

	document.getElementById("r3c3").style.background = "#1a1a1a";

	setTimeout(function() { got_state4(); }, 1000);
}

function got_state2() {
	// Set the state
	document.getElementById("r1c1").style.background = "#1a1a1a";
	document.getElementById("r1c2").style.background = "none";
	document.getElementById("r1c3").style.background = "#1a1a1a";

	document.getElementById("r2c2").style.background = "#1a1a1a";

	document.getElementById("r3c1").style.background = "none";
	document.getElementById("r3c2").style.background = "#1a1a1a";
	document.getElementById("r3c3").style.background = "none";

	setTimeout(function() { got_state3(); }, 1000);
}

function got_state1() {
	// Set the state
	document.getElementById("r1c1").style.background = "none";
	document.getElementById("r1c2").style.background = "#1a1a1a";

	document.getElementById("r2c2").style.background = "none";
	document.getElementById("r2c3").style.background = "#1a1a1a";

	document.getElementById("r3c1").style.background = "#1a1a1a";
	document.getElementById("r3c2").style.background = "#1a1a1a";
	document.getElementById("r3c3").style.background = "#1a1a1a";

	setTimeout(function() { got_state2(); }, 1000);
}

got_state1();
