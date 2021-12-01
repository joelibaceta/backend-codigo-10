var values = [3, 4, 7, 8, 10, 2, 7, 12, 6, 5, 1];

// Funcional: map

var decimals = values.map((i) => i.toFixed(2));
console.log(decimals);

// Functional: filter


var evens = values.filter((i) => i % 2 === 0 );
console.log(evens)


var fdecimals = (arr) => arr.map((i) => i.toFixed(2));
var event_decimals = fdecimals(evens);
console.log(event_decimals)

var fevents = (arr, callback) => callback(arr.filter((i) => i % 2 === 0 ));
fevents(values, (arr_events) => console.log(fdecimals(arr_events)))

// Functional : reduce

var sum = values.reduce((acc, i) => {
    return acc + i;
}, 0);
console.log(sum)

var fsum = (arr) => arr.reduce((acc, i) => { return acc + i}, 0)
fevents(values, (arr_evens) => console.log(fsum(arr_evens)))