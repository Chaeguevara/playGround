import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios'



const initialState = {
    loading: false,
    users: [],
    error: ''
}

//Generated pending fullfilled and rejected action types
export const fectchUsers = createAsyncThunk('user/fetchUsers', () => {
    return axios.get('https://jsonplaceholder.typicode.com/users', )
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

export default userSlice.reducer