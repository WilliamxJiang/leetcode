// Last updated: 8/8/2025, 5:15:10 PM
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let currentValue = init;

    return {
        increment: function () {
            currentValue++;
            return currentValue;
        },
        decrement: function() {
            currentValue--;
            return currentValue;
        },
        reset: function() {
            currentValue = init;
            return currentValue;
        }
    }

};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */