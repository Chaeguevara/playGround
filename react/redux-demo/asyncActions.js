
const redux = require('redux')
const thunkMiddleware = require('redux-thunk').thunk
const axios = require('axios')
const createStore = redux.createStore
const applyMiddleware = redux.applyMiddleware
const https = require('https')
const httpsAgent = new https.Agent({
    rejectUnauthorized: false
})


const initialState = {
    loading: false,
    users: [],
    error: '',
}
const FETCH_USERS_REQUESTED = 'FETCH_USERS_REQUESTED'
const FETCH_USERS_SUCCEEDED = 'FETCH_USERS_SUCCEEDED'
const FETCH_USERS_FAILED = 'FETCH_USERS_FAILED'

const fetchUsersRequest = () => {
    return {
        type: FETCH_USERS_REQUESTED,
    }
}
const fetchUsersSucess = users => {
    return {
        type: FETCH_USERS_SUCCEEDED,
        payload: users,
    }
}
const fetchUsersFailure = error => {
    return {
        type: FETCH_USERS_FAILED,
        payload: error,
    }
}

const reducer = (state = initialState, action) => {
    switch (action.type) {
        case FETCH_USERS_REQUESTED:
            return {
                ...state,
                loading: true,
            }
        case FETCH_USERS_SUCCEEDED:
            return {
                ...state,
                loading: false,
                users: action.payload
            }
        case FETCH_USERS_FAILED:
            return {
                ...state,
                loading: false,
                error: action.payload
            }
        default:
            return state

    }

}

const fetchUsers = () => {
    return function (dispatch) {
        dispatch(fetchUsersRequest())
        axios.get("https://jsonplaceholder.typicode.com/users",{httpsAgent}).then(response => {
            const users = response.data.map(user => user.id)
            dispatch(fetchUsersSucess(users))
        }).catch(error => {
            dispatch(fetchUsersFailure(error.message))
        })
    }
}

const store = createStore(reducer, applyMiddleware(thunkMiddleware))

store.subscribe(()=> {console.log(store.getState())})
store.dispatch(fetchUsers())