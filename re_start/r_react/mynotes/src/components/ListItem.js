import React from 'react'
import { Link } from 'react-router-dom'

export const ListItem = ({note}) => {
   // console.log('Props: ', props )
  return (
    <Link to={`/note/${note.id}`}>
      <div className='notes-list-item'>
        <h3>ListItem: {note.body}</h3>
      </div>
    </Link> 
    
  )
}
