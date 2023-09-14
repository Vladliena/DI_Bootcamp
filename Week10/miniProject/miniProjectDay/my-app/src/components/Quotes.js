import quotes from "../QuotesDatabase";
import { useState, useEffect } from "react";
import './Quotes.css'


function Quotes({ }) {
    const [mainquote, setMainQuote] = useState({
        quote: '',
        author: ''
    })

    const [color, setColor] = useState('')


    useEffect(() => {
        console.log('new quote received')
        quoteGenerator()
    }, []);

    function randomColor() {
        const randomColor = Math.floor(Math.random() * 16777215).toString(16)
        setColor(`#${randomColor}`)
    }

    function quoteGenerator() {
        randomColor()
        const quotesObj = JSON.parse(JSON.stringify(quotes))
        let value = quotesObj[(Math.floor(Math.random() * quotesObj.length))];
        if (value.quote === mainquote.quote){
            return quoteGenerator()
        }
        setMainQuote({ quote: value.quote, author: value.author })
    }

    return (
        <section style={{ backgroundColor: color }}>
            <div className="wrapper">
                <h3>"{mainquote.quote}"</h3>
                <span><i>-{mainquote.author}-</i></span>
                <button onClick={quoteGenerator} style={{ backgroundColor: color, marginTop: '50px', color:'white' }}>New quote</button>
            </div>
        </section>
    );
}


export default Quotes