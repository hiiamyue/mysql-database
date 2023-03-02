import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import {Badge, Card} from "flowbite-react"

const CastCard = () => {
  
  return (
    <div className="w-[13em]">
        <Card
            imgAlt="Meaningful alt text for an image that is not purely decorative"
            imgSrc="character.jpg"
        >
            <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
            Chris Colombus
            </h5>
            <p className="font-normal text-gray-700 dark:text-gray-400 mt-[-1em]">
            Director
            </p>
        </Card>
                    
    </div>
  );
};

export default CastCard;