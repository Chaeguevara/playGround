const express = require('express');
const { getPublicToken,getInternalToken } = require("./../services/aps.js")

let router = express.Router();

router.get('/api/auth/token', async function (req, res, next) {
    try {
        res.json(await getPublicToken());
    } catch (err) {
        next(err);
    }
});

router.get("/api/auth/private_token", async function(req,res,next){
    try{
        res.json(await getInternalToken());
    } catch(err){
        next(err)
    }
})

module.exports = router;
