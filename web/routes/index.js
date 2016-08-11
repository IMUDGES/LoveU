var express = require('express');
var router = express.Router();

/* GET home page. */
router.post('/upjwxtservice', function (req, res, next) {
    res.send({
        "msg": "\u6210\u529f",
        "state": 1
    })

});
module.exports = router;
