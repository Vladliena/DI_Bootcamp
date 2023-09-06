const express = require('express')
const m_router = express.Router();

m_router.get('/', (req, res) => {
    res.send('Homepage')
});

m_router.get('/about', (req, res) => {
    res.send('About Us page');
});

module.exports = {m_router}