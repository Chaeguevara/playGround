const createSlice = require('@reduxjs/toolkit').createSlice
const createAction = require('@reduxjs/toolkit').createAction
const orderCake = createAction('cake/ordered')

const initialState = {
    numOfIcecreams: 20
}

const icecreamSlice = createSlice({
    name: 'icecream',
    initialState,
    reducers: {
        ordered: state=>{
            state.numOfIcecreams--
        },
        restocked: (state,action)=>{
            state.numOfIcecreams+=action.payload
        }
    },
    extraReducers: (builder)=>{
        builder
        .addCase(orderCake, (state,action) =>{
            state.numOfIcecreams -= 1
        })
    }

})

module.exports = icecreamSlice.reducer
module.exports.icecreamActions = icecreamSlice.actions