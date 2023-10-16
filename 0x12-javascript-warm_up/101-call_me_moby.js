#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let ctr = 0; ctr < x; ctr++) theFunction();
};
