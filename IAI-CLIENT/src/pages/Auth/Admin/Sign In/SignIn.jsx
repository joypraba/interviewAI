import React, {useState} from "react";
import "./SignIn.css"
import { Link, useLocation, useNavigate  } from "react-router-dom";
// import { Button } from "bootstrap";
import { logIn } from "../../../../services/Auth";
const Login = () => {
  const navigate = useNavigate(); 
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const role = params.get("role");

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const signIn = async () => {
    
    try {
      const data = {
        email,
        password,
        type: role
      }
      const response = await logIn(data)
      sessionStorage.setItem("acces_data", JSON.stringify(response.data));
      if (response?.data?.user_type == 1) {
        console.log(response?.data?.user_type)
        navigate('/admin/dashboard')
      } else if (response?.data?.user_type == 2) {
        navigate('/candidate/dashboard')
      } else {
        navigate('/')
      }
    } catch (e) {
      console.log(e.message)
    }
  }
  const signUp = () => {
    if (role == 1) {
      navigate("/admin/sign-up?role=1")
    } else if (role == 2) {
      navigate("/candidate/sign-up?role=2")
    } else {
      navigate("/")
    }
  }

  return (
    
    <main className="d-flex w-100">
      <div className="container d-flex flex-column">
        <div className="row vh-100">
          <div className="col-sm-10 col-md-8 col-lg-6 col-xl-5 mx-auto d-table h-100">
            <div className="d-table-cell align-middle">

              <div className="text-center mt-4">
                <h1 className="h2">Welcome back!</h1>
                <p className="lead">Sign in to your account to continue</p>
              </div>

              <div className="card">
                <div className="card-body">
                  <div className="m-sm-3">
                      <div className="mb-3">
                        <label className="form-label">Email</label>
                        <input
                          className="form-control form-control-lg"
                          type="email"
                          name="email"
                          onChange={(e) => setEmail(e.target.value)}
                          placeholder="Enter your email"
                        />
                      </div>
                      <div className="mb-3">
                        <label className="form-label">Password</label>
                        <input
                          className="form-control form-control-lg"
                          type="password"
                          name="password"
                          onChange={(e) => setPassword(e.target.value)}
                          placeholder="Enter your password"
                        />
                      </div>
                      <div>
                        <div className="form-check align-items-center">
                          <input
                            id="customControlInline"
                            type="checkbox"
                            className="form-check-input"
                            value="remember-me"
                            name="remember-me"
                            defaultChecked
                          />
                          <label
                            className="form-check-label text-small"
                            htmlFor="customControlInline"
                          >
                            Remember me
                          </label>
                        </div>
                      </div>
                      <div className="d-grid gap-2 mt-3">
                        <button className="btn btn-lg btn-primary" onClick={signIn}>
                          Sign in
                        </button>
                        {/* <Link to="/admin/dashboard">Sign In</Link> */}
                      </div>
                  </div>
                </div>
              </div>

              <div className="text-center mb-3">
                Don't have an account?{" "}
                <a onClick={signUp}>Sign up</a>
              </div>

            </div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default Login;
