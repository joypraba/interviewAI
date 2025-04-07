import {jwtDecode} from "jwt-decode";
export const getAccessData = () => {
    const data = sessionStorage.getItem("acces_data");
    return data ? jwtDecode(JSON.parse(data)?.["access_token"]) : null;
  };