const redux = require('redux');
const produce = require('immer').produce
const createStore = redux.createStore

const initialState = {
    name: 'Vishwas',
    address: {
        street: '123 Main st',
        city: 'Boston',
        state: 'MA',
    },
}

const STREET_UPDATE = 'STREE_UPDATE'
const updateStreet = (street) => {
    return {
        type: STREET_UPDATE,
        payload: street,
    }
}

const reducer = (state = initialState, action) => {
    switch (action.type) {
        case STREET_UPDATE:
            // return {
            //     ...state,
            //     address: {
            //         ...state.address,
            //         street: action.payload,
            //     },
            // }
            return produce(state,(draft)=> {
                draft.address.street = action.payload

            })
        default: {
            return state
        }
    }
}

const store = createStore(reducer)
console.log('Initial state',store.getState())
const unsubscribe = store.subscribe(()=>{
    console.log('Update State',store.getState())
})
store.dispatch(updateStreet("456 Main St"))
unsubscribe()