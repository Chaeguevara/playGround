const redux = require('redux');
const createStore = redux.createStore
const bindActionCreators = redux.bindActionCreators
const combineReducers = redux.combineReducers
const applyMiddleware = redux.applyMiddleware

const reduxLogger = require('redux-logger')
const logger = reduxLogger.createLogger()

const CAKE_ORDERED = 'CAKE_ORDERED'
const CAKE_RESTOCKED = 'CAKE_RESTOCKED'
const ICECREAM_ORDERED = "ICECREAM_ORDERED"
const ICECREAME_RESTOCKED = "ICECREAME_RESTOCKED"


function orderCake() {
    return {
        type: CAKE_ORDERED,
        payload: 1
    }
}

function restockCake(qty = 1) {
    return {
        type: CAKE_RESTOCKED,
        payload: qty
    }
}

function orderIceCream(qty = 1) {
    return {
        type: ICECREAM_ORDERED,
        payload: qty
    }
}

function restockIceCream(qty = 1) {
    return {
        type: ICECREAME_RESTOCKED,
        payload: qty
    }
}



// const initialState = {
//     numOfCakes: 10,
//     numOfIcecreams:20,
// }

const initalCakeState = {
    numOfCakes: 10,
}
const initalIceCreamState = {
    numOfIceCreams: 20,
}

// (prevState, action )=> newState

const cakeReducer = (state = initalCakeState, action) => {
    switch (action.type) {
        case CAKE_ORDERED:
            return {
                ...state,
                numOfCakes: state.numOfCakes - 1
            }
        case CAKE_RESTOCKED:
            return {
                ...state,
                numOfCakes: state.numOfCakes + action.payload
            }
        default:
            return state
    }
}

const iceCreamReducer = (state = initalIceCreamState, action) => {
    switch (action.type) {
        case ICECREAM_ORDERED:
            return {
                ...state,
                numOfIceCreams: state.numOfIceCreams - 1
            }
        case ICECREAME_RESTOCKED:
            return {
                ...state,
                numOfIceCreams: state.numOfIceCreams + action.payload
            }
        default:
            return state
    }
}

const rootReducer = combineReducers({
    cake:cakeReducer,
    iceCream:iceCreamReducer
})

const store = createStore(rootReducer,applyMiddleware(logger))
console.log('initial state', store.getState())

const unsubscribe = store.subscribe(() =>{})

// store.dispatch(orderCake())
// store.dispatch(orderCake())
// store.dispatch(orderCake())
// store.dispatch(restockCake(10))
const actions = bindActionCreators({ orderCake, restockCake, orderIceCream, restockIceCream }, store.dispatch)
actions.orderCake()
actions.orderCake()
actions.orderCake()
actions.restockCake(3)
actions.orderIceCream()
actions.orderIceCream()
actions.orderIceCream()
actions.restockIceCream(3)

unsubscribe()