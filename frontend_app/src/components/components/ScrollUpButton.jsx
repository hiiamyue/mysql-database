import React from "react";
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import Fab from '@mui/material/Fab';

const ScrollUpButton = () => {

    let mybutton = document.getElementById("myBtn");
    
    function topFunction() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    } 

    window.onscroll = function () {
        scrollFunction();
      };

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
          mybutton.style.display = "block";
        } else {
          mybutton.style.display = "none";
        }
    }

    return (
         <button className='fixed bottom-8 right-8 z-50 hidden' id="myBtn">
                    <Fab color="secondary" aria-label="edit" onClick={topFunction} size='large'>
                        <KeyboardArrowUpIcon />
                    </Fab>
        </button>   
    );
}

export default ScrollUpButton;