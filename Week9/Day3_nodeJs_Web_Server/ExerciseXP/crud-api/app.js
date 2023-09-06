const express = require('express');
const { fetchPosts } = require('./data/dataService');
const app = express();
const port = 5000;



app.listen(port, () => {
    console.log(`run on port ${port}`)
});

app.get('/api/posts', async (req, res) => {
    try {
        const posts = await fetchPosts();
        res.json(posts);
        console.log('Data has been successfully retrieved and sent as a response.');
    } catch (error) {
        console.error('Error:', error.message);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});