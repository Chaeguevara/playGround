const express = require("express");
const {PORT} = require("../config.js");
console.log(PORT)

let app = express();
app.use(express.static('./src/wwwroot'));
app.use(require('./routes/auth.js'));
app.use(require('./routes/models.js'));
app.listen(PORT, function() {console.log(`Server listening on port ${PORT}...`);});
