import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { ordered,restocked } from './icecreamSlice';

export const IcecreamView = () => {
    const [value,setValue] = useState(1)
    const numOfIcecreams = useSelector((state)=>state.icecream.numOfIcecreams)
    const dispatch = useDispatch()
    return(
        <div>
            <h2> Number of icecreams - {numOfIcecreams}</h2>
            <button onClick={()=>dispatch(ordered())}>Order icecream</button>
            <input type="number" onChange={(e)=>setValue(e.target.value)}/>
            <button onClick={()=>dispatch(restocked(value))}>Restock icecream</button>
        </div>
    )
}