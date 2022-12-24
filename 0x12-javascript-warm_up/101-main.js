#!/usr/bin/node
const callmeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
	console.log('C is fun');
});
