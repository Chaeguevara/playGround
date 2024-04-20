import  { useState } from 'react';
import { useAppSelector,useAppDispatch } from '../../app/hooks';
import { restocked, ordered } from './cakeSlice';


export const CakeView = () => {
    const [value,setValue] = useState(1)
    const numOfCakes = useAppSelector((state) => state.cake.numOfCakes)
    const dispatch = useAppDispatch()
    return (
        <div>
            <h2>
                Number of cakes - {numOfCakes}
            </h2>
            <button onClick={() => dispatch(ordered())}>Order cake</button>
            <input type='number' onChange={(e)=>setValue(parseInt(e.target.value))}/>
            <button onClick={() => dispatch(restocked(value))}>Restock cake</button>
        </div>
    )
}