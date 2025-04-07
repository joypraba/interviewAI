import axios from 'axios'
const apiUrl = import.meta.env.VITE_API_URL;

export const logIn = async (data) => {
    return await axios.post(`${apiUrl}/auth/signin`, data)
}

export const recruiterSignUp = async (data) => {
    return await axios.post(`${apiUrl}/recruiters`, data)
}
export const candidateSignUp = async (data) => {
    return await axios.post(`${apiUrl}/candidates`, data, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
}