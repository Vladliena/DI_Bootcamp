import { useState, useEffect } from "react"
import postsData from '../Database.json'




const PostList = () => {

    const [posts, setPost] = useState()

    useEffect(() => {
        setPost(postsData)
    }, [])

    return (
        <div>
            {posts && posts.map((item) => {
                return (
                    <>
                        <h1>{item.title}</h1>
                        <p>{item.content}</p>
                    </>
                )
            })}

        </div>
    )

}

export default PostList