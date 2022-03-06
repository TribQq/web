import {React, useEffect, useState} from 'react'
// import  notes  from '../assets/data'
import { Link, useParams, useNavigate } from 'react-router-dom'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'
// useParams для использования параметров которые мы пердаём через /:id/:param_name
//

const NotePage = () => {
  let {noteId} = useParams()
  let note_id={noteId}['noteId']
  console.log(note_id)

  let navigate = useNavigate();
  // let note =  notes.find(note => note.id === Number({id}['id']))
  // console.log({id}['id'])

  let [note, setNote] = useState([]) // null === error

  console.log('check point (1)')

  useEffect(()=>{
     getNote()
  }, [note_id])
  
  console.log('check point (2)')

  let getNote = async () => {
    // if (note_id === 'new') return
    console.log('try get')
    let response = await fetch(`http://localhost:7000/notes/${note_id}`)
    let data = await response.json()
    console.log('data: ' ,data)
    setNote(data)
  }

  let createNote = async () => {
    await fetch(`http://localhost:7000/notes/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body:JSON.stringify({...note, 'updated':new Date()})
    })
  }

  let updateNote = async () => {
    await fetch(`http://localhost:7000/notes/${note_id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body:JSON.stringify({...note, 'updated':new Date()})
    })
  }

  let deleteNote = async () => {
    await fetch(`http://localhost:7000/notes/${note_id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      },
      body:JSON.stringify(note)
    })
    navigate.push('/')
  }


  let handleSubmit = () => {
    if (note_id!=='new' && !note.body){
      deleteNote()
    }else if (note_id!=='new'){
      updateNote()
    }else if (note_id === 'new' && note !== []){
      createNote()
    }
    navigate.push('/')
  }

  return (
    <div className='note'>
      <div className='note-header'>
        <h3>
          <Link to='/'>
            <ArrowLeft onClick={handleSubmit} />
          </Link>
        </h3>

        <Link to='/' >
          {note_id !== 'new'? (
            <button onClick={deleteNote} >Delete</button>
          ):(
            <button onClick={handleSubmit} >Done</button>
          )}
        </Link>

        
        
      </div>
      <textarea onChange={(e) => {setNote({...note, 'body':e.target.value })}} value={note.body} ></textarea>
       </div>
  )
}
// textarea value{[note.id , note.body]} , можно было сделать как пример передчи нескольких арг
export default NotePage

// onChange={(e) => {setNote({...note, 'body':e.target.value })}}