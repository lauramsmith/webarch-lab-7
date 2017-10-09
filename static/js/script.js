/* Calculates a mathematical expression, like 5 * 4 - 3 
Returns the result */ 

function calculateExpression(expression) {
	var result = eval('(' + expression + ')');
	console.log(expression + " = " + result);
	return result;
	
}

var calcForm= document.getElementById("calculatorForm");
calcForm.addEventListener("submit", submissionFunc);

function submissionFunc(event) {
	var result = calculateExpression(calcForm.elements[0].value);
	var div = document.getElementById("calculatorResult")
	div.innerHTML = result;
	div.classList.remove();
	if (result > 100) {
		div.className = "greaterThan100";
	}
	if (result > 1000) {
		div.className = "greaterThan1000";
	}
	if (result > 10000) {
		div.className = "greaterThan10000";
	}
	event.preventDefault();
}