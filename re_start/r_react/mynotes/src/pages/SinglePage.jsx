import React from 'react'
import { useParams } from 'react-router-dom'

const SinglePage = () => {
   const {id} = useParams()
   const {category_id} = useParams()
  return (
    <div>
       <p>
       SinglePage ({id}) |
       Category ({category_id})
       </p>

    </div>
  )
}

export {SinglePage}
// export default SinglePage