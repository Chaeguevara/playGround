const configureStore = require('@reduxjs/toolkit').configureStore
// const reduxLogger = require('redux-logger')
const cakeReducer = require('../features/cake/cakeSlice')
const icecreamReducer = require('../features/icecream/icecreamSlice')

// const logger = reduxLogger.createLogger

const store = configureStore({
    reducer:{
        cake:cakeReducer,
        icecream:icecreamReducer,
    },
    // middleware: (getDefaultMiddleWare) => getDefaultMiddleWare().concat(logger()),
})

module.exports= store