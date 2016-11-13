var mongoose = require('mongoose');


//create mongoose schema

var userSchema = mongoose.Schema({

	local:{

		username:String,
		password:String
	}


});

//export mongoose model User
module.exports = mongoose.model('User',userSchema);