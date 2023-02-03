import React, {useState} from 'react'
import {AiOutlineMenu, AiOutlineClose} from 'react-icons/ai'
import SearchBar from './SearchBar'
import { useLocation, Link } from 'react-router-dom';

const Navbar = () => {
    const [nav, setnav] = useState(true)
    const handleNav = () => {
        setnav(!nav)
    }

    const { pathname } = useLocation();

    return (
        <div className=" flex justify-between items-center h-24 max-w-[1240px] mx-auto px-4 text-white ">
            <Link to='/'><img src="logo.png" className="object-cover h-48 m-4 sm:ml-[-0px]" alt="..." /></Link>
            <div className='hidden md:flex'><SearchBar/></div>
            <ul className ='hidden md:flex'>
                {pathname === '/' ? <li className='p-4 text-fuchsia-300'>Home</li> : <Link to='/'><li className='p-4 hover:text-pink-200'>Home</li></Link>}
                {pathname === '/movies' ? <li className='p-4 text-fuchsia-300'>Movies</li> : <Link to='/movies'><li className='p-4 hover:text-pink-200'>Movies</li></Link>}
                <li className='p-4'>Genres</li>
            </ul>
            <div onClick={handleNav} className='block md:hidden sm:pr-6'>
                {!nav ? <AiOutlineClose size={20}/> : <AiOutlineMenu size={20}/>}
            </div>
            <div className={!nav ? 'z-50 fixed left-0 top-0 w-[50%] h-full border-r border-r-slate-600 border-w-200 bg-slate-800 ease-in-out duration-500 md:hidden' : 'fixed left-[-100%]'}>
                <Link to='/'><img src="logo.png" className="object-cover h-48 mt-[-48px] ml-4" alt="..." /></Link>
                <ul className='uppercase p-4 divide-y divide-slate-600'>
                    {pathname === '/' ? <li className='p-4 text-fuchsia-300'>Home</li> : <Link to='/'><li className='p-4 hover:text-pink-200'>Home</li></Link>}
                    {pathname === '/movies' ? <li className='p-4 text-fuchsia-300'>Movies</li> : <Link to='/movies'><li className='p-4 hover:text-pink-200'>Movies</li></Link>}
                    <li className='p-4'>Genres</li>
                </ul>
            </div>
        </div>
    );
}

export default Navbar