import React from 'react'

export const ListItem = ({note}) => {
   // console.log('Props: ', props )
  return (
    <h3>ListItem: {note.body}</h3>
  )
}
