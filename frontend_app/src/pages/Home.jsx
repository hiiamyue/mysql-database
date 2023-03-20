import React from "react";
import Navbar from '../components/Navbar';
import Hero from '../components/components/Hero';
import Footer from '../components/Footer';

const Home = () => {
    return (
        <div className='bg-[url("../public/8.png")] bg-no-repeat'>
            <div className='bg-[#000300] bg-opacity-80'>
                <Navbar />
                <Hero />
                <Footer/>
            </div>
        </div>
    )
}
export default Home