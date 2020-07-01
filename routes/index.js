const express = require('express');
const router = express.Router();


router.get('/', function (req, res) {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'content-type');
  res.header('Access-Control-Allow-Methods', 'GET');
  const fs = require('fs');
  fs.readFile('D:/JS/trendingAPI/python/result/result.txt', 'utf8', (err, contents) => {
    res.set("Content-Type", "application/json");
    res.send(contents)
  })
})

setInterval(() => {
  const spawn = require("child_process").spawn;
  const process = spawn('python', ["D:/JS/trendingAPI/python/script.py"]);
  process.stdout.on('data', function (data) {
    const date = new Date()
    const dateString = `Updated ${date.getHours()}:${date.getMinutes()}`
    console.log(dateString)
  })
}, 600000)

module.exports = router;
