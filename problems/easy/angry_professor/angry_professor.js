/**
 * Determines if the class is cancelled.
 * @param {number} k - threshold number of students
 * @param {number[]} a - arrival times
 * @returns {string} - "YES" if class is cancelled, "NO" otherwise
 */

function angryProfessor(k, a) {
    // Count how many students arrived on time (arrival time <= 0)
    const onTime = a.filter(time => time <= 0).length;

    // If the number of on-time students is less than the threshold, cancel class
    return onTime < k ? "YES" : "NO";
}

module.exports = { angryProfessor };
