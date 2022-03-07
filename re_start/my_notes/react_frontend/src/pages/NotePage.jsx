import {React, useState, useEffect} from 'react'
import ListItem from '../components/ListItem'
import { Link, useParams, useNavigate } from 'react-router-dom'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'


const NotePage = () => {
   let navigate = useNavigate();
   let {note_id} = useParams()
   note_id = {note_id}['note_id']

   let [note, setNote] = useState([])

   useEffect(()=>{
      getNotes()
   }, [note_id])

   let getNotes = async () =>{
      if (note_id==='note_create') return // 2//11 need stop this f if new note
      let response = await fetch(`/api/note/${note_id}`)
      let data = await response.json()
      console.log('DATA: ', data)
      setNote(data)
   }


   let updadteNote = async () => {
      fetch(`/api/note/${note_id}/update`, {
         method : "PUT",
         headers:{
            'Content-Type': 'application/json'
         },
         body: JSON.stringify(note)
      })
   }


   let handleSubmit = () =>{
      console.log(`note: ${note},\nnote_body${note.body}`)
      if (note_id !== 'note_create' && !note.body) deleteNote()
      else if (note_id !== 'note_create') updadteNote()
      else if (note_id === 'note_create' && note !== []) {
         createNote()
      }
      navigate('../notes')
   }


   let deleteNote = async () => {
      await fetch(`/api/note/${note_id}/delete`, {
         method : 'DELETE',
         headers:{
            'Content-Type': 'application/json'
         }
      })
      navigate('../../notes')
   }

   let createNote = async () => {
      fetch(`/api/note/note_create`, {
         method : "POST",
         headers:{
            'Content-Type': 'application/json'
         },
         body:JSON.stringify(note) // мы передаём в бэк request.data // json(note)
      })
      navigate('../../notes')
   }

   let myButton = (note_id) => {
      if (note_id !== 'note_create') {
         return <button onClick={deleteNote}> Delete </button>
      }else {
      return <button onClick={createNote}> Create </button>}
   }

   console.log('userParams(): ', useParams())
   console.log(note_id, 'note_id')
   return (
    <div>
       <div className='note'>
          <div className='note-header'>
               <h3>
                    <ArrowLeft onClick={handleSubmit} />
               </h3>
               {myButton(note_id)}
               
            </div>
            <textarea onChange={(e) => {setNote({...note, 'body':e.target.value})}} defaultValue={note.body}></textarea>
      </div>
    </div>
  )
}

export default NotePage


// { note_id === 'new'?(
//    <button> Create </button>
// ):(
// <button onClick={deleteNote}> Delete </button>
// )
// }