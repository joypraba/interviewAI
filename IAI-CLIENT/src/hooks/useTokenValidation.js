import { useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import {jwtDecode} from "jwt-decode";

const useTokenValidation = () => {
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const interval = setInterval(() => {
      const acces_data_raw = sessionStorage.getItem("acces_data");
      const params = new URLSearchParams(location.search);
      const role = params.get("role");
      if (location.pathname.includes("sign-up")) {
        return
      }
      if (!acces_data_raw) {
        if (role === "1") navigate("/admin?role=1");
        else if (role === "2") navigate("/candidate?role=2");
        else navigate("/");
        return;
      }

      try {
        const acces_data = JSON.parse(acces_data_raw);
        console.log(acces_data)
        const token = acces_data?.access_token;

        if (!token) throw new Error("Missing token");

        const decoded = jwtDecode(token);
        const now = Date.now() / 1000;

        if (decoded.exp < now) {
          sessionStorage.removeItem("acces_data");
          navigate("/");
          if (acces_data?.user_type === "1") navigate("/admin?role=1");
          else if (acces_data?.user_type === "2") navigate("/candidate?role=2");
          else navigate("/");
        }
      } catch (err) {
        console.error("Token validation error:", err);
        sessionStorage.removeItem("acces_data");
        navigate("/");
      }
    }, 10000); // check every 10 seconds

    return () => clearInterval(interval);
  }, [navigate, location]);
};

export default useTokenValidation;
