import axios from 'axios'
const apiUrl = import.meta.env.VITE_API_URL;

export const logIn = async (data) => {
    return await axios.post(`${apiUrl}/auth/signin`, data)
}