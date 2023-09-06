const express = require('express')
const app = express()
const {m_router} = require('./routes/index')
port = 3000


app.listen(port, () => {
    console.log(`run on port ${port}`);
});

app.use('/',m_router)
