import axios from 'axios'
const apiUrl = import.meta.env.VITE_API_URL;

export const getCandidates = async () => {
    return await axios.get(`${apiUrl}/candidates`)
}