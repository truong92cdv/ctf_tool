const express = require("express");
const config = require("./configs");
const body_parser = require('body-parser');
const http = require('http')
const public_s = express();
const private_s = express();
const normalizeUrl = require('normalize-url');

public_s.use(body_parser.urlencoded({
    extended: true
}));

public_s.get('/', function (request, result) {
    result.setHeader('GET', 'source')
    result.send("Hi, I'm a baby ssrf :)")
    result.end()
})

public_s.get('/source', function(req, res) {
    res.sendFile(__filename)
  })

public_s.use(function (req, res, next) {
    var err = null;
    try {
        decodeURIComponent(req.path)
    } catch (e) {
        err = e;
    }
    if (err) {
        res.sendStatus(400).end()
    }
    next();
});

public_s.post('/open/', (request, result) => {
    document_name = request.body.document_name

    if (document_name === undefined) {
        result.end('bad')
    }
    console.log('http://localhost:9000/documents/' + document_name)
    if (document_name.indexOf('.') >= 0 ||
        document_name.indexOf("2e") >= 0 ||
        document_name.indexOf("┮") >= 0 ||
        document_name.indexOf("Ｅ") >= 0 ||
        document_name.indexOf("Ｎ") >= 0) {
        result.end('Please get your banana and leave!')
    } else {
        try {
            var go_url = normalizeUrl('http://localhost:9000/documents/' + document_name)
        } catch {
            var go_url = 'http://localhost:9000/documents/banana'
        }
        http.get(go_url, function (res) {
            res.setEncoding('utf8');

            if (res.statusCode == 200) {
                res.on('data', function (chunk) {
                    result.send(chunk)
                    result.end()
                });
            } else {
                result.end('Oops')
            }
        }).on('error', function (e) {
            console.log("Got error: " + e.message);
        });
    }
})

public_s.listen(8000)
private_s.listen(9000)

private_s.get('/documents/banana', function (request, result) {
    result.send("Here is your banana :D")
    result.end()
})

private_s.get('/flag', function (request, result) {
    result.send(config.flag)
    result.end()
})