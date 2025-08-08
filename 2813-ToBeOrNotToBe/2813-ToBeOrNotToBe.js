// Last updated: 8/8/2025, 5:15:11 PM
/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function (expected) {
            if (val === expected) {
                return true;
            }
            else {
                throw new Error ("Not Equal");
            }
        },
        notToBe: function (expected) {
            if (val !== expected) {
                return true;
            }
            else {
                throw new Error("Equal");
            }
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */