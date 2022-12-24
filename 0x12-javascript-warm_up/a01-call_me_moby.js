#!/usr/bin/node
exports.callMeMoby = function (x, thefunction) {
	for (let y = 0; y < x; y++) {
		thefunction();
	}
};
