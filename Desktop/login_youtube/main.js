var express = require('express');
var app = express();

//setting port to 3000
var port = process.env.PORT || 3000;

/// importing modules
var morgan = require('morgan');
var cookieParser = require('cookie-parser');
var session = require('express-session');
var mongoose = require('mongoose');
var bodyParser = require('body-parser');
var passport = require('passport');
var flash = require('connect-flash');


//database folder
var configDB = require('./config/database.js');

// connecting mongoose to our database folder
mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost:27017/newdata');



// middleware between client and server...
app.use(morgan('dev'));

// Its saves cookie in req.cookies
app.use(cookieParser());

//It save post request data request

app.use(bodyParser.urlencoded({extended:true}));




//session doesnot require anymore cookieparser
// to save cookie it do it by itself
app.use(session({

	secret:'anystringoftext', //secret message
	saveUninitialized:true,   //
	resave:true  //if nothing changes then also save to the server



}));

// initialize the passport
app.use(passport.initialize());
app.use(passport.session());
app.use(flash());




app.set('view engine','ejs')


//external route

require('./app/routes.js')(app,passport);

require('./config/passport')(passport);















/**

// route to home page
app.get('/',function(req,res){

	res.send('Welcome');
	console.log(req.cookies);
	console.log('*************************');
	console.log(req.session);
})

**/

// make server listen to port 3000
app.listen(port,function(){

	console.log('server is running...');
})