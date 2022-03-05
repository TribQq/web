import React from 'react'
import notes from '../assets/data'
import { ListItem } from '../components/ListItem'


export const NotesListPage = (props) => {
  console.log('props: ', props)
  return (
    <div>
      <div className='notes_list'>
        {/* {[1,2,3].map(n => (
          <p>{n}</p>
        ))} */}
        {notes.map((note,index)=>(
          // <p>{note.body}</p>
          <ListItem key={index} note={note}/>
        ))}
      </div>
    </div>
  )
}


