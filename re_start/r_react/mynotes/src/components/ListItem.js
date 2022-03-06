import React from 'react'
import { Link } from 'react-router-dom'


let getDateUpd = (note) => {
  return new Date(note.updated).toLocaleDateString()
}

let getTitle = (note) => {
  let title = note.body.split('\n')[0]
  if(title.length > 30) return title.slice(0,30) // +'...'
  return title
}

let getContent = (note) => {
  let title = getTitle(note)
  let content = note.body.replaceAll('\n', ' ')
  content = content.replaceAll(title, '')
  if (content.length > 30){
    return content.slice(0,30)
  }else{
    return content
  }
}


export const ListItem = ({note}) => {
   // console.log('Props: ', props )
  return (
    <Link to={`/note/${note.id}`}>
      <div className='notes-list-item'>
        <h3>{getTitle(note)}</h3>
        <p>
          <span>{getDateUpd(note)}</span>
          {getContent(note)}
        </p>
      </div>
    </Link> 
    
  )
}
