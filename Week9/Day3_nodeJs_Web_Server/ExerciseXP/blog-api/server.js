const express = require('express')
const { articles } = require('./db')
const app = express()
const dotenv = require('dotenv')
dotenv.config();
app.use(express.urlencoded({ extended: true }))
app.use(express.json())


app.listen(process.env.PORT, () => {
    console.log(`run on port ${process.env.PORT}`)
});


app.get('/api/articles', (req, res) => {
    res.json(articles)
});

app.post('/api/articles', (req, res) => {
    const { title, content } = req.body;
    const newPost = {
        id: articles.length + 1,
        title: title,
        content: content
    }
    articles.push(newPost)
    res.json(articles)
})

app.get('/api/articles/:id', (req, res) => {
    const { id } = req.params
    const post = articles.find((item) => item.id == id)
    if (!post) {
        return res.status(404).json({ msg: 'no such post' })
    } else {
        res.json(post)
        res.status(200).json({ msg: "OK" })
    }
});

app.put('/api/articles/:id', (req, res) => {
    const { id } = req.params
    const { title, content } = req.body;
    const post = articles.find((item) => item.id == id)
    if (!post) {
        return res.status(404).json({ msg: 'no such post' })
    } else {
        const index = articles.findIndex((item) => item.id == id)
        articles[index] = { ...articles[index], title: title, content: content }
    }
    res.json(articles)
    res.status(200).json({ msg: "OK" })
});

app.delete('/api/articles/:id', (req, res) => {
    const { id } = req.params
    const index = articles.findIndex((item) => item.id == id)
    if (index === -1) return res.status(404).json({ msg: 'not found' })
    articles.splice(index, 1)
    res.json(articles)
    res.status(200).json({ msg: "OK" })

})