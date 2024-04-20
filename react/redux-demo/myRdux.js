const redux = require('@reduxjs/toolkit')
const createSlice = redux.createSlice
const configureStore = redux.configureStore
const applyMiddleware = redux.applyMiddleware
const reduxLogger = require('redux-logger')
const logger = reduxLogger.createLogger()

const counterSlice = createSlice({
    name: 'counter',
    initialState: {
        value: 0
    },
    reducers: {
        incremented: state => {
            state.value += 1
        },
        decremented: state => {
            state.value -= 1
        }
    }
})

const cakeSlice = createSlice({
    name: 'cake',
    initialState: {
        value: 10
    },
    reducers: {
        orderCake: (state, action) => {
            state.value -= action.payload
        },
        restockCake: (state, action) => {
            state.value += action.payload
        }
    }
})

const {orderCake, restockCake} = cakeSlice.actions
const { incremented, decremented } = counterSlice.actions

const rootReducer = redux.combineSlices(cakeSlice,counterSlice)

const store = configureStore({
    reducer: rootReducer,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(logger),
})

console.log('initial state',store.getState())


const actions = redux.bindActionCreators({orderCake,restockCake,incremented,decremented},store.dispatch)



// store.dispatch(incremented())
// store.dispatch(incremented())
// store.dispatch(incremented())
// store.dispatch(decremented())


actions.orderCake(2)
actions.orderCake(3)
actions.orderCake(5)
actions.orderCake(1)
actions.incremented()
actions.incremented()
actions.decremented()