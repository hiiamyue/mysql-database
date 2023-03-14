import React from "react";

const Footer = () => {
    return (
            <footer className='mx-auto py-16 px-4  gap-8 text-gray-50 bg-gray-900 opacity-80 z-[1000]'>
                <div className='max-w-[1240px] mx-auto'>
                    <img src="logo.png" class="object-cover h-48" alt="..." />
                    <p className="ml-4"> Lorem ipsum et dolor sit amet consectur adipising elit.</p>
                    <ul className='hidden md:flex px-auto flex-center'>
                        <li className='p-4' >Home</li>
                        <li className='p-4'>Search</li>
                        <li className='p-4'>Genres</li>
                    </ul>

                    <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
                    <span class="block text-sm text-gray-500 sm:text-center dark:text-gray-400">© <a href="https://ucl.ac.uk/" class="hover:underline">Dataflix™</a> (COMP0022). All Rights Reserved.
                    </span>

                </div>
                
            </footer>
    );
}

export default Footer;