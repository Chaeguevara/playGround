import { createSlice, createAction } from '@reduxjs/toolkit'
import { ordered as orderCake } from '../cake/cakeSlice'

const initialState = {
    numOfIcecreams: 20
}

const icecreamSlice = createSlice({
    name: 'icecream',
    initialState,
    reducers: {
        ordered: state => {
            state.numOfIcecreams--
        },
        restocked: (state, action) => {
            state.numOfIcecreams += action.payload
        }
    },
    // extraReducers: (builder) => {
    //     builder
    //         .addCase(orderCake, (state, action) => {
    //             state.numOfIcecreams -= 1
    //         })
    // }

})

export default icecreamSlice.reducer
export const { ordered, restocked } = icecreamSlice.actions