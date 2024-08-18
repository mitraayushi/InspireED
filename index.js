const express = require("express")
const app = express()
const path = require('path')

const __root = path.resolve()

app.get('/', (req,res)=> {
    res.sendFile(`${__root}/public/home.html`)
})

app.use(express.static(`${__root}/public`))

app.listen(process.env.PORT || 8000, () => {
    console.log("http://localhost:8000");//
    
})