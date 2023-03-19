import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import {Badge, Card} from "flowbite-react"

const CastCard = ({ name, role }) => {
  
  return (
    <div className="sm:w-[14em] w-[12em] mx-4 sm:mx-0">
        <Card
            imgAlt="Meaningful alt text for an image that is not purely decorative"
            imgSrc="character.jpg"
        >
            <h5 className="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
            {name}
            </h5>
            <p className="font-normal text-gray-700 dark:text-gray-400 mt-[-1em]">
            {role}
            </p>
        </Card>
                    
    </div>
  );
};

export default CastCard;