import React from 'react'
import Link from 'next/link'
const Header = () => {
  return (
    <div className=' mt-5 bg-blue-500 flex justify-between items-center '>
      <h1 className=' text-2xl font-semibold '>
        <Link href='/'>
          KeyAssign
        </Link>
      </h1>
      <div className='  '>
        <Link href='/'>
          KeyAssign
        </Link>
        <Link href='/'>
          KeyAssign
        </Link>
        <Link href='/'>
          <button>Github</button>
        </Link>
      </div>
    </div>
  )
}

export default Header
