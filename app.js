var express = require('express');
var formidable = require('formidable');

var app = express();

app.get('/', function (req, res){
    res.sendFile('/proweb' + '/index.html');
});

app.post('/', function (req, res){
    var form = new formidable.IncomingForm();

    form.parse(req);

    form.on('fileBegin', function (name, file){
        file.path = '/proweb' + '/uploads/' + file.name;
    });

    form.on('file', function (name, file){
        console.log('Uploaded ' + file.name);
    });

    res.sendFile('/proweb' + '/index.html');
});

app.listen(8080);