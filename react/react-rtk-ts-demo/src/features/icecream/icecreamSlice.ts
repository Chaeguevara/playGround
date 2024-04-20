import { createSlice, PayloadAction } from '@reduxjs/toolkit'

type InitialState ={
    numOfIcecreams: number
}
const initialState:InitialState = {
    numOfIcecreams: 20
}

const icecreamSlice = createSlice({
    name: 'icecream',
    initialState,
    reducers: {
        ordered: state => {
            state.numOfIcecreams--
        },
        restocked: (state, action:PayloadAction<number>) => {
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