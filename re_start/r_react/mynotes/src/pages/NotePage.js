import {React} from 'react'
import  notes  from '../assets/data'
import { Link, useParams } from 'react-router-dom'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'
// useParams для использования параметров которые мы пердаём через /:id/:param_name
//

const NotePage = () => {
  let {id} = useParams()
  console.log({id})
  let note =  notes.find(note => note.id === Number({id}['id']))
  // console.log({id}['id'])
  return (
    <div className='note'>
      <div className='note-header'>
        <h3>
          <Link to='/'>
            <ArrowLeft />
          </Link>
        </h3>
      </div>
      <textarea value={note.body}></textarea>
       </div>
  )
}
// textarea value{[note.id , note.body]} , можно было сделать как пример передчи нескольких арг
export default NotePage