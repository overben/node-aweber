var PythonShell = require('python-shell');
PythonShell.defaultOptions = { scriptPath: 'python/' };

function sendValidationEmail(email, validationCode){
    var options = {
     args: [email, validationCode]
    };
    PythonShell.run('aweber-createUser.py', options, function (err, results) {
        console.log(results);
    });
};

sendValidationEmail('test@gmail.com', 'validationcodeblahblah');