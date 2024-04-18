const createSlice = require('@reduxjs/toolkit').createSlice
const createAsyncThunk = require('@reduxjs/toolkit').createAsyncThunk
const axios = require('axios')
const https = require('https')
const httpsAgent = new https.Agent({
    rejectUnauthorized: false
})

const initialState = {
    loading: false,
    users: [],
    error: ''
}

//Generated pending fullfilled and rejected action types
const fectchUsers = createAsyncThunk('user/fetchUsers', () => {
    return axios.get('https://jsonplaceholder.typicode.com/users', { httpsAgent })
        .then(response => response.data.map((user) => user.id))
})

const userSlice = createSlice({
    name: 'user',
    initialState,
    extraReducers: builder => {
        builder.addCase(fectchUsers.pending, state => {
            state.loading = true
        })
        builder.addCase(fectchUsers.fulfilled, (state, action) => {
            state.loading = false
            state.users = action.payload
            state.error = ''
        })
        builder.addCase(fectchUsers.rejected, (state, action) => {
            state.loading = false
            state.users = []
            state.error = action.error.message
        })
    },
})

module.exports = userSlice.reducer
module.exports.fetchUsers = fectchUsers