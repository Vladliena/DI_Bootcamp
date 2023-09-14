import { useState } from "react";
import './Todo.css'

function Todo() {
    const [todo, setTodo] = useState([
        {
            id: null,
            task: 'something'
        }
    ])

    function randomNumber() {
        let random;
        do {
            random = Math.floor(Math.random() * 100);
            return random
        } while (random === todo.id)
    }

    function handleChange(e) {
        if (e.key === 'Enter') {
            let randId = randomNumber()
            setTodo(current => [...current, { id: randId, task: e.target.value }]);
        }
        console.log(todo)
    }

    function deleteTask(id) {
        const data = todo.filter(item => item.id !== id)
        setTodo(data)
    }

    return (
        <div style={{ width: "500px", margin: 'auto' }}>
            <h1 className="header">TODO'S</h1>
            <div>
                {todo.length === 0 ? 'You have no todos left, yay!' : todo.map((item) => {
                    return (
                        <>
                            <div style={{ backgroundColor: "beige", borderBottom: "1px grey solid", paddingBottom: "5px" }} className="task_txt" onClick={() => deleteTask(item.id)}>{item.task}</div>
                        </>
                    )
                })}
            </div>
            <label for='task'>Add a new todo: </label>
            <input name='task' id='task' type="text" onKeyDown={(e) => handleChange(e)}></input>
            <hr />
        </div>
    )
}

export default Todo